from typing import Optional, Union
from urllib.parse import urlparse

from airflow.exceptions import AirflowException
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.sensors.base import BaseSensorOperator

import re
import fnmatch
import logging as log


class CustomS3KeySensor(BaseSensorOperator):
    template_fields = ('bucket_key', 'bucket_name')

    def __init__(
            self,
            *,
            bucket_key: str,
            bucket_name: Optional[str] = None,
            aws_conn_id: str = 'aws_default',
            delimiter='/',
            verify: Optional[Union[str, bool]] = None,
            **kwargs,
    ):
        super().__init__(**kwargs)
        self.bucket_name = bucket_name
        self.bucket_key = bucket_key
        self.aws_conn_id = aws_conn_id
        self.verify = verify
        self.hook: Optional[S3Hook] = None
        self.delimiter = delimiter

    def poke(self, context):

        if self.bucket_name is None:
            parsed_url = urlparse(self.bucket_key)
            if parsed_url.netloc == '':
                raise AirflowException('If key is a relative path from root, please provide a bucket_name')
            self.bucket_name = parsed_url.netloc
            self.bucket_key = parsed_url.path.lstrip('/')
        else:
            parsed_url = urlparse(self.bucket_key)
            if parsed_url.scheme != '' or parsed_url.netloc != '':
                raise AirflowException(
                    'If bucket_name is provided, bucket_key'
                    + ' should be relative path from root'
                    + ' level, rather than a full s3:// url'
                )

        self.log.info('Poking for key : s3://%s/%s', self.bucket_name, self.bucket_key)
        is_present = self.get_hook().check_for_wildcard_key(self.bucket_key, self.bucket_name)

        if is_present:  # TODO get name of the key
            # TODO refactor
            prefix = re.split(r'[*]', self.bucket_key, 1)[0]
            key_list = self.get_hook().list_keys(self.bucket_name, prefix=prefix, delimiter=self.delimiter)
            key_matches = [k for k in key_list if fnmatch.fnmatch(k, self.bucket_key)]
            if key_matches:
                context['task_instance'].xcom_push('bucket_key', str(key_matches[0]))
                # key = self.get_hook().get_key(key_matches[0], self.bucket_name)

        return is_present

    def get_hook(self) -> S3Hook:
        """Create and return an S3Hook"""
        if self.hook:
            return self.hook

        self.hook = S3Hook(aws_conn_id=self.aws_conn_id, verify=self.verify)
        return self.hook

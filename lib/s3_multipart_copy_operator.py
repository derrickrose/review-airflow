from typing import Sequence, Optional, Union

from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

MAXIMUM_ALLOWABLE_SIZE = 5368709120


class S3MultiPartCopyObjectOperator(BaseOperator):
    """
    Creates a copy of an object that is already stored in S3.

    Note: the S3 connection used here needs to have access to both
    source and destination bucket/key.

    .. seealso::
        For more information on how to use this operator, take a look at the guide:
        :ref:`howto/operator:S3CopyObjectOperator`

    :param source_bucket_key: The key of the source object. (templated)

        It can be either full s3:// style url or relative path from root level.

        When it's specified as a full s3:// url, please omit source_bucket_name.
    :param dest_bucket_key: The key of the object to copy to. (templated)

        The convention to specify `dest_bucket_key` is the same as `source_bucket_key`.
    :param source_bucket_name: Name of the S3 bucket where the source object is in. (templated)

        It should be omitted when `source_bucket_key` is provided as a full s3:// url.
    :param dest_bucket_name: Name of the S3 bucket to where the object is copied. (templated)

        It should be omitted when `dest_bucket_key` is provided as a full s3:// url.
    :param source_version_id: Version ID of the source object (OPTIONAL)
    :param aws_conn_id: Connection id of the S3 connection to use
    :param verify: Whether or not to verify SSL certificates for S3 connection.
        By default SSL certificates are verified.

        You can provide the following values:

        - False: do not validate SSL certificates. SSL will still be used,
                 but SSL certificates will not be
                 verified.
        - path/to/cert/bundle.pem: A filename of the CA cert bundle to uses.
                 You can specify this argument if you want to use a different
                 CA cert bundle than the one used by botocore.
    :param acl_policy: String specifying the canned ACL policy for the file being
        uploaded to the S3 bucket.
    """

    template_fields: Sequence[str] = (
        'source_bucket_key',
        'dest_bucket_key',
        'source_bucket_name',
        'dest_bucket_name',
    )

    def __init__(
            self,
            *,
            source_bucket_key: str,
            dest_bucket_key: str,
            source_bucket_name: Optional[str] = None,
            dest_bucket_name: Optional[str] = None,
            source_version_id: Optional[str] = None,
            aws_conn_id: str = 'aws_default',
            verify: Optional[Union[str, bool]] = None,
            acl_policy: Optional[str] = None,
            **kwargs,
    ):
        super().__init__(**kwargs)

        self.source_bucket_key = source_bucket_key
        self.dest_bucket_key = dest_bucket_key
        self.source_bucket_name = source_bucket_name
        self.dest_bucket_name = dest_bucket_name
        self.source_version_id = source_version_id
        self.aws_conn_id = aws_conn_id
        self.verify = verify
        self.acl_policy = acl_policy

    def execute(self, context: 'Context'):
        s3_hook = S3Hook(aws_conn_id=self.aws_conn_id, verify=self.verify)
        head_response = s3_hook.head_object(self.source_bucket_key, self.source_bucket_name)
        if head_response and head_response["ContentLength"] and head_response[
            "ContentLength"] >= MAXIMUM_ALLOWABLE_SIZE:
            print(
                f"Copy source size {head_response['ContentLength']} is bigger than maximum allowable size, will proceed with multi-part copy!")
            copy_source = {
                'Bucket': self.source_bucket_name,
                'Key': self.source_bucket_key
            }
            # multi-part copy
            s3_hook.get_conn().copy(copy_source, self.dest_bucket_name, self.dest_bucket_key)
        else:
            s3_hook.copy_object(
                self.source_bucket_key,
                self.dest_bucket_key,
                self.source_bucket_name,
                self.dest_bucket_name,
                self.source_version_id,
                self.acl_policy,
            )

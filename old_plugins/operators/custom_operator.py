from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging as log


class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        log.info(f"{self.__class__.__name__} execute on plugin with param {self.param}")

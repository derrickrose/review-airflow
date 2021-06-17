from airflow.models import BaseOperator
from airflow.utils import apply_defaults
import logging as log


class ReviewOperator(BaseOperator):

    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super.__init__(args, kwargs)
        self.param = param

    def execute(self, context):
        log.info("{} execute with param {}".format(self.__class__.__name__, self.param))

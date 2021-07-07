FROM python:3.8-buster

# set airflow home env variable
ENV AIRFLOW_HOME=/user/local/airflow

# Define en_US local
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

# add local files to airflow home dir
ADD . /user/local/airflow

# all command would be run from this dir
WORKDIR "/user/local/airflow"

# install all airflow dependencies
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:$AIRFLOW_HOME

EXPOSE 8080

RUN chmod u+x entrypoint.sh

ENTRYPOINT ["/usr/local/airflow/entrypoint.sh"]
CMD ["webserver"]


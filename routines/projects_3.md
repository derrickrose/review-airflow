 **README 3 - Projet AWS Airflow + Spark**
``` markdown
# AWS Airflow + Spark Advanced Data Engineering Project

## 🎯 Project Overview
### "Enterprise Data Lake avec Apache Airflow sur Amazon MWAA et Apache Spark sur EMR"

**Duration:** 10-12 jours
**Focus:** AWS native orchestration + distributed processing
**Level:** Senior/Lead Data Engineer
**Target TJM:** 800-950€/jour

## 🏗️ Architecture Complète
```
Data Sources → S3 Landing → Airflow (MWAA) → EMR Spark → Data Lake → Analytics ↓ ↓ ↓ ↓ ↓ ↓ [APIs/SFTP] [Raw Zone] [Orchestration] [Processing] [Gold Zone] [Dashboards] ↓ ↓ ↓ ↓ ↓ ↓ EventBridge → Lambda → Airflow DAGs → Spark Jobs → Athena → QuickSight
``` 

**Services AWS Principaux:**
- **Orchestration**: Amazon MWAA (Managed Airflow)
- **Processing**: EMR (Elastic MapReduce) avec Spark 3.4+
- **Storage**: S3 avec partitioning optimisé
- **Catalog**: Glue Data Catalog + Athena
- **Monitoring**: CloudWatch + Airflow native monitoring
- **Security**: IAM roles + Lake Formation

## 🚀 Components Détaillés

### 1. Amazon MWAA Setup (Advanced)
**Configuration Airflow:**
```
python
# airflow.cfg customizations
[core] executor = CeleryExecutor max_active_runs_per_dag = 3 dagbag_import_timeout = 60
[webserver] authenticate = True auth_backend = airflow.providers.amazon.aws.auth_manager.aws_auth_manager.AwsAuthManager
[scheduler] catchup_by_default = False max_tis_per_query = 16
``` 

**Custom Operators:**
- **EMRSparkOperator** avec auto-scaling
- **S3DataQualityOperator** avec Great Expectations
- **SlackNotificationOperator** pour alertes business
- **DynamoDBSensorOperator** pour event-driven workflows

### 2. EMR Spark Jobs (Production-Ready)

**Cluster Configuration:**
```
json { "Applications": [{"Name": "Spark"}, {"Name": "Hive"}, {"Name": "Hadoop"}], "BootstrapActions": [ { , "Instances": { "MasterInstanceType": "m5.xlarge", "SlaveInstanceType": "r5.2xlarge", "InstanceCount": 5, "Ec2KeyName": "your-key", "KeepJobFlowAliveWhenNoSteps": false }, "JobFlowRole": "EMR_EC2_DefaultRole", "ServiceRole": "EMR_DefaultRole" }
latex_unknown_tag
``` 

**Spark Applications:**
- **Customer Data ETL**: Join multiple sources + deduplication
- **Transaction Processing**: Streaming + batch reconciliation  
- **Feature Engineering**: ML features avec Delta Lake format
- **Data Quality Checks**: Automated validation + anomaly detection

### 3. Advanced DAG Patterns

**Parent DAG - Data Pipeline Orchestrator:**
```
python from airflow import DAG from airflow.providers.amazon.aws.operators.emr import EmrCreateJobFlowOperator from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor from datetime import datetime, timedelta
default_args = { 'owner': 'data-engineering-team', 'depends_on_past': False, 'start_date': datetime(2025, 1, 1), 'email_on_failure': True, 'email_on_retry': False, 'retries': 2, 'retry_delay': timedelta(minutes=5), 'sla': timedelta(hours=4) }
dag = DAG( 'enterprise_data_pipeline', default_args=default_args, description='Enterprise Data Lake ETL Pipeline', schedule_interval='@daily', catchup=False, tags=['production', 'data-lake', 'emr', 'spark'] )
# Sensor pour déclenchement basé sur arrivée des données
data_arrival_sensor = S3KeySensor( task_id='wait_for_raw_data', bucket_name='enterprise-data-lake-raw', bucket_key='daily-extract/{{ ds }}/data_ready.flag', wildcard_match=False, timeout=7200, poke_interval=300, dag=dag )
# EMR Cluster creation avec auto-scaling
create_emr_cluster = EmrCreateJobFlowOperator( task_id='create_emr_cluster', job_flow_overrides=EMR_CONFIG, aws_conn_id='aws_default', emr_conn_id='emr_default', dag=dag )
latex_unknown_tag
latex_unknown_tag
``` 

**Child DAGs - Domaines métier:**
- **Customer Processing DAG**
- **Transaction Processing DAG** 
- **Risk Analytics DAG**
- **Regulatory Reporting DAG**

### 4. Spark Applications Avancées

**Customer 360 ETL (Scala + Spark):**
```
scala import org.apache.spark.sql.{DataFrame, SparkSession} import org.apache.spark.sql.functions._
object Customer360ETL { def main(args: Array[String]): Unit = { val spark = SparkSession.builder() .appName("Customer360ETL") .config("spark.sql.adaptive.enabled", "true") .config("spark.sql.adaptive.coalescePartitions.enabled", "true") .getOrCreate()
// Optimized joins avec broadcast hints
val customers = spark.read
  .format("delta")
  .load("s3a://data-lake-silver/customers/")
  .repartition(col("customer_segment"))

val transactions = spark.read
  .format("delta")
  .load("s3a://data-lake-silver/transactions/")
  .filter(col("transaction_date") >= date_sub(current_date(), 90))

// Feature engineering pour ML
val customer360 = customers
  .join(broadcast(transactions), "customer_id")
  .groupBy("customer_id", "customer_segment")
  .agg(
    sum("transaction_amount").as("total_spend_90d"),
    count("transaction_id").as("transaction_count_90d"),
    avg("transaction_amount").as("avg_transaction_amount"),
    stddev("transaction_amount").as("transaction_volatility")
  )

// Écriture avec optimizations
customer360.write
  .format("delta")
  .mode("overwrite")
  .partitionBy("customer_segment")
  .option("overwriteSchema", "true")
  .save("s3a://data-lake-gold/customer360/")
} }
``` 

**Real-Time + Batch Lambda Architecture (Python + PySpark):**
```
python from pyspark.sql import SparkSession from pyspark.sql.functions import * from pyspark.sql.types import * import boto3
def process_streaming_data(): """Process real-time transactions via Kinesis""" spark = SparkSession.builder
.appName("RealTimeTransactionProcessing")
.config("spark.jars.packages", "org.apache.spark:spark-sql-kinesis_2.12:3.4.0")
.getOrCreate()
# Kinesis stream reading
kinesis_df = spark \
    .readStream \
    .format("kinesis") \
    .option("streamName", "transaction-stream") \
    .option("region", "eu-west-1") \
    .option("initialPosition", "TRIM_HORIZON") \
    .load()

# Real-time transformations
processed_df = kinesis_df \
    .select(from_json(col("data").cast("string"), transaction_schema).alias("transaction")) \
    .select("transaction.*") \
    .withColumn("processing_time", current_timestamp()) \
    .withColumn("fraud_score", calculate_fraud_score(col("amount"), col("merchant_category")))

# Write to S3 + DynamoDB
query = processed_df.writeStream \
    .outputMode("append") \
    .format("delta") \
    .option("path", "s3a://data-lake-silver/transactions-streaming/") \
    .option("checkpointLocation", "s3a://checkpoints/transactions/") \
    .trigger(processingTime="30 seconds") \
    .start()

return query
def process_batch_data(): """Daily batch processing pour reconciliation""" spark = SparkSession.builder
.appName("BatchTransactionReconciliation")
.config("spark.sql.adaptive.enabled", "true")
.getOrCreate()
# Compare streaming vs batch results
streaming_data = spark.read.format("delta").load("s3a://data-lake-silver/transactions-streaming/")
batch_data = spark.read.format("delta").load("s3a://data-lake-silver/transactions-batch/")

# Data quality checks
reconciliation_report = streaming_data.join(
    batch_data, 
    ["transaction_id", "transaction_date"], 
    "full_outer"
).select(
    when(streaming_data.transaction_id.isNull(), "missing_in_streaming")
    .when(batch_data.transaction_id.isNull(), "missing_in_batch")
    .otherwise("matched").alias("status"),
    count("*").alias("count")
).groupBy("status").agg(sum("count"))

# Send to CloudWatch metrics
send_metrics_to_cloudwatch(reconciliation_report)
``` 

## 🎛️ Advanced Airflow Patterns

### 1. Dynamic DAG Generation
```python
from airflow.models import Variable
import json

# Configuration driven DAGs
CONFIG = Variable.get("etl_config", deserialize_json=True)

for domain, config in CONFIG['domains'].items():
    dag_id = f"etl_{domain}_processing"
    
    # Create dynamic DAG per business domain
    globals()[dag_id] = create_domain_dag(
        dag_id=dag_id,
        domain=domain,
        config=config,
        schedule_interval=config.get('schedule', '@daily')
    )
```
```
### 2. Custom Sensors & Operators
``` python
class EMRSparkJobSensor(BaseSensorOperator):
    """Custom sensor pour EMR job completion avec retry logic"""

    def __init__(self, job_flow_id, step_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_flow_id = job_flow_id
        self.step_id = step_id
        self.emr_client = boto3.client('emr')

    def poke(self, context):
        response = self.emr_client.describe_step(
            ClusterId=self.job_flow_id,
            StepId=self.step_id
        )

        state = response['Step']['Status']['State']

        if state == 'COMPLETED':
            return True
        elif state in ['CANCELLED', 'FAILED', 'INTERRUPTED']:
            raise AirflowException(f"EMR step failed: {state}")

        return False


class DataQualityOperator(BaseOperator):
    """Custom operator pour data quality avec Great Expectations"""

    def execute(self, context):
        # Great Expectations validation
        data_context = DataContext()
        suite_name = "transaction_validation_suite"

        batch = data_context.get_batch(
            batch_kwargs={"path": self.s3_path, "datasource": "s3_datasource"},
            expectation_suite_name=suite_name
        )

        results = data_context.run_validation_operator(
            "action_list_operator",
            assets_to_validate=[batch]
        )

        if not results["success"]:
            raise AirflowException("Data quality validation failed")
```
### 3. Advanced Scheduling & SLA Management
``` python
# SLA monitoring with custom callbacks
def sla_miss_callback(dag, task_list, blocking_task_list, slas, blocking_tis):
    """Custom SLA miss handling"""
    slack_message = f"""
    🚨 SLA BREACH ALERT 🚨
    DAG: {dag.dag_id}
    Tasks: {[t.task_id for t in task_list]}
    Blocking: {[t.task_id for t in blocking_tis]}
    """
    send_slack_notification(slack_message)
    create_jira_incident(dag.dag_id, task_list)


# Custom timetable pour business hours
class BusinessHoursTimetable(Timetable):
    """Execute only during business hours (9-18 CET)"""

    def next_dagrun_info(self, last_automated_run, restriction):
        if last_automated_run is None:
            next_run = pendulum.now("Europe/Paris").replace(hour=9, minute=0, second=0)
        else:
            next_run = last_automated_run + timedelta(hours=1)

        # Skip weekends and non-business hours
        while next_run.weekday() >= 5 or not (9 <= next_run.hour < 18):
            next_run = next_run + timedelta(hours=1)

        return DagRunInfo.interval(next_run, next_run + timedelta(hours=1))
```
## 📊 Monitoring & Observability
### 1. Custom CloudWatch Metrics
``` python
def send_custom_metrics(metric_name, value, unit='Count', dimensions=None):
    """Send custom metrics to CloudWatch"""
    cloudwatch = boto3.client('cloudwatch')

    cloudwatch.put_metric_data(
        Namespace='DataEngineering/Pipeline',
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value,
                'Unit': unit,
                'Dimensions': dimensions or []
            }
        ]
    )


# Dans vos DAGs
def track_data_quality_metrics(**context):
    task_instance = context['task_instance']

    # Custom metrics
    send_custom_metrics('DataQuality.RecordsProcessed', records_processed)
    send_custom_metrics('DataQuality.ErrorRate', error_rate, 'Percent')
    send_custom_metrics('Pipeline.Duration', duration_seconds, 'Seconds')
```
### 2. Airflow + Spark Monitoring Integration
``` python
# Spark History Server integration
SPARK_HISTORY_SERVER = "http://emr-master:18080"


def get_spark_application_metrics(application_id):
    """Get Spark app metrics from History Server"""
    response = requests.get(f"{SPARK_HISTORY_SERVER}/api/v1/applications/{application_id}")
    return response.json()


# Dans vos Spark operators
class MonitoredEMRAddStepsOperator(EmrAddStepsOperator):
    def execute(self, context):
        step_id = super().execute(context)

        # Wait for completion then collect metrics
        self.wait_for_completion(step_id)
        metrics = self.collect_spark_metrics(step_id)

        # Send to monitoring system
        self.send_metrics_to_cloudwatch(metrics)

        return step_id
```
## 💰 Cost Optimization Strategies
### 1. EMR Spot Instances avec Auto-Recovery
``` python
EMR_CONFIG_OPTIMIZED = {
    "Instances": {
        "MasterInstanceType": "m5.xlarge",
        "InstanceFleets": [
            {
                "Name": "MasterFleet",
                "InstanceFleetType": "MASTER",
                "TargetOnDemandCapacity": 1,
                "TargetSpotCapacity": 0,
                "InstanceTypeConfigs": [
                    {"InstanceType": "m5.xlarge", "BidPrice": "0.05"}
                ]
            },
            {
                "Name": "CoreFleet",
                "InstanceFleetType": "CORE",
                "TargetOnDemandCapacity": 1,
                "TargetSpotCapacity": 4,
                "InstanceTypeConfigs": [
                    {"InstanceType": "r5.2xlarge", "BidPrice": "0.15"},
                    {"InstanceType": "r5.xlarge", "BidPrice": "0.08"}
                ]
            }
        ]
    },
    "AutoTerminationPolicy": {"IdleTimeout": 3600}  # 1h idle = terminate
}
```
### 2. Intelligent Scheduling
``` python
# Cost-aware scheduling
def get_spot_price_schedule():
    """Determine optimal execution time based on spot prices"""
    ec2 = boto3.client('ec2')

    # Get historical spot prices
    response = ec2.describe_spot_price_history(
        InstanceTypes=['r5.2xlarge'],
        ProductDescriptions=['Linux/UNIX'],
        MaxResults=168  # 1 week
    )

    # Find cheapest hour pattern
    cheapest_hours = analyze_price_patterns(response['SpotPrices'])
    return cheapest_hours


# Dynamic DAG scheduling based on cost
for hour in get_spot_price_schedule()[:3]:  # Top 3 cheapest hours
    create_cost_optimized_dag(schedule_hour=hour)
```
## 🎯 Business Use Cases Implementés
### 1. Banking Transaction Processing
- **Real-time fraud detection** (<100ms response)
- **Regulatory reporting** (automated BCBS compliance)
- **Customer 360** (real-time + batch features)

### 2. E-commerce Analytics
- **Product recommendation** features
- **Inventory optimization** avec ML forecasting
- **Customer churn prediction** pipeline

### 3. IoT Data Processing
- **Sensor data streaming** avec anomaly detection
- **Predictive maintenance** features
- **Real-time dashboards** pour operations

## 📈 Success Metrics & KPIs
### Technical Metrics
- **Pipeline SLA**: 99.5% on-time completion
- **Data freshness**: <15min average latency
- **Cost efficiency**: 40% reduction vs baseline EC2
- **Error rate**: <0.1% failed tasks

### Business Metrics
- **Data quality score**: >99% automated validation
- **Developer productivity**: 50% faster feature development
- **Compliance**: 100% automated regulatory reporting
- **Stakeholder satisfaction**: Self-service analytics adoption

## 🚀 Deliverables
### 1. Code Repository
``` 
aws-airflow-spark-enterprise/
├── dags/                          # Airflow DAGs
│   ├── enterprise_data_pipeline.py
│   ├── customer_360_processing.py
│   └── real_time_fraud_detection.py
├── plugins/                       # Custom operators & sensors
├── spark_jobs/                    # Spark applications
│   ├── scala/                     # Scala applications  
│   └── python/                    # PySpark jobs
├── infrastructure/                # Terraform IaC
├── monitoring/                    # CloudWatch dashboards
├── docs/                         # Architecture & runbooks
└── tests/                        # Unit & integration tests
```
### 2. Infrastructure as Code
- **Complete Terraform modules** pour MWAA + EMR
- **Auto-scaling policies** et cost optimization
- **Multi-environment** (dev/staging/prod) support
- **Security best practices** (IAM, encryption, VPC)

### 3. Documentation & Knowledge Transfer
- **Architecture Decision Records** (ADRs)
- **Operational runbooks** pour troubleshooting
- **Performance tuning guides** pour Spark + Airflow
- **Cost optimization playbook**

## 💡 Competitive Advantages
**Ce projet vous positionne comme expert sur:**
- **MWAA advanced patterns** (rare sur le marché français)
- **EMR cost optimization** (expertise recherchée)
- **Production-ready Spark** avec monitoring intégré
- **Enterprise data architecture** avec compliance

**ROI Client immédiat:**
- Infrastructure prête-à-déployer
- Patterns éprouvés en production
- Monitoring et alerting inclus
- Documentation complète

**TJM justifié:** 850-950€/jour pour missions Lead Data Engineer avec composante architecture.
_Projet conçu pour démontrer votre maîtrise des technologies AWS data les plus demandées en 2025_

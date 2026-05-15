#!/usr/bin/env python3
"""Modify dagggbbb1.py to implement ShortCircuit approach with mode parameter."""

# Read the original file
with open('dags/dagggbbb.py', 'r') as f:
    content = f.read()

# 1. Change DAG_ID
content = content.replace(
    'DAG_ID = f"{ENV_UPPER}_LCRR_D004_RTS24_CLASSIC"',
    'DAG_ID = f"{ENV_UPPER}_LCRR_D004_RTS24_CLASSIC_1"'
)

# 2. Update process_on_demand_query_results to not pull trading_date from extract_trading_date
content = content.replace(
    '''@task
def process_on_demand_query_results(**context):
    """Process Athena query results and build EMR params for dynamic mapping."""
    ti = context["ti"]
    trading_date = ti.xcom_pull(task_ids="extract_trading_date")
    query_execution_id = ti.xcom_pull(task_ids="query_on_demand_table")

    # Ensure string type for JSON serialization in downstream dynamic mapping
    trading_date = str(trading_date)''',
    '''@task
def process_on_demand_query_results(**context):
    """Process Athena query results and build EMR params for dynamic mapping."""
    ti = context["ti"]
    query_execution_id = ti.xcom_pull(task_ids="query_on_demand_table")

    # For on-demand requests, trading_date comes from each row's data
    trading_date = None  # Will be overridden by row-specific trading_date'''
)

# 3. Add ShortCircuit tasks before DAG definition
shortcircuit_code = '''
@task.short_circuit
def should_run_loads(**context):
    """Determine if load tasks should run based on mode parameter."""
    conf = context.get('dag_run').conf or {}
    mode = conf.get('mode', 'full')
    logger.info(f"Execution mode: {mode}")
    logger.info(f"should_run_loads: {mode in ['full', 'loads_only']}")
    return mode in ['full', 'loads_only']

@task.short_circuit
def should_run_generate(**context):
    """Determine if file generation tasks should run based on mode parameter."""
    conf = context.get('dag_run').conf or {}
    mode = conf.get('mode', 'full')
    logger.info(f"Execution mode: {mode}")
    logger.info(f"should_run_generate: {mode in ['full', 'generate_only']}")
    return mode in ['full', 'generate_only']

@task.short_circuit
def should_run_ondemand(**context):
    """Determine if on-demand workflow should run based on mode parameter."""
    conf = context.get('dag_run').conf or {}
    mode = conf.get('mode', 'full')
    logger.info(f"Execution mode: {mode}")
    logger.info(f"should_run_ondemand: {mode in ['full', 'ondemand_only']}")
    return mode in ['full', 'ondemand_only']

'''

# Insert before "# =============================================================================="
# "# DAG Definition"
dag_def_marker = "# ==============================================================================\n# DAG Definition\n# =============================================================================="
content = content.replace(dag_def_marker, shortcircuit_code + dag_def_marker)

# 4. Replace DAG body with new flow
old_dag_body = '''with DAG(
    dag_id=DAG_ID,
    description=(
        "rts24 market events data processing - triggered by the completion of trading "
        "and order data processing, representing the availability of the consolidated "
        "market events data for the day"
    ),
    start_date=DAG_START_DATE,
    schedule=reduce(
        and_,
        [
            saturn_slc_ready_asset,
            segment_BLK_ready_asset,
            segment_EQU_ready_asset,
            segment_ETF_ready_asset,
            segment_FXI_ready_asset,
            segment_WAR_ready_asset,
        ],
    ),
    catchup=False,
    max_active_runs=DAG_MAX_ACTIVE_RUNS,
    tags=TAGS,
    doc_md=__doc__,
):
    trading_date = extract_trading_date()
    all_load_tasks, generation_tasks = create_all_flows(trading_date=trading_date)

    # Task 1: Query Athena for pending on-demand requests (deferrable - non-blocking)
    query_on_demand_table = AthenaOperator(
        task_id="query_on_demand_table",
        query=f"SELECT * FROM {ONDEMAND_REQUESTS_TABLE} WHERE run_flag = '{RUN_FLAG_PENDING}'",
        database=LAKEHOUSE_DATABASE,
        workgroup=ATHENA_WORKGROUP,
        # output_location=ATHENA_OUTPUT_LOCATION,
        deferrable=True,
        aws_conn_id=AWS_CONN_ID,
    )

    # Task 2: Process query results and build EMR job parameters
    process_on_demand_query_results_task = process_on_demand_query_results()

    # On-demand requests wait for all data loads to ensure data availability
    [*all_load_tasks] >> query_on_demand_table >> process_on_demand_query_results_task

    # Dynamic mapping creates one task per on-demand request for parallel execution
    generate_on_demand_files = EmrServerlessStartJobOperator.partial(
        task_id="generate_on_demand_files",
        map_index_template="{{ task.name }}",
        application_id="{{ var.value.get('DEV_LUNA_CASH_REGULATORY_REPORTING_EMR_APPLICATION_ID') }}",
        execution_role_arn="{{ var.value.get('DEV_LUNA_CASH_REGULATORY_REPORTING_EMR_ROLE') }}",
        deferrable=True,
        on_execute_callback=log_emr_job_start,
        config={"tags": EMR_CONFIG_TAGS},
        **EMR_RETRY_POLICY,
    ).expand_kwargs(process_on_demand_query_results_task)

    update_task = update_ondemand_requests_flag()
    verify_task = verify_update_status()

    process_on_demand_query_results_task >> generate_on_demand_files >> update_task >> verify_task'''

new_dag_body = '''with DAG(
    dag_id=DAG_ID,
    description=(
        "RTS24 Parameterized Pipeline (ShortCircuit Approach) - Supports multiple execution modes: "
        "full, loads_only, generate_only, ondemand_only"
    ),
    start_date=DAG_START_DATE,
    schedule=reduce(
        and_,
        [
            saturn_slc_ready_asset,
            segment_BLK_ready_asset,
            segment_EQU_ready_asset,
            segment_ETF_ready_asset,
            segment_FXI_ready_asset,
            segment_WAR_ready_asset,
        ],
    ),
    catchup=False,
    max_active_runs=DAG_MAX_ACTIVE_RUNS,
    tags=TAGS + ["parameterized", "shortcircuit"],
    doc_md=__doc__,
):
    # Always extract trading_date (needed for loads and generate modes)
    trading_date = extract_trading_date()

    # Create ShortCircuit gates for different execution paths
    check_loads = should_run_loads()
    check_generate = should_run_generate()
    check_ondemand = should_run_ondemand()

    # Create all tasks (they always exist in DAG structure)
    all_load_tasks, generation_tasks = create_all_flows(trading_date=trading_date)

    # On-demand workflow tasks
    query_on_demand_table = AthenaOperator(
        task_id="query_on_demand_table",
        query=f"SELECT * FROM {ONDEMAND_REQUESTS_TABLE} WHERE run_flag = '{RUN_FLAG_PENDING}'",
        database=LAKEHOUSE_DATABASE,
        workgroup=ATHENA_WORKGROUP,
        trigger_rule='none_failed',  # Run even if upstream is skipped
        deferrable=True,
        aws_conn_id=AWS_CONN_ID,
    )

    process_on_demand_query_results_task = process_on_demand_query_results()

    generate_on_demand_files = EmrServerlessStartJobOperator.partial(
        task_id="generate_on_demand_files",
        map_index_template="{{ task.name }}",
        application_id="{{ var.value.get('DEV_LUNA_CASH_REGULATORY_REPORTING_EMR_APPLICATION_ID') }}",
        execution_role_arn="{{ var.value.get('DEV_LUNA_CASH_REGULATORY_REPORTING_EMR_ROLE') }}",
        deferrable=True,
        on_execute_callback=log_emr_job_start,
        config={"tags": EMR_CONFIG_TAGS},
        **EMR_RETRY_POLICY,
    ).expand_kwargs(process_on_demand_query_results_task)

    update_task = update_ondemand_requests_flag()
    verify_task = verify_update_status()

    # Dependencies with ShortCircuit gates
    # Path 1: Loads (gated by check_loads)
    trading_date >> check_loads >> [*all_load_tasks]

    # Path 2: Generation (gated by check_generate, depends on loads)
    trading_date >> check_generate
    [*all_load_tasks] >> generation_tasks
    check_generate >> generation_tasks

    # Path 3: On-demand (gated by check_ondemand)
    check_ondemand >> query_on_demand_table >> process_on_demand_query_results_task
    process_on_demand_query_results_task >> generate_on_demand_files >> update_task >> verify_task'''

content = content.replace(old_dag_body, new_dag_body)

# Write the modified content
with open('dags/dagggbbb1.py', 'w') as f:
    f.write(content)

print("✅ dagggbbb1.py created successfully with ShortCircuit approach")
print("\nSupported parameters:")
print('  {"trading_date": "2026-05-14", "mode": "full"}  # Default: all tasks')
print('  {"trading_date": "2026-05-14", "mode": "loads_only"}  # Only load data')
print('  {"trading_date": "2026-05-14", "mode": "generate_only"}  # Only generate files')
print('  {"mode": "ondemand_only"}  # Only on-demand workflow')

from google.cloud import bigquery

def bq_config():
    """
    Configures BigQuery connection to connect to table.

    Arguments:
        - None

    Returns:
        - client: BigQuery client connection
        - project_id (string): project id
    
    """

    # ----- Table Information -----
    project_id = 'YOUR_PROJECT_NAME'
    dataset_id = 'DATASET_ID'
    table_name = 'TABLE_NAME'
    table_id = f'{project_id}.{dataset_id}.{table_name}'

    # ----- BigQuery Connection -----
    client = bigquery.Client(project = project_id)
    return client, project_id, dataset_id, table_name, table_id
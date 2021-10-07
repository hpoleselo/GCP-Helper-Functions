from utils.bigquery_config import bq_config
import ibis
import ibis_bigquery

_, project_id, dataset_id, table_name, table_id = bq_config()

# ----- IBIS BigQuery Connection ------
def ibis_config():
    conn = ibis_bigquery.connect(
        project_id=project_id,
        dataset_id=dataset_id)
    return conn

def table_query_with_filter():
    conn = ibis_config()
    model_catalog_table = conn.table(table_name)
    part_table = model_catalog_table['Row1', 'Row2']
    query_condition = (part_table.Row1 == "certain_value") & (part_table.Row2 == "certain_value2")
    filtered_query = part_table[query_condition]
    filtered_query_df = filtered_query.execute()
    filtered_query_as_json = filtered_query_df.to_json(orient='records')




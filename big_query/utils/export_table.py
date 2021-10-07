from utils.bigquery_config import bq_config
from google.cloud import bigquery

bq_client, project_id, dataset_id, table_name, table_id = bq_config()

def export_table_as_json():
    # GCS destination
    folder1 = "CONSTRUCT_YOUR_PATH"
    filename = "NAME_OF_FILE"
    gcs_bucket_name = "YOUR_BUCKET_NAME"
    json_output = f"{folder1}/{filename}.json"
    destination_uri = f"gs://{gcs_bucket_name}/{json_output}"

    # Configuring Job Config to export data as JSON
    job_config = bigquery.job.ExtractJobConfig()
    job_config.destination_format = bigquery.DestinationFormat.NEWLINE_DELIMITED_JSON

    # This extracts the whole table instead of a single row
    extract_job = bq_client.extract_table(
        table_id,
        destination_uri,
        job_config=job_config,
        # Location must match that of the source table, check that on your BQ instance.
        location="US"
    )
    extract_job.result()
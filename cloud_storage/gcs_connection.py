from google.cloud import storage

def gcs_config():
    gcs_client = storage.Client()
    bucket_name = 'YOUR_BUCKET_NAME'
    gcs_bucket = gcs_client.get_bucket(bucket_name) 
    
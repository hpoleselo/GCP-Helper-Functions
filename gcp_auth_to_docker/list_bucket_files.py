from google.cloud import storage

from os import environ

print(environ['GOOGLE_APPLICATION_CREDENTIALS'])


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    #storage_client = storage.Client.from_service_account_json(gcp_creds_file_path)

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)

list_blobs("BUCKET_NAME")

## Mounting GCP creds

```$ docker run --rm -e GOOGLE_APPLICATION_CREDENTIALS=credentials.json -v $env:GOOGLE_APPLICATION_CREDENTIALS:/credentials.json list_bucket_objects```

1. Setup GOOGLE_APPLICATION_CREDENTIALS environment variable:
https://cloud.google.com/docs/authentication/production#windows
https://cloud.google.com/run/docs/testing/local#docker-with-gcp-access
https://blog.dataminded.com/application-default-credentials-477879e31cb5
https://medium.com/google-cloud/use-google-cloud-user-credentials-when-testing-containers-locally-acb57cd4e4da
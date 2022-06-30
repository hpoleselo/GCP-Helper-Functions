FROM python:3.8-slim

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY ./list_bucket_files.py ./
CMD ["python". "list_bucket_files.py"]
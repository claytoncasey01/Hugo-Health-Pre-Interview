# Pull python image
FROM python:3.7-slim

WORKDIR /app

ADD . /app

ENTRYPOINT ["python3", "main.py"]
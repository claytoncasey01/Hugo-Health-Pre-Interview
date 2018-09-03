# Pull python image
FROM python:3.7-slim

ENV API_KEY 309c0f36-b920-41eb-a34e-37a0fecb5c62

WORKDIR /app

ADD . /app

ENTRYPOINT ["python3", "main.py"]
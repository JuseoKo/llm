FROM python:3.12-slim

COPY requirements.txt .

RUN pip install --no-cache-dir uv \
    && uv pip install --system --no-cache-dir -r requirements.txt
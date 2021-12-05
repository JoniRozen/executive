# syntax=docker/dockerfile:1
FROM python:3.10.0-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUn export PYTHONPATH=/app/executive
CMD [ "python3", "executive/main.py", "run", "--host=0.0.0.0"]
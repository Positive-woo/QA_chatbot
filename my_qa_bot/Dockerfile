FROM python:3.10.12-slim

WORKDIR /code

# linux setting
RUN apt-get update && apt-get install -y

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Local venv folder
ENV PIPENV_VENV_IN_PROJECT=1

# Disabling cache to reduce image size
ENV PIP_NO_CACHE_DIR=false

# install virtual environment
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
COPY ./fastapi/. .
RUN pip install --upgrade pip && pip install pipenv && pipenv install

CMD ["pipenv", "run", "python", "main.py"]
FROM python:3.10-slim

WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY docker_config.py default_config.py

CMD ["python", "app.py"]
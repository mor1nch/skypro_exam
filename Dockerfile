FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
COPY docker_config.py config.py

CMD ["python", "app.py"]
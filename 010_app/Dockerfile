# Dockerfile
FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app3.py /code/app3.py

CMD ["fastapi", "run", "app3.py", "--port", "80"]
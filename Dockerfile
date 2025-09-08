FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod 777 entrypoint.sh

EXPOSE 8000

CMD["./entrypoint.sh"]

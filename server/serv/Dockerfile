FROM python:slim

Workdir /app

COPY requirements.txt .

RUN python3 -m venv .venv
RUN .venv/bin/pip3 install -r requirements.txt

COPY server.env .env

COPY server.py .

CMD [".venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "server:app"]

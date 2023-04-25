FROM python:slim

WORKDIR /app

COPY requirements.txt . 

RUN python3 -m venv .venv 
RUN .venv/bin/pip install -r requirements.txt

COPY collector.env .env

COPY collector.py .

CMD [".venv/bin/python", "collector.py"]
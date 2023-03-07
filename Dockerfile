FROM python:3.10

RUN apt-get update && apt-get install -y firefox-esr

COPY . /netcord
WORKDIR /netcord

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

ENV HOST="0.0.0.0" 
ENV PORT=5000

EXPOSE $PORT

CMD ["python3.10", "netcord.py"]

FROM python:3.10-alpine

RUN apk add --no-cache build-base

COPY . /netcord
WORKDIR /netcord

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

ENV HOST="0.0.0.0" 
ENV PORT=5000

EXPOSE $PORT

CMD ["python3.9", "netcord.py"]

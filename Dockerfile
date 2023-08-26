FROM python:3.11

RUN useradd --create-home netcord_user

RUN apt-get update && apt-get install -y apt-utils firefox-esr iputils-ping traceroute dnsutils net-tools

ENV PATH="/home/netcord_user/.local/bin:${PATH}"

COPY . /netcord
WORKDIR /netcord

RUN chown -R netcord_user:netcord_user /netcord
USER netcord_user

RUN pip install --upgrade pip setuptools --user && \
    pip install -r requirements.txt --user

ENV HOST="0.0.0.0" 
ENV PORT=5000

EXPOSE $PORT

CMD ["python3.11", "netcord.py"]

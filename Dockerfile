FROM python:3.9

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /opt/working
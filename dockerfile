FROM python:3.8

WORKDIR /words-in-songs

COPY . .

RUN pip install -r requirements.txt

RUN sleep 1d

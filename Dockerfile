FROM python:3.11

COPY ./requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt



COPY ./src /src
COPY ./tests /tests



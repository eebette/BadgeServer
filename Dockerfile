FROM python:latest

COPY badge_server.py /
COPY requirements.txt /

RUN apt update && apt install -y build-essential python-dev-is-python3

RUN pip3 install -r /requirements.txt

RUN pip3 install uwsgi

CMD ["uwsgi", \
     "--http-socket", "0.0.0.0:3031", \
     "--wsgi-file", "/badge_server.py", \
     "--callable", "app", \
     "--processes", "4", \
     "--threads", "2", \
     "--stats", "0.0.0.0:9191"]
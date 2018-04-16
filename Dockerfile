FROM python:3.6

WORKDIR /app

ADD . /app

VOLUME ["/app"]

CMD ["python", "visqgen.py"]

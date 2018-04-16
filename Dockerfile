FROM python:3.6

RUN pip install csv

WORKDIR /app

ADD . /app

VOLUME ["/app"]

CMD ["python", "visqgen.py"]

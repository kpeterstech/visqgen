FROM python:3.6

WORKDIR /app

COPY visqgen.py /usr/local/bin/visqgen.py

CMD ["python", "/usr/local/bin/visqgen.py"]

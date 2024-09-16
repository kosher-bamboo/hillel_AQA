FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install psycopg2

CMD ["pytest"]

RUN pip install psycopg2
RUN pip install pytest

CMD ["pytest", "-vv", "db_docker_file.py"]

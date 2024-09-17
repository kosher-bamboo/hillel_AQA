FROM python:3.9-bullseye

# Install OpenJDK
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

# Install allure
RUN apt-get update && apt-get install -y unzip
# RUN wget -qO- https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.zip -O allure.zip \
RUN wget -qO- https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.5/allure-commandline-2.13.5.zip -O allure.zip \
    && unzip allure.zip -d /opt/ \
#     && ln -s /opt/allure-2.14.0/bin/allure /usr/bin/allure
    && ln -s /opt/allure-2.13.5/bin/allure /usr/bin/allure

# Set environment variable to ensure allure is in $PATH
# ENV PATH="/opt/allure-2.14.0/bin:$PATH"
ENV PATH="/opt/allure-2.13.5/bin:$PATH"

# Other commands for setting up your container
COPY . /app
WORKDIR /app


RUN pip install psycopg2
RUN pip install pytest
RUN pip install allure-pytest

CMD pytest -vv db_docker_file.py
#--alluredir=allure-results && allure generate --clean

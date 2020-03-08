# The Dockerfile defines the image's environment
# Import Python runtime and set up working directory
FROM python:3.7-slim

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install any necessary dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -U pip \
   && pip install --no-cache-dir -r /tmp/requirements.txt

RUN apt-get update -y && apt-get install libgtk2.0-dev curl vim -y

WORKDIR /app

COPY bin /app/bin
COPY image_diff /app/image_diff

WORKDIR /cwd

ENTRYPOINT ["/app/bin/image_diff"]
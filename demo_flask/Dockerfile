FROM alpine

ARG BUILD_DATE
ARG BUILD_VERSION

LABEL org.opencontainers.image.authors="clemenko@docker.com" \
      org.opencontainers.image.source="https://github.com/clemenko/dockerfiles/tree/master/demo_flask" \
      org.opencontainers.image.created=$BUILD_DATE \
      org.opencontainers.image.title="clemenko/flask_demo" \
      org.opencontainers.image.description="The repository contains a simple flask application " \
      org.opencontainers.image.source=$BUILD_VERSION

RUN apk -U upgrade && apk add --no-cache python3 curl  &&\
    pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir flask redis pymongo &&\
    rm -rf /var/cache/apk/*
    
WORKDIR /code
ADD . /code
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python", "app.py"]

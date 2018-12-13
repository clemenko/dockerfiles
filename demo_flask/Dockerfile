FROM alpine

ARG BUILD_DATE
ARG VCS_REF
ARG BUILD_VERSION
ARG JAR_FILE

# Labels.
LABEL maintainer="clemenko@docker.com" \
      org.label-schema.vcs-url="https://github.com/clemenko/dockerfiles/tree/master/demo_flask" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="clemenko/flask_demo" \
      org.label-schema.description="The repository contains a simple flask application " \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$BUILD_VERSION

RUN apk -U upgrade && apk add --no-cache curl py-pip  &&\
    pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir flask redis pymongo &&\
    rm -rf /var/cache/apk/*
    
WORKDIR /code
ADD . /code
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python", "app.py"]

FROM alpine:3.18.3
RUN apk -U upgrade && apk add --no-cache py3-pip curl  &&\
    pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir flask redis &&\
    rm -rf /var/cache/apk/*

WORKDIR /code
ADD . /code
EXPOSE 5000

CMD ["python3", "app.py"]

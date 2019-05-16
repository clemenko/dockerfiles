FROM alpine
RUN apk -U upgrade && apk add --no-cache python3 curl  &&\
    pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir flask redis pymongo &&\
    rm -rf /var/cache/apk/*

WORKDIR /code
ADD . /code
EXPOSE 5000

CMD ["python3", "app.py"]

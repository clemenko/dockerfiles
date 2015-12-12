FROM alpine
RUN apk update && apk add python &&\
    apk add py-pip &&\
    pip install --upgrade pip &&\
    pip install flask &&\
    pip install redis &&\
    rm -rf /var/cache/apk/*
WORKDIR /code
ADD . /code
EXPOSE 5000
CMD ["python", "app.py"]

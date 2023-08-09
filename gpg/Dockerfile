FROM alpine:3.18.3

LABEL org.opencontainers.image.authors="clemenko@gmail.com" \
      org.opencontainers.image.source="https://github.com/clemenko/dockerfiles/tree/master/gpg" \
      org.opencontainers.image.title="clemenko/gpg" 

WORKDIR /code

RUN apk -U upgrade && apk add gnupg && \
    echo " Some Secret Awesome Phrase that needs to be protected. " | gpg -c --passphrase Pa22word --batch --yes > secret.gpg 

ADD init.sh /code

CMD ["/code/init.sh"]

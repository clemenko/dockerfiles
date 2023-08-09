FROM alpine:3.18.3

ENV VERSION=6.18.1

RUN apk -U add msr-tools --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
    apk -U upgrade && apk add gcompat && \
    cd /opt && wget https://github.com/xmrig/xmrig/releases/download/v$VERSION/xmrig-$VERSION-linux-static-x64.tar.gz && \
    tar -zxvf xmrig-$VERSION-linux-static-x64.tar.gz && \
    rm -rf /var/cache/apk/* /opt/xmrig-$VERSION-linux-static-x64.tar.gz

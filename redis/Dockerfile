FROM alpine
RUN apk update && apk add redis &&\
    sed -i 's/daemonize yes/daemonize no/g' /etc/redis.conf &&\
    sed -i 's/# bind 0.0.0.0/bind 0.0.0.0/g' /etc/redis.conf &&\
    rm -rf /var/cache/apk/*
ENTRYPOINT ["/usr/bin/redis-server","/etc/redis.conf"]
EXPOSE 6379


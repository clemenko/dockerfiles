FROM golang:1.8-alpine
WORKDIR /go/src/
#RUN go get -d -v golang.org/x/net/html
COPY gen_token.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o gen_token .

FROM alpine:latest
MAINTAINER clemenko@docker.com
LABEL RUN="docker run --rm -it -v ${PATH_TO_LIC_AND_OUTPUT_DIR}:/data/ clemenko/docker_scanning_database"
WORKDIR /
RUN apk -U upgrade && apk add --no-cache jq curl
COPY --from=0 /go/src/gen_token .
COPY gen_token.sh .
CMD /gen_token.sh

FROM alpine
RUN apk update &&\
    apk add --update git &&\
    apk add --update nginx &&\
    git clone https://github.com/hakimel/reveal.js.git /revealjs &&\
    rm -rf /var/cache/apk/*

WORKDIR /revealjs
ADD revealjs/index.html /revealjs/
ADD revealjs/custom.css /revealjs/css/
ADD revealjs/title.js /revealjs/plugin/
ADD revealjs/slides.md /revealjs/md/
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/default.conf /etc/nginx/conf.d/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

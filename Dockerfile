
FROM nginx:alpine

EXPOSE 8080

COPY  nginx.conf  /etc/nginx/

WORKDIR /www/data

COPY  index.html  /www/data/

WORKDIR /tmp/logs/

ENV  port=8080

RUN mkdir -p /www/data/

RUN echo "Hello World to tzipi" > /www/data/index.html

VOLUME [ "/www/data/" ]






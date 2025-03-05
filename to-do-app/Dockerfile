FROM node:12.18.2 AS build

WORKDIR /app

COPY ./package.json /app/package.json

RUN npm install
COPY . .
RUN npm build

FROM nginx:latest

COPY . /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:stable

ARG APP_CONTAINER_NAME=app

COPY ./deploy/nginx/conf.d/ /etc/nginx/conf.d/
RUN sed -i "s/fastcgi_pass app:8000.*/fastcgi_pass $APP_CONTAINER_NAME:8000;/" /etc/nginx/conf.d/default.conf

EXPOSE 80

WORKDIR /etc/nginx

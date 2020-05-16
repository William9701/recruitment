# Build based on the already built base,
# Build ihopeit/django-recruitment-base:0.8 image using Dockerfile-base in advance
# Or pull version 0.8 base image from docker.io, this image contains complete python/django packages
FROM ihopeit/django-recruitment-base:0.8
WORKDIR /data/recruitment
ENV server_params=
COPY . .
EXPOSE 8000
CMD ["/bin/sh", "/data/recruitment/start.production.bat"]
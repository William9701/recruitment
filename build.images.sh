docker build -f Dockerfile-base -t ihopeit/django-recruitment-base:0.8 .

 ## or just docker pull already built image from docker hub:
 # docker pull ihopeit/django-recruitment-base:0.8

## Build version 0.9 image including local.py file (based on 0.8 image):
docker build -f Dockerfile -t ihopeit/django-recruitment:0.9 .

docker tag ihopeit/django-recruitment:0.9 registry.cn-beijing.aliyuncs.com/ihopeit/django-recruitment:0.9
docker push registry.cn-beijing.aliyuncs.com/ihopeit/django-recruitment:0.9


## k8s deployment
## Before deployment, replace {{BUILD_NUMBER}} in k8s/xxx-deployment.yaml with version number
## Then run apply
## kubectl apply -f k8s
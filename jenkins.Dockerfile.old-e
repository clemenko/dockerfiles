from jenkins:alpine
MAINTAINER clemenko@docker.com
LABEL RUN="docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v /jenkins/:/var/jenkins_home -v /jenkins/.ssh:/root/.ssh/ -p 8080:8080 --name jenkins superjenkins"
USER root
RUN apk -U --no-cache add docker

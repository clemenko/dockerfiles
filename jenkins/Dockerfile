# stage 1
FROM alpine as build
RUN apk -U add docker

# stage 2
FROM jenkins/jenkins:lts-alpine

ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false ${JAVA_OPTS:-}"
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/casc/

LABEL org.opencontainers.image.authors="clemenko@gmail.com" \
      org.opencontainers.image.source="https://github.com/clemenko/dockerfiles/tree/master/jenkins" \
      org.opencontainers.image.title="clemenko/jenkins" \
      org.opencontainers.image.description="The repository contains a simple jenkins application " \
      org.opencontainers.docker.cmd="docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v /jenkins/:/var/jenkins_home -v /jenkins/.ssh:/root/.ssh/ -p 8080:8080 -p 50000:50000 --name jenkins clemenko/jenkins" \
      org.opencontainers.stack="dmVyc2lvbjogIjMuNCIKc2VydmljZXM6CiAgYXBwOgogICAgaW1hZ2U6IGNsZW1lbmtvL2ZsYXNrX2RlbW8KICAgIGRlcGxveToKICAgICAgcmVwbGljYXM6IDQKICAgICAgdXBkYXRlX2NvbmZpZzoKICAgICAgICBwYXJhbGxlbGlzbTogMgogICAgICBsYWJlbHM6CiAgICAgICAgICBjb20uZG9ja2VyLmxiLm5ldHdvcms6IGZsYXNrX2t2CiAgICAgICAgICBjb20uZG9ja2VyLmxiLmhvc3RzOiBhcHAuZG9ja3IubGlmZQogICAgICAgICAgY29tLmRvY2tlci5sYi5wb3J0OiA1MDAwCiAgICBwb3J0czoKICAgICAgLSA1MDAwOjUwMDAKICAgIG5ldHdvcmtzOgogICAgICBkYjoKICAgICAga3Y6CgogIG1vbmdvOgogICAgaW1hZ2U6IG1vbmdvCiAgICBuZXR3b3JrczoKICAgICAgZGI6CgogIHJlZGlzOgogICAgaW1hZ2U6IHJlZGlzOmFscGluZQogICAgbmV0d29ya3M6CiAgICAgIGt2OgoKbmV0d29ya3M6CiAga3Y6CiAgZGI6Cg=="

USER root
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY jenkins.yaml /usr/share/jenkins/casc/
COPY --from=build /usr/bin/docker /usr/bin/

ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false ${JAVA_OPTS:-}"
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/casc/

RUN apk -U update; apk add libltdl git jq && \
    apk --purge del apk-tools && \
    /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt && \
    rm -rf /var/cache/apk/*


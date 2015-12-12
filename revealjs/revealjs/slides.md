# Rancher - Not just for cattle anymore!

---

## Who : Andy Clemenko
 - Geek/Devops/System Admin
 - Twitter : <a href="http://twitter.com/aclemenko" target=new>@aclemenko</a>
 - Github : <a href="https://github.com/clemenko" target=new>clemenko</a>
 - Homepage : <a href="http://andyc.info" target=new>andyc.info</a>
 - Email : <a href="mailto:clemenko@gmail.com" target=new>clemenko@gmail.com</a>

---

## This talk is :
 1. Background
 2. Demos

---

## Docker Adoption Problems :
 1. Applications built for containers
 2. Container orchestration
 3. Network space consistency

  Rancher Solves #2, #3!

---

## What is Rancher?
## "Simple, elegant tools for managing Docker in production"
 - gui/api for running docker at scale.
 - Docker Orchestration
 - IPSEC network overlay
 - Service level orchestration.

---

## Deploy Rancher :
 - Use any OS that supports Docker
 - Prefer RancherOS/CoreOS/Atomic
 - Single command server deployment.
   <pre> docker run -d -p 8080:8080 --restart=always --name rancher-server
rancher/server </pre>
 - Single command agent deployent <-- curled form api.
   <pre> docker run -d --privileged -v /var/run/docker.sock:/var/run/docker.sock
 rancher/agent:v0.7.8 http://10.0.133.60:8080/v1/scripts/78E2DDB0896470936E8D:
1432900800000:pFBCrKoYdkuoVkFiAU5Tka0nP5I </pre>

---

## Demo :
 - CoreOS - Google Compute Engine
 - <a href=":8080/static/infrastructure/hosts" target=new>demo</a>
 - $500 credit for GCE (https://cloud.google.com/compute/) use code "docker2015"
---

##Future of Rancher
 - Self scaling services.
 - LDAP authentication.
 - Storage overlay.
 - Self contained deployments.

---

## Learn more
 - Rancher : <a href="http://rancher.com/rancher-io/" target=new>rancher.com/rancher-io</a>
 - RancherOS : <a href="http://rancher.com/rancher-os/" target=new>rancher.com/rancher-os</a>
 - Youtube : <a href="https://www.youtube.com/channel/UCh5Xtp82q8wjijP8npkVTBA" target=new>Rancher Labs Channel</a>
 - Presentation : <a href="https://github.com/clemenko/rancher_presentation" target=new>github.com/clemenko/rancher_presentation</a>

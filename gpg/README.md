# Simple Demo of GPG

This is a simple demo for using an encrypted file within an image. The idea is that you have to pass in a environment variable. This could be very easily modified to use Docker Secrets, Docker Configs, or even TPM. 

## USE

The demo password is `Pa22word`. 

Without Password

```bash
$ docker run --rm -it clemenko/gpg 
 -- Warning -- Please pass in an environemnt variable named "password" with a "-e password=".  
```

With Password

```bash
$ docker run --rm -it -e password=Pa22word clemenko/gpg
 -- Secret --  Some Secret Awesome Phrase that needs to be protected. 
```
#!/bin/sh
RED="\e[31m"
GREEN="\e[32m"
NORMAL="\e[39m"

if [ -z "$password" ]; then 
  echo -e $RED "-- Warning -- Please pass in an environemnt variable named \"password\" with a \"-e password=\". " $NORMAL
  exit
fi

gpg --passphrase $password --batch --yes -o secret -d secret.gpg  > /dev/null 2>&1
secret=$(cat secret)
echo -n -e $GREEN "-- Secret -- $secret $NORMAL"
echo ""
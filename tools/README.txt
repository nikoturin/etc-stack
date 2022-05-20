paramsChange.sh was created to make a changes to IP address into files necesary to execute process NEAR.

Those are the files:
dockerFile="../docker-compose.yaml"
aliasCmd="../bc/near/sc/alias-lnear.sh"
keyPathStack="../bc/near/sc/neartosis/"
pathGtw="../gtw/nginx.conf"

There is a bug script to executing changes to nginx.conf, I mean when the process is executed there are some spaces added to URL, will be necessary to delete the space.

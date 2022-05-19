#!/bin/bash

#####
# Make a IP change into files yaml, alias and nginx
# Copy key into neartosis directory
#####
declare -a arrVar
arrVar=()
nearEnv="NEAR.txt"
dockerFile="../docker-compose.yaml"
aliasCmd="../bc/near/sc/alias-lnear.sh"
keyPathStack="../bc/near/sc/neartosis/"
pathGtw="../gtw/nginx.conf"

ip=$(ifconfig  enp0s8 | grep netmask|sed -n 's/^ *//p'|cut -d " " -f2)

for i in $(grep export $nearEnv  | tr " " "\n" | grep NEAR)
do
	addLine=$(echo $i| sed -n 's/\/\//\\\/\\\//p'|tr "=" ":"|sed -n "s/127.0.0.1/$ip/p")
	arrVar+=($addLine)
done
for value in "${arrVar[@]}"
do
	cont=$((cont +1))
	
	#docker-compose.yaml
	envVar=$(echo $value|cut -d ":" -f1)
	oldStr=$(grep $envVar $dockerFile|sed -n 's/\/\//\\\/\\\//p'| sed -n 's/^ *//p')
	newStr=$(echo $value | sed -n 's/:/: /p')
	echo "NEAR.TXT:"$value

	#local_near alias
	lnOldStr=$(grep $envVar $aliasCmd|sed -n 's/\\//p' | sed -n 's/^ *//p'| sed -n 's/\/\//\\\/\\\//p')
	lnNewStr=$(echo $value|sed -n "s/$envVar:/$envVar=/p")

	#nginx         
	prefix=$(echo "$envVar" | tr [[:upper:]] [[:lower:]] |cut -d "_" -f2)         
	oldProxy=$(grep -A2 $prefix $pathGtw  | grep proxy_pass | sed -n 's/^ *//p' | tr ";" " " | cut -d " " -f3 |cut -d "/" -f3)         
	newProxy=$(echo $value| cut -d "/" -f3|tr '"' " ")         

	sed -i "s/$oldProxy/$newProxy/g" $pathGtw
	sed -i "s/$oldStr/$newStr/g" $dockerFile
	sed -i "s/$lnOldStr/$lnNewStr /g" $aliasCmd
	
done

keyPath=$(grep export NEAR.txt | grep "NEAR_CLI_LOCALNET_KEY_PATH" | cut -d "=" -f2| tr '"' " " | sed -n 's/^ *//p')
yes | cp -rvfp $keyPath $keyPathStack

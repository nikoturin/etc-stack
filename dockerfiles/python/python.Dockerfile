#FROM ubuntu:18.04
FROM node:10.17.0-jessie

RUN apt-get update \
	&& npm install -g near-cli\
	&& alias local_near='NEAR_ENV="local" NEAR_CLI_LOCALNET_NETWORK_ID="localnet"\
		 	     NEAR_NODE_URL="http://192.168.56.105:49178"\ 
			     NEAR_CLI_LOCALNET_KEY_PATH="/var/src/near/neartosis/validator-key.json" \
			     NEAR_WALLET_URL="http://192.168.56.105:49182" \
			     NEAR_HELPER_URL="http://192.168.56.105:49179" \
			     NEAR_HELPER_ACCOUNT="test.near" \
                             NEAR_EXPLORER_URL="http://192.168.56.105:49181" near'

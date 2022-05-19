#!/bin/bash

alias local_near='NEAR_ENV="local" \
		  NEAR_CLI_LOCALNET_NETWORK_ID="localnet" \
NEAR_NODE_URL="http://192.168.56.105:49186" \
		  NEAR_CLI_LOCALNET_KEY_PATH="/var/src/near/neartosis/validator-key.json" \
NEAR_WALLET_URL="http://192.168.56.105:49190" \
NEAR_HELPER_URL="http://192.168.56.105:49187" \
		  NEAR_HELPER_ACCOUNT="test.near" \
NEAR_EXPLORER_URL="http://192.168.56.105:49189" \
		  near'

#local_near view $NEAR_HELPER_ACCOUNT get_num --accountId $NEAR_HELPER_ACCOUNT

import asyncio
import os
from hfc.fabric import Client

loop = asyncio.get_event_loop()
#loop = asyncio.new_event_loop()

cli = Client(net_profile='network.json')
org1_admin = cli.get_user('org1.example.com', 'Admin')

# Make the client know there is a channel in the network
cli.new_channel('mychannel')

# Install Example Chaincode to Peers
# GOPATH setting is only needed to use the example chaincode inside sdk

#gopath_bak = os.environ.get('GOPATH', '')
#gopath = os.path.normpath(os.path.join(
#                      os.path.dirname(os.path.realpath('__file__'))
#                     ))
#os.environ['GOPATH'] = os.path.abspath(gopath)

# Query a chaincode
args = [""]
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               cc_name='basic',
               fcn='GetAllAssets'
               ))

print(response)

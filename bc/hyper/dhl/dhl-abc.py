import asyncio
import os
from hfc.fabric import Client

#get_event_loop() deprecated to python3.10
loop = asyncio.get_event_loop()
#loop = asyncio.new_event_loop()

cli = Client(net_profile='network.json')
org1_admin = cli.get_user('org1.example.com', 'Admin')

# Make the client know there is a channel in the network
cli.new_channel('mychannel')

# Install Example Chaincode to Peers
# GOPATH setting is only needed to use the example chaincode inside sdk

gopath_bak = os.environ.get('GOPATH', '')
gopath = os.path.normpath(os.path.join(
                      os.path.dirname(os.path.realpath('__file__'))
                     ))
os.environ['GOPATH'] = os.path.abspath(gopath)


#policy = {     'identities': [         
#                {'role': {'name': 'member', 'mspId': 'Org1MSP'}},     
#                {'role': {'name': 'admin', 'mspId': 'Org1MSP'}}
#                ],     
#                'policy': {         
#                    '1-of': [             
#                            {'signed-by': 0},{'signed-by':1}
#                        ]     
#                    }
#                }

#args = [""]

#response = loop.run_until_complete(cli.chaincode_instantiate(                
#                requestor=org1_admin,                
#                channel_name='mychannel',                
#                peers=['peer0.org1.example.com'],                
#                args=args,                
#                cc_name='basic',                
#                cc_version='v1.0',                
#                cc_endorsement_policy=policy, # optional, but recommended                
#                collections_config=None, # optional, for private data policy                
#                transient_map=None, # optional, for private data                
#                wait_for_event=True # optional, for being sure chaincode is instantiated                
#                ))

args = ["asset7","brown","100","OPER2","2000","2308202202021306340000089494OPER2-22939979010005001050000092546022B20160221200634"] # The response should be true if succeed 

response = loop.run_until_complete(cli.chaincode_invoke(                
        requestor=org1_admin,                
        channel_name='mychannel',                
        peers=['peer0.org1.example.com','peer0.org2.example.com'],                
        args=args,                
        cc_name='basic',
        fcn='CreateAsset',
        transient_map=None, # optional, for private data                
        wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event                
        #cc_pattern='^invoked*' # if you want to wait for chaincode event and you have a `stub.SetEvent("invoked", value)` in your chaincode                
       ))
print(response)

# Query a chaincode
#args = ["asset5"]
# The response should be true if succeed
#response = loop.run_until_complete(cli.chaincode_query(
#               requestor=org1_admin,
#               channel_name='mychannel',
#               peers=['peer0.org1.example.com'],
#               args=args,
#               cc_name='basic',
#               fcn='ReadAsset'
#               ))

#print(response)

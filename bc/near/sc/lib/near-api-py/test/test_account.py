import near_api
import json

from config import NODE_URL



    # Signer private Local Private Key
    # Master user I mean, test.near
def setUp():
    provider = near_api.providers.JsonProvider(NODE_URL)
    signer = near_api.signer.Signer(
        "test.near",
        near_api.signer.KeyPair(
            "ed25519:5diEZPadQcTT4ogCrrEpptStwoesyh8bBtjoV9kiBuz187436n5WqtzuNkFAHuQFL5MrTSk2M9GCPpceqtt12ZPL"
        ))
    master_account = near_api.account.Account(provider,
                                                   signer,
                                                   "test.near")

    #owner smartContract ...
    #It's the way to read data from smartContracts NEAR
    result=provider.view_call("msg.test.near","get_status",json.dumps({"account_id": "test.near"}).encode('utf8'))
    result["result"] = json.loads(''.join([chr(x) for x in result["result"]]))
    print(result)
        
    #up to now it's the way to call rpc functions from smartContracts NEAR, will be necesary to deep more into lib 
    trans=master_account.function_call("msg.test.near","set_status",{"message": "one more time ..."})
    print(trans)

setUp()

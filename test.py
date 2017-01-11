import requests
import json
import pudb
import base64

BASE_URL = "https://61479249b3384ea5af19213bc3189b9b-vp0.us.blockchain.ibm.com:5001"

# get current chain height
chain_url = BASE_URL + "/chain"
chain_height = json.loads(requests.get(chain_url).text)['height']

for i in range(chain_height - 1, 0, -1):
    block_url = BASE_URL + '/chain/blocks/' + str(i)
    block = json.loads(requests.get(block_url).text)
    try:
        payload = block['transactions'][0]['payload']
    except:
        print("brick on " + str(i))

    decoded_payload = base64.b64decode(payload)

    for el in str(decoded_payload).split('\\n'):
        if 'user_type1_0' in el:
            print(str(decoded_payload).split('\\n'))


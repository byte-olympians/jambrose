'''
{
  "jsonrpc": "2.0",
  "method": "invoke",
  "params": {
    "type": 1,
    "chaincodeID": {
      "name": "5d613bc88ea0f98828e3a25b4844fb399d6d75258fa5f7558a0e2d782d842694688626a6548e42093175abc2ac9bf247d66e3acbba0e6646e7c36d1fa7e3f124"
    },
    "ctorMsg": {
      "function": "write",
      "args": [
        "user_type1_0 wallet", "obligation to user_type1_2"
      ]
    },
    "secureContext": "user_type1_2"
  },
  "id": 3
}
'''
import requests

URL = "https://61479249b3384ea5af19213bc3189b9b-vp0.us.blockchain.ibm.com:5001/chaincode"

def make_json(func, user1, user2=None):
    if func == 'write':
        _json = { "jsonrpc": "2.0",
                  "method": "invoke",
                  "params": {
                    "type": 1,
                    "chaincodeID": {
                      "name": "5d613bc88ea0f98828e3a25b4844fb399d6d75258fa5f7558a0e2d782d842694688626a6548e42093175abc2ac9bf247d66e3acbba0e6646e7c36d1fa7e3f124"
                    },
                    "ctorMsg": {
                      "function": func,
                      "args": [
                        user1, user2
                      ]
                    },
                    "secureContext": "user_type1_2"
                  },
                  "id": 3
                }
    else:
        _json = {"jsonrpc": "2.0",
          "method": "query",
          "params": {
            "type": 1,
            "chaincodeID": {
              "name": "5d613bc88ea0f98828e3a25b4844fb399d6d75258fa5f7558a0e2d782d842694688626a6548e42093175abc2ac9bf247d66e3acbba0e6646e7c36d1fa7e3f124"
            },
            "ctorMsg": {
              "function": func,
              "args": [
                user1
              ]
            },
            "secureContext": "user_type1_2"
          },
          "id": 2
        }
    return _json

def call_write(func, user1, user2):
    
    data = make_json(func, user1, user2)
    resp = requests.post(URL, json=data)
    return resp

def call_read(func, user1):
    data = make_json(func, user1)
    return requests.post(URL, json=data)

def call(func, user1, user2=None):
    if func == 'write':
        resp = call_write(func, user1, user2)
    else:
        resp = call_read(func, user1)

    return resp


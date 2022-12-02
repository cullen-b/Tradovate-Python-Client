#Gets list of all filled orders

import requests 
from GetAccessToken import getAccessToken
from config import *


def getFills(live, token):
    """Gets a list of fills from your account on that day

    Args:
        live (bool): True = live, False = demo
        token (String): your access token
    """

    if live:
        url = "https://live.tradovateapi.com/v1/fill/list"
    else:
        url = "https://demo.tradovateapi.com/v1/fill/list"

    header = {
        'Authorization': f'Bearer ${token}'
        }

    res = requests.get(url, headers=header)
    print(res)
    print(res.text)


#token = getAccessToken(False)[0]
#getFills(False, token)


#Example format
# most recent trade is last in list
"""
[
{"id":4914944371,
"orderId":4914944368,
"contractId":2794446,
"timestamp":"2022-10-25T19:31:02.965Z",
"tradeDate":{"year":2022,
"month":10,"day":25},
"action":"Buy",
"qty":1,
"price":3871.25,
"active":true,
"finallyPaired":0,
"external":false},

{"id":4914944436,
"orderId":4914944380,
"contractId":2794446,
"timestamp":"2022-10-25T19:48:47.359Z",
"tradeDate":{"year":2022,"month":10,"day":25},
"action":"Sell",
"qty":1,
"price":3872.0,
"active":true,
"finallyPaired":0,
"external":false},

{"id":4914944450,
"orderId":4914944447,
"contractId":2794446,
"timestamp":"2022-10-25T20:34:19.589Z",
"tradeDate":{"year":2022,"month":10,"day":25},
"action":"Buy",
"qty":1,
"price":3850.0,
"active":true,
"finallyPaired":0,
"external":false}
]
"""
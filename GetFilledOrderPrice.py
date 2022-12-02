#Gets Fill from order ID

import requests
from GetAccessToken import getAccessToken


def getFilledOrderPrice(live, orderID, token):
    """Gets price an order was filled at

    Args:
        live (bool): True for live, False for demo
        orderID (int): id of order you want price of
        token (string): your access token 

    Returns:
        float: price order was filled at
        0: if order has not been filled
    """
    
    if live:
        url = "https://live.tradovateapi.com/v1/fill/deps"
    else:
        url = "https://demo.tradovateapi.com/v1/fill/deps"

    header = {
        'Authorization': f'Bearer ${token}'
        }

    params = {
        "masterid": orderID
    }

    res = requests.get(url, headers=header, params=params)

    try:
        content = res.json()
        price = content[0]["price"]
        return price
    except:
        return 0

    

#token = getAccessToken(False)
#print(getFilledOrderPrice(False, 4890355687))
#Response Format
"""
Example:

[{"id":4890355029,
"orderId":4890355026,
"contractId":2794446,
"timestamp":"2022-10-20T22:17:41.350Z",
"tradeDate":{"year":2022,"month":10,"day":21},
"action":"Buy",
"qty":1,
"price":3671.25,
"active":true,
"finallyPaired":0,
"external":false}]

"""
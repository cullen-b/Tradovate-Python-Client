#Place TV market order
import requests
import time
from GetAccessToken import getAccessToken
from config import *


# Be careful!
# buysell must be either "Sell" or "Buy"
def placeMarketOrder(live, Qty, buysell, token):
    """Places market order with quantity "Qty" and in direction "buysell" at the market price

    Args:
        live (bool): True = live, False = demo
        Qty (int): Quantity of contracts you want to buy
        buysell (string): "Buy" or "Sell
        token (string): User's access token

    Returns:
        int: orderId of order you just placed
    """

    header = {
        'Authorization': f'Bearer ${token}', 
        'Accept': 'application/json'
            }

    if live:
        url = "https://live.tradovateapi.com/v1/order/placeorder"
        accId = LIVE_ACCOUNT_ID
    else:
        url = "https://demo.tradovateapi.com/v1/order/placeorder"
        accId = DEMO_ACCOUNT_ID

    order = {"accountSpec": USER_NAME,
            "accountId": accId,
            "action": buysell,
            "symbol": SYMBOL,
            "orderQty": Qty,
            "orderType": "Market",
            "isAutomated": "true"
            }

    # Make request
    res = requests.post(url, headers=header, data=order)
    
    if res.status_code != 200:
        print("Order Failed")
        print(res.status_code)
        print(res.reason)
        print(res.text)

    content = res.json()
    orderId = content["orderId"]
    print("Market Order Placed!\nId: " + str(orderId))
    return orderId


#token = getAccessToken(False)[0]
#placeMarketOrder(False, 1, "Buy", token)
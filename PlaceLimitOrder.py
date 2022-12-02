#Place TV limit order
import requests
from GetAccessToken import getAccessToken
from config import *
import time


# Be careful with this one! It will submit an order!
# buysell must be either "Sell" or "Buy"
def placeLimitOrder(live, Qty, buysell, orderPrice, token):
    """Places limit order with quantity "Qty" in direction "buysell" at price "orderPrice"

    Args:
        live (bool): True = live, False = demo
        Qty (int): Quantity of contracts you want to buy
        buysell (string): "Buy" or "Sell"
        orderPrice (int): Price you want the order at
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
            "price": orderPrice,
            "orderType": "Limit",
            "isAutomated": "true"
            }

    # Make request
    res = requests.post(url, headers=header, data=order)

    # Error stuff
    if res.status_code != 200:
        print("Limit Order Failed")
        print(res.text)
        print(res.status_code)
        print(res.reason)

    orderId = res.json()['orderId']

    return orderId


#token = getAccessToken(False)[0]
#print(placeLimitOrder(False, 1, "buy", 3700, token))
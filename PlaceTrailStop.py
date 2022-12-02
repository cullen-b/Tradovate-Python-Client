#Place TV trailing stop order
import requests
from GetAccessToken import getAccessToken
from config import *
import time


# Be careful!
# buysell must be either: "Sell" or "Buy"
def placeTrailingStopOrder(live, Qty, buysell, orderPrice, token):
    """Places trailing stop with quantity "Qty" in direction "buysell" with a price of "orderPrice"

    Args:
        live (bool): True = live, False = demo
        Qty (int): Quantity of contracts you want to buy
        buysell (string): "Buy" or "Sell
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
            "stopPrice": orderPrice,
            "orderType": "TrailingStop",
            "isAutomated": "true"
            }

    res = requests.post(url, headers=header, data=order)

    # Error
    if res.status_code != 200:
        print("TrailingStop Order Failed")
        print("Status Code:", res.status_code)
        print(res.text)
        print("Reason", res.reason)

    orderId = res.json()['orderId']

    return orderId


# Test Here
#token = getAccessToken(False)[0]
#print(placeTrailingStopOrder(False, 1, "sell", 3600, token))
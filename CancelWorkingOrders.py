# Cancels all active orders

import requests
from CancelOrder import cancelOrder
from GetAccessToken import getAccessToken


def cancelWorkingOrders(live):
    """Cancels all active/working orders

    Args:
        live (bool): True = live, False = Demo
    """

    token = getAccessToken(live)[0]

    if live:
        url = "https://live.tradovateapi.com/v1/order/list"
    else:
        url = "https://demo.tradovateapi.com/v1/order/list"

    header = {
        'Authorization': f'Bearer ${token}', 
            }

    res = requests.get(url, headers=header)
    try:
        content = res.json()
        print(content)
    except:
        if res.status_code == 200:
            print("No active orders... nothing to cancel!")
        else:
            print("Cancel orders failed...")
            print(res.status_code)
            return False

    for order in content:
        if order['ordStatus'] == "Working":
            orderId = order['id']
            cancelOrder(live, orderId, token)

    if res.status_code == 200:
        print("\nAll working orders canceled!\n")
        return True
    else:
        print("TROUBLE with /order/orderlist")
        return False


#token = getAccessToken(True)[0]
#print(token)
#cancelWorkingOrders(True, token)

# Cancels an order

import requests


def cancelOrder(live, orderId, token):
    """Cancels an order

    Args:
        live (bool): True = live acc, False = demo acc
        orderId (int): Id of order you want to cancel
        token (string): user's access token
    """
    if live:
        url = "https://live.tradovateapi.com/v1/order/cancelorder"
    else:
        url = "https://demo.tradovateapi.com/v1/order/cancelorder"

    header = {
        'Authorization': f'Bearer ${token}', 
            }

    data = {
        "orderId": orderId,
        "isAutomated": "true"
    }

    # Send request!
    requests.post(url, data=data, headers=header)
    print("\nOrder " + str(orderId) + " canceled")


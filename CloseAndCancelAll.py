#Liquidate all Positions and cancel all orders

import requests
from GetAccessToken import getAccessToken
from config import CONTRACT_ID_MESZ2, DEMO_ACCOUNT_ID, LIVE_ACCOUNT_ID


def closeAndCancelAll(live):
    """Liquidates all positions and cancels active orders on a given contract

    Args:
        live (bool): True = live, False = demo
    """

    token = getAccessToken(live)[0]

    if live:
        url = "https://live.tradovateapi.com/v1/order/liquidateposition"
        accId = LIVE_ACCOUNT_ID
    else:
        url = "https://demo.tradovateapi.com/v1/order/liquidateposition"
        accId = DEMO_ACCOUNT_ID

    header = {
        'Authorization': f'Bearer ${token}'
            }

    data = {
        "accountId": accId,
        "contractId": CONTRACT_ID_MESZ2,
        "admin": "false"
        }

    res = requests.post(url, data=data, headers=header)

    if res.status_code == 200:
        print("Positions Liquidated")
        return True
    else:
        print("Failed to cancel and close\n")
        print("Status code:", res.status_code)
        print(res.text)
        print(res.reason)

        return False


#token = getAccessToken(False)[0]
#print(closeAndCancelAll(False, token))
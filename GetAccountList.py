
import requests
from GetAccessToken import getAccessToken

# Use this to get account ID, and other information
def getAccountList(live, token):
    """Gets a list of all your accounts with Tradovate

    Args:
        live (bool): True for live account, False for demo account
        token (string): your access token
    """
    
    if live:
        url = "https://live.tradovateapi.com/v1/account/list"
    else:
        url = "https://demo.tradovateapi.com/v1/account/list"

    header = {
        'Authorization': f'Bearer ${token}', 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
            }

    res = requests.get(url, headers=header)

    print(res)
    print(res.text)
    print(res.json())


# TEST HERE
# Live = True for live account, False for demo account
#live = True
#token = getAccessToken(live)[0]
#getAccountList(live, token)

import requests
from GetAccessToken import getAccessToken

# Use this to get account ID, and other information
def getAccountList(token):
    """Gets a list of all your accounts with Tradovate

    Args:
        token (string): your access token
    """
    
    url = "https://live.tradovateapi.com/v1/account/list"

    header = {
        'Authorization': f'Bearer ${token}', 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
            }

    res = requests.get(url, headers=header)

    print(res)
    print(res.text)
    print(res.json())


#demoToken = getAccessToken(True)[0]
#getAccountList(demoToken)
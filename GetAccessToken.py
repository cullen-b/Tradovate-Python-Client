# Gets access token from TV
import requests
from config import *
 
 
# Use this function to get your Tradovate access token
# TV access tokens are very important, a lot of funcitons in the library will not work without
#  an access function 
# Please note that this funciton returns TWO values: the token and the expiry time of the token
# If you want to use this function to acces the token you must use something like:
# token = getAccessToken(True)[0]
def getAccessToken(live):
    """Gets tradovate access token for my account

    Args:
        live (bool): True for live, False for demo

    Returns:
        String: access token (very long) [0]
        String: token expiration time [1]
    """

    if live:
        url = "https://live.tradovateapi.com/v1/auth/accesstokenrequest"
    else:
        url = "https://demo.tradovateapi.com/v1/auth/accesstokenrequest"

    data = {
        "name": USER_NAME,
        "password": PASSWORD,
        "appId": APP_ID,
        "appVersion": APP_VERSION,
        "cid": CID,
        "deviceId": DEVICE_ID,
        "sec": API_SECRET
        }

    res = requests.post(url, data)
    jd = res.json()
    token = jd['accessToken']
    expTime = jd['expirationTime']

    return token, expTime


#Test Function Here
#print(getAccessToken(True))
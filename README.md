# Tradovate-Python-Client
This library jumpstarts your ability to make trades with the Tradovate API using Python! 

This is not a complete Tradovate API wrapper, it only has the code you need to make trades.

My apologies in advance for using incorrect Python Syntax...

Please keep in mind that this is my first repo and I'm still figuring things out, just becuase it works on my machine doesn't mean it will work on yours! If my code doesn't work for you I hope it can at least serve as a template for your code. 

The Tradovate documentation is terrible (they don't even have Python docs) and I know I would've appreciated something like this when I was building my project so I hope it helps you! While building this client I made use of their forums which were helpful but sparse. You can find the forums here: https://community.tradovate.com/c/api-developers/15

# AS OF EARLY 2023 THE CME HATES SMALL TRADERS!!
In early 2023 the CME started requiring expensive ($400+ /month) licenses for individual traders accesing their data through api's. I'm not sure of the total effect on this api but a lot of tradovate's api connections don't work anymore unless you have the license :(

How to use the client...

Step 1:
- Insert your data into config.py file
- Please don't share this data with anyone
- You will need to get your device id from GetDeviceID.py
    - Running GetDeviceID.py multiple times will produce different device IDs. Do not worry - this is ok 
    - I recommend picking one and sticking with it while you build your project
- Make sure this data is correct as nothing will work if it is not
    - Most of the data can be found on the tradovate app/web app
    - If there is data that can't be found on the app it is probably found in GetAccountList.py
- At the time of writing the App version is "1.0" - unless you are very far in the future I doubt this is different for you

Step 2:
- Make sure GetAccessToken.py is working
- Without this funciton you will not be able to acces the API so get this working before anything else
- Tradovate doesn't like when you request many tokens in a short timespan, I don't know the exact number/min but don't run   this function too frequently to avoid trouble

Step 3:
- Test all the functions in a DEMO enviroment first!
- Some functions will work in the DEMO and not in LIVE (but not the other way around)
    - At the time of writing everything should work, but it still may require some trial and error 
- Read the part below about how the funcitons work

How do the functions work?

Each function has a "live" parameter which is where you decide if you want this action to take place in a live enviroment or a demo envioment...
For a DEMO enviroment set "live" to False
For a LIVE envrioment set "live" to True
(should be a boolean)

Some functions have a "token" parameter.
Use GetAccessToken.py to get your access token before inputing it into the parameter
The function in GetAccessToken.py returns a tuple. The first value is the token and the second value is the token's expiry time
Please don't foget to add [0] to the end of your called getAccessToken function if you want the access token, I forgot to do this many times while developing my project and I'm sure you will too. 
NOTE: The access tokens expire after a certain amount of hours so you will need to call the funciton periodically to make sure you always have a valid token.

Some funcitons don't have a token parameter and instead have the token request inside the function.
This is becasue these functions are important and I wanted to make sure there was always a fresh access token available (Ex. Cancelling orders or closing positions) feel free to add this functionality to the other functions, just keep in mind what I said above about the Tradovate API getting mad. 

All the other function parameters should be self explanatory, and all the funcitons should have adequate docstrings to describe what they do/require/return. 

Please keep in mind that I am NOT responsible for any financial losses (or gains) that come from using my client

If all else fails feel free to contact me via email (CLNBKRPVD@GMAIL.COM) about problems with the client, I'm sure we can get it sorted out!

Happy coding, happy trading, and good luck!
-C

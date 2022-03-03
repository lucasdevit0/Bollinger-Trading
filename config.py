from binance.client import Client

# Binance API Keys
def API_keys():
    api_key = "aJT1idslE4VFdlGiqTNMiwDd6UExuRyviJiViRyRI1ZX0Q3uDZTy7Ek50lMfPD9P"
    api_secret = "WIPOuCCsQlqKPFFlJNyX8LcTwH1ACkoMRvsTTOzGPD8fMidzCySZ5aQDfV2EFw8E"

    #Create client
    client = Client(api_key, api_secret)

    #Make sure Acc. is connected and ready to trade
    info = client.get_account()
    if info['canTrade'] == True:
        print('Binance Connected. Ready to trade.')
        return client
    else:
        print('Binance connection failed')
        return 0


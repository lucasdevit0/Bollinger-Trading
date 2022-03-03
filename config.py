from binance.client import Client

# Binance API Keys
def API_keys():
    api_key = ""
    api_secret = ""

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


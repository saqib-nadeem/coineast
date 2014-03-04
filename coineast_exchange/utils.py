import json
import requests
import pymongo
from pymongo import Connection

#----------------------------------------
# MongoLab-Connection
#----------------------------------------


MONGODB_URI = 'mongodb://admin:admin@ds027749.mongolab.com:27749/project'
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

def get_user(email):
    profile = {}
    cursor = db['user'].find({'email': email})

    if cursor.count() == 0:
        return None
    else:
        result = cursor[0]
        return result

def get_user_balance(email):
    user = get_user(email)
    if user is None:
        return None
    else:
        return user['balance']
        
def get_user_BTC(email):
    user = get_user(email)
    if user is None:
        return None
    else:
        return user['BTC']
    
def update_balance(email, new_balance):
    user = get_user(email)
    if user is None:
        return None
    else:
        user['balance'] = new_balance
        db['user'].save(user)
        return user

def update_BTC(email, new_BTC):
    user = get_user(email)
    if user is None:
        return None
    else:
        user['BTC'] = new_BTC
        db['user'].save(user)
        return user

def update_view_instructions(email, status):
    user = get_user(email)
    if user is None:
        return None
    else:
        user['view_instructions'] = status
        db['user'].save(user)


def open_url(url):
    data = None
    try:
        e = requests.get(url)
        result = json.loads(e.text)
    except:
        pass
    else:
        if e.status_code == 200:
            data = result
    return data

def btc_price_in_usd():
    coinvibes_api_url = "http://www.coinvibes.com/api/v1/tickers/bitstamp/btc_usd"
    data = open_url(coinvibes_api_url)
    usd_price = data['bid']
    return usd_price

def usd_rate_in_pkr():
    currency_api_url = "http://dreams-soft.com/apps/android/currency/rates?currency=pkr&token=xqS6u5sh7SLunBopwE61tMCEME35412F"
    data = open_url(currency_api_url)
    pkr_rate = float(data['data']['rates']['PKR'])
    return pkr_rate

def btc_price_in_pkr():
    btc_in_usd = btc_price_in_usd()
    usd_in_pkr = usd_rate_in_pkr()
    btc_pkr_price = str(btc_in_usd * usd_in_pkr)
    return btc_pkr_price


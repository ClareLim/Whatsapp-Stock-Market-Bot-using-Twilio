# MARKETSTACK_KEY

#0 explore Marketstack doc and find relevant URL
#1 start getting prices of given stock - integrate the API

# import os to access env variable
import os
# import request module to call market stack API
import requests
import json

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol): 
    params = {
        'access_key': API_KEY,
    }
    end_point = ''.join([BASE_URL, "tickers/", stock_symbol, "/intraday/latest"])
    api_result = requests.get(end_point, params)
    # print(api_result.text)
    json_result = json.loads(api_result.text)
    return {
        "last_price": json_result["last"]
    }

# result = get_stock_price("AAPL")
# print(result)
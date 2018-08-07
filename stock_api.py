import json
import urllib.parse
import urllib.request
import requests
import re

BASE_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=LJ41HKQ3UC5G59SD&symbol="

class InvalidSymbol(Exception):
    pass

class APIException(Exception):
    pass

def create_url(symbol: str):
    return BASE_URL + symbol

def get_data(url: str)->dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        json_text = json.loads(json_text)
        return json_text
    except:
        raise APIException

    finally:
        if response != None:
            response.close()

def check_valid(data):
    try:
        if data["Error Message"]:
            raise InvalidSymbol
    except KeyError:
        return
    pass
    
def get_current_close(json: dict):
    #print(type(json))
    date = json["Meta Data"]["3. Last Refreshed"]
    current = json[date]["4. close"]
    return [current, date]
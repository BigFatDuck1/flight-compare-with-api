import requests
import os
from dotenv import load_dotenv

# https://tequila.kiwi.com/portal/docs/tequila_api/search_api

load_dotenv()

# ! Use your own API key from Kiwi!
api_key = os.environ.get("api_key")
header = {"apikey": api_key}
endpoint = "https://tequila-api.kiwi.com/v2/search"

# TODO: Put your departure from location here 
depart_from = "city:HKG"

class FlightSearch:        
    
    def get_price(self, destination, from_date, to_date, currency, max_price):
        body = {
            "fly_from": depart_from,
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "selected_cabins": "C",
            "curr": currency,
            "price_to": max_price
        }

        response = requests.get(url=endpoint, params=body, headers=header)

        #Find price
        returned_data = response.json()["data"]
        price_for_adults = returned_data[0]["price"]

        return price_for_adults



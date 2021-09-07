import csv
import pandas
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# ! Use your own API key from Kiwi!
api_key = os.environ.get("api_key")

header = {"apikey": api_key}
api_endpoint = "https://tequila-api.kiwi.com/locations/query"

# Creates a dataframe called flight_data
flight_data = pandas.read_csv("flight_data.csv")
cities_series = flight_data["City"]
IATA_series = flight_data["IATA"]
cities_list = cities_series.to_list()

class FlightData:

    def query_for_IATA_code():

        #Blank array to fill in IATA codes
        IATA_codes = []

        #API request stuff 
        header = {"apikey": api_key}

        #Find IATA codes from API
        for each_city in cities_list:
            query = {
                "term": each_city, 
                "location_types": "city"
            }

            # API request
            response = requests.get(url=api_endpoint, headers=header, params=query)
            
            # Get location (key) in response
            location = response.json()["locations"]
            # Get code (value) from location (key)
            #Get the first list
            location_first_list = location[0]
            #Get the id from the first list
            id = location_first_list["code"]
            IATA_codes.append(id)
        
        return IATA_codes






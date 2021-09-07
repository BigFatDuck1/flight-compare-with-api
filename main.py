from find_iata_codes import FlightData, flight_data
from flight_search import FlightSearch
import pandas

newSearch = FlightSearch()

#Returns a list of the IATA codes
id_codes = FlightData.query_for_IATA_code()

#Modify the series
flight_data["IATA"] = id_codes

flight_data.to_csv(path_or_buf="flight_data_with_IATA.csv", index=False)

# Get the IATA codes column
IATA_file = pandas.read_csv("flight_data_with_IATA.csv")
IATA_dict = dict(zip(IATA_file["IATA"], IATA_file["Lowest Price"]))


discounts = {}

# Obtain price for every city
for city,price in IATA_dict.items():
    try:
        #Fill in dates here
        result = newSearch.get_price(city, "10/10/2021", "25/12/2021", "HKD", str(price))
        discounts[city] = result
    except:
        discounts[city] = "Not available"

print(discounts)



import requests
import json
from datetime import date, timedelta
from last_date import last_date
import time


url = "https://covid-19-data.p.rapidapi.com/report/country/code"

#2020-01-31 -> 2020-06-1

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "f8542a8d8amsh53557ef9a891d92p1f5fadjsn2d0f8c255ba5"
    }

# results = json.loads(response.text)

# print(results[0]["provinces"][0]["deaths"])



# with open('Covid_Data.txt', 'r') as file:
#     data = file.read()

# data = json.loads(data)


# print(last_date(data))


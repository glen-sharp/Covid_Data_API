import requests
import json
from datetime import date, timedelta
import time
from last_date import last_date

url = "https://covid-19-data.p.rapidapi.com/report/country/code"

#2020-01-31 -> 2020-06-1

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "f8542a8d8amsh53557ef9a891d92p1f5fadjsn2d0f8c255ba5"
    }

def add_data():

    with open('Covid_Data.txt', 'r') as file:
        data = file.read()

    data = json.loads(data)

    single_date = last_date(data)
    start_date = date(int(single_date[0]), int(single_date[1]), int(single_date[2]))
    deaths = {}
    itt = 0
    while True:
        start_date = start_date + timedelta(1)
        querystring = {"date":start_date,"code":"gb","format":"json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        results = json.loads(response.text)
        try:
            result = results[0]["provinces"][0]["deaths"]
        except KeyError:
            break
        print(start_date)
        print(result)
        deaths[str(start_date)] = int(result)
        itt = itt + 1
        time.sleep(2)

    print(deaths)

    data.update(deaths)

    print(data)

    with open('Covid_Data.txt', 'w') as file:
        file.write(json.dumps(data))
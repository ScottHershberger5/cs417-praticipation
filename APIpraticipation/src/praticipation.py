import requests
import csv


response = requests.get(
    'http://date.nager.at/api/v3/publicholidays/2026/US',
)


data = response.json() #turn the response into a Json

data_MLK = data[1] #simplify it down to one date


with open('MLK_data.csv', "w", newline = "", encoding = "utf-8") as f: #turn the Json into a csv
    fieldnames = ["date", "localName", "countryCode"]
    writer = csv.DictWriter(f, fieldnames = fieldnames, extrasaction  = 'ignore')

    writer.writeheader()
    writer.writerow(data_MLK)
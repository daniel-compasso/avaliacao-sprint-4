import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["covidindiadb"]
mycol = mydb["covidindiadbtable"]

URL = 'https://api.covid19india.org/data.json'

response = requests.get(URL)
print(response.json())

x = mycol.insert_one(response.json())
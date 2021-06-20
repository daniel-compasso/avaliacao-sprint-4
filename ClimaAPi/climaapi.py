import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ClimaAPIdbdb"]
mycol = mydb["ClimaAPidbtable"]

openweathermap_KEY = '4e813866cb5b3cd562d3c7a0b7bca99a'
tomtom_KEY = 'l7BHMV8QTASNZPyYZC7EJ7xhoRAXRS1l'
URL = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric&lang=pt_br"

response = requests.get(URL)
print(response.json())

x = mycol.insert_one(response.json())
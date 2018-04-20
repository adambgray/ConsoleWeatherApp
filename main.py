import requests
import json

zipcode = input("Enter a US zip code:")

url = "http://api.openweathermap.org/data/2.5/weather"

querystring = {"APPID":"3c3e2aa1bb0dbb728b2cfe17ac264992","units":"imperial","zip":"{0},us".format(zipcode)}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "0e4f597a-3276-4819-bd52-2a37fdbfccb9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

obj = json.loads(response.text)
print("The temperature in " + obj["name"] + " is " + str(obj["main"]["temp"]) + " degrees F.")
print("Winds are currently " + str(obj["wind"]["speed"]) + " miles per hour.")
print("It is " + str(obj["clouds"]["all"]) + '''%''' +  ' cloudy.')

#print(response.text)
#print(type(response.text))
#!/usr/bin/env python3

import requests
import json

###################
# Variables
###################

#### Site air quality 


site = "https://api.waqi.info/feed/"  # Air quality website API
city = "@2994"   # City to monitor
token = "37880a6310a514b11b8e86b1d76f24db47dcd2ab"  # API token

url = site+city+"/?token="+token

#### Domobox

domobox = "https://domobox.maison.lan/json.htm?"
IDX_alerte = "35"

##################
# Fonctions
##################

### Get air quality value

def getAirQuality(consolidatedUrl):
  """ Récupère la qualité de l'air sur le site World Air Quality Index """
  r = requests.get(consolidatedUrl)
  raw = r.json()
  for key, value in raw.items():
    if (key == "data"):
      aqi = int(value['aqi'])
  return(aqi)

def getAlertState(id):
  """ Récupère le status actuel de l'alerte """
  urlDomo = domobox+"type=devices&rid="+id
  r = requests.get(urlDomo,verify=False)
  dataDB = r.json()
  for i in dataDB["result"]:
    level = i["Level"]
  return(level)
  

print(getAirQuality(url),type(getAirQuality(url)))
print(getAlertState(IDX_alerte),type(getAlertState(IDX_alerte)))

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
IDX_alerte = "33"

##################
# Fonctions
##################

### Get air quality value


def getAirQuality(consolidatedUrl):
  
  r = requests.get(consolidatedUrl)
  raw = r.json()
  for key, value in raw.items():
    if (key == "data"):
      aqi = int(value['aqi'])
  return(aqi)

print(getAirQuality(url),type(getAirQuality(url)))

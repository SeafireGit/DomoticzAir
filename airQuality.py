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
IDX_alert = "35"

#### Air level

table = {0:'Pas de données', 1:'Bon',2:'Moyen',3:'Malsain pour gp sensibles',4:'Malsain'}

##################
# Fonctions
##################

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
    urlDomo = '{0}type=devices&rid={1}'.format(domobox,id)
    r = requests.get(urlDomo,verify=False)
    dataDB = r.json()
    for i in dataDB["result"]:
      level = i["Level"]
    return(level)

def updateAlert(now):
    """ Update la device alert avec le niveau now """
    requests.get('{0}type=command&param=udevice&idx={1}&nvalue={2}&svalue={3}'.format(domobox,IDX_alert,str(now),table[now]),verify=False)

def defineLevel(mesure):
    """ Définit le niveau de l'alerte en fonction de la valeur de l'index recue """
    if ( 1 < mesure <= 50):
      now = 1
    elif ( 50 < mesure <= 100):
      now = 2
    elif ( 100 < mesure <= 150):
      now = 3
    elif ( 150 < mesure):
      now = 4
    return(now)

##################
# Execution
##################

if __name__ == '__main__':

    actualLevel = defineLevel(getAirQuality(url))
    print(actualLevel)    # Debug

    if ( actualLevel != getAlertState(IDX_alert)):
      updateAlert(actualLevel)

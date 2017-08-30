#!/usr/bin/env python3

import unittest
from airQuality import *

class AirTest(unittest.TestCase):
  """ Test case utilisé pour controlé les fonctions de DomoticzAir """

  def SetUp(self):
    """ Initialisation """

  def test_getAirQuality_int(self):
    """ Test que le retour de la connection au site renvoi un entier """
    test = getAirQuality(url)
    self.assertTrue( type(test) == int)


  def test_getAirQuality_ok(self):
    """ Test que le retour de la connection au site renvoi un entier compris entre 0 et x """
    test = getAirQuality(url)
    self.assertTrue( 0 < test < 400)

  def test_getAlertState(self):
    """ Test que le retour de la récupération de l'état de l'alerte est un entier entre 1 et 4 """
    test = getAlertState(IDX_alert)
    self.assertTrue( 0 <= test <= 4)

  # Test de la fonction defineLevel
  def test_defineLevel_1(self):
    """ Test qu'un AQI de 45 donne bien un level de 1 """
    aqi = 45
    self.assertTrue( defineLevel(aqi) == 1)

  def test_defineLevel_2(self):
    """ Test qu'un AQI de 62 donne bien un level de 2 """
    aqi = 62
    self.assertTrue( defineLevel(aqi) == 2)

  def test_defineLevel_3(self):
    """ Test qu'un AQI de 123 donne bien un level de 3 """
    aqi = 123
    self.assertTrue( defineLevel(aqi) == 3)

  def test_defineLevel_4(self):
    """ Test qu'un AQI de 250 donne bien un level de 4 """
    aqi = 250
    self.assertTrue( defineLevel(aqi) == 4)

if __name__ == '__main__':
    unittest.main()

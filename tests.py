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
    test = getAlertState(IDX_alerte)
    self.assertTrue( 0 <= test <= 4)

if __name__ == '__main__':
    unittest.main()

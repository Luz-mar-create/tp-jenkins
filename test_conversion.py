from conversion import km_miles
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def test_km_miles():
   # Test avec différentes valeurs
   test_distances = [
      (0, 0.0),
      (1, 0.621371),
      (5, 3.106855),
      (10, 6.21371),
      (100, 62.1371)
   ]

   for km, valAttendu in test_distances:
      resConv = km_miles(km)
      assert round(resConv, 6) == round(valAttendu, 6)

      logger.info(f"km_miles({km}) = {resConv}, attendu = {valAttendu}")
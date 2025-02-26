from nombres import calculs
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def test_calculs():
    num1 = 10
    num2 = 5
    
    # Appel de la fonction
    resCalc = calculs(num1, num2)

    # Attentes des résultats
    res_somme = num1 + num2
    res_difference = num1 - num2
    res_moyenne = (num1 + num2) / 2

    # Log des résultats obtenus
    logger.info(f"Test calculs({num1}, {num2}) = {resCalc}")

    # Vérification avec assert
    assert resCalc[0] == res_somme, f"Erreur: Somme attendue {res_somme}, obtenue {resCalc[0]}"
    assert resCalc[1] == res_difference, f"Erreur: Différence attendue {res_difference}, obtenue {resCalc[1]}"
    assert resCalc[2] == res_moyenne, f"Erreur: Moyenne attendue {res_moyenne}, obtenue {resCalc[2]}"



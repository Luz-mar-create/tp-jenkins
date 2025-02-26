def calculs(num1, num2):
    # Calcull des opérations demandées
    somme = num1 + num2
    difference = num1 - num2
    moyenne = (num1 + num2) / 2

    return somme, difference, moyenne

# Seulement exécuter si le script est lancé manuellement
if __name__ == "__main__":
    num1 = float(input("Entrez le 1er nombre: "))
    num2 = float(input("Entrez le 2ème nombre: "))

    # Appel de la fonction et récupération des résultats
    somme, difference, moyenne = calculs(num1, num2)

    # Affichage des résultats
    print(f"Somme : {somme:.2f}")
    print(f"Différence : {difference:.2f}")
    print(f"Moyenne : {moyenne:.2f}")
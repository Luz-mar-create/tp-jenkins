def calculs(num1, num2):
    # Calcull des opérations demandées
    somme = num1 + num2
    difference = num1 - num2
    moyenne = (num1 + num2) / 2

    return somme, difference, moyenne

# Demande à l'utilisateur d'entrer deux nombres
num1 = float(input("Entrez le 1er nombre: "))
num2 = float(input("Entrez le 2ème nombre: "))

# Appel de la fonction et récupération des résultats
somme, difference, moyenne = calculs(num1, num2)

# Affichage des résultats
print(f"Somme : {somme}")
print(f"Différence : {difference}")
print(f"Moyenne : {moyenne}")
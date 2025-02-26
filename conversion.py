def km_miles(km):
    return km * 0.621371

if __name__ == "__main__":
    distances_km = [0, 1, 5, 10, 100] # Liste de valeurs prédéfinies
    for km in distances_km:
        miles = km_miles(km)
        print(f"{km} km équivaut à {miles:.2f} miles")
import numpy as np
from time import sleep
import time

#Rapporter temps au mieux/pire
# Rapporter Moyenne
# Graphe des valeurs obtenus

delay = 0.1
tempsMax = 0
tempsMin = 10
tempsMoy = 0
k=0 # compteur

def mystere(T):
    i = 0

    while i<n and T[i] != True :
        i = i +1
        sleep(delay)
    return i

# Définir la taille n
n = int(input('Taille du tableau ?'))
# Créer une liste pour stocker les tableaux
arrays = []
# Boucle sur toutes les combinaisons possibles de "VRAI" et "FAUX"
for i in range(2**n):
    # Créer un tableau de zéros avec la taille n
    array = np.zeros(n, dtype=bool)
    # Mettre à jour les valeurs du tableau en fonction de la combinaison actuelle
    for j in range(n):
        if (i & (1 << j)) != 0:
            array[j] = True
    # Ajouter le tableau à la liste des tableaux
    arrays.append(array)
# Afficher la liste des tableaux
for array in arrays:
    k = k + 1
    start = time.time()
    print('\n')
    print(mystere(array))
    print(array)
    tempsAlgo = time.time() - start
    if tempsAlgo > tempsMax :
        tempsMax = tempsAlgo
    else:
        tempsMin = tempsAlgo
    tempsMoy = tempsMoy + tempsAlgo


    print("L'algorithme a mis ",tempsAlgo,"seconde(s)")

tempsMoy = tempsMoy/k
print('\n')
print("Le temps maximum(temps aure pire) :",tempsMax)
print("La moyenne (coûts en moyenne) :",tempsMoy)
print("Le temps minimum(Coût au mieux) :",tempsMin)

#print(mystere(arrays))


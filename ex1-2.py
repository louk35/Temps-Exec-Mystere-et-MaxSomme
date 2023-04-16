import random
from math import *
import numpy as np
from time import sleep
import time


#########Fonction#########

def MaxSomme1(T,k):
    maxsomme = 0
    for i in range (k):
        somme = 0
        for j in range(i, k):

            somme = somme+T[j]
            if somme > maxsomme:
                maxsomme = somme

    return maxsomme
#Voir si erreur vient des tableaux 0 à n / 1 à n
def MaxSomme2(T,debut,fin):
    if debut == fin:
        return max(0,T[fin])
    milieu = floor((debut+fin)/2)
    #
    mg = 0
    somme = 0
    i = milieu
    #
    while i >= debut:
        somme = somme +T[i]
        mg=max(mg,somme)
        i = i-1
    #
    md = 0
    somme = 0
    i = milieu+1
    #
    while i<=fin:
        somme = somme+T[i]
        md=max(md,somme)
        i = i+1
    return max((mg+md),(MaxSomme2(T,debut,milieu)),MaxSomme2(T,milieu+1,fin))

def MaxSomme3(T,n):
    p = 0
    q = 0
    i = 0
    while i <=n-1:
        q = max((q+T[i]),0)
        p = max(p,q)
        i = i + 1
    return p
################## ALGO PRINCIPALE ##############################
# Définir la taille n
n = int(input('Taille du tableau ?'))
num_arrays = 200 # nombre de tableaux à générer
debut = 0
fin = n - 1
tempsMax = 0
tempsMin = 10
tempsMoy = 0
t=0


for i in range(num_arrays):
    array = []
    if n%2 != 0:            # Si le taille n est impair | Pour conserver un intervale d'entier on va arrondir la division de n
        a = floor(n/2)     # On arrondi la division à l'entier inférieur
        x = random.randint(1,a)

        b = ceil(-n/2)   # On arrondi la division à l'entier supérieur
        y = random.randint(b, -1)

        # ajoute d'un entier positif et négatif dans le tableau
        array.append(x)
        array.append(y)
    elif n/2 >= 1:
        a = floor(n/2)     # On arrondi la division à l'entier inférieur
        x = random.randint(1,a)

        b = ceil(-n/2)   # On arrondi la division à l'entier supérieur
        y = random.randint(b, -1)
        array.append(x)
        array.append(y)

    # remplir le reste du tableau avec des entiers aléatoires dans l'intervalle [-n/2 ; n/2] et avec 0 exclu
    while len(array) < n:
        value = random.randint(-(n//2), n//2)
        if value != 0:
            array.append(value)

    # mélanger du tableau pour rendre l'ordre des éléments aléatoire
    random.shuffle(array)

    print('\n')
    print("tableau n°",i+1,array)
    #resultat1= MaxSomme1(array,n) # appel fonction MaxSomme1
    start = time.time()
    resultat3= MaxSomme3(array,n) # appel fonction MaxSomme3
    tempsAlgo = time.time() - start

    if tempsAlgo >= tempsMax:
        tempsMax = tempsAlgo
    elif tempsAlgo < tempsMin:
        tempsMin = tempsAlgo
    tempsMoy = tempsMoy + tempsAlgo

    #print("Temps de l'algo",i+1,tempsAlgo)
    #print("MaxSome1 :",resultat1)

    #resultat2 = MaxSomme2(array,debut,fin)# appel fonction MaxSomme2
    #print("MaxSome2 :",resultat2)

    #resultat3= MaxSomme3(array,n) # appel fonction MaxSomme3
    print("MaxSome3 :",resultat3)
tempsMoy = tempsMoy/num_arrays
print("Le temps maximum(temps aure pire) :",tempsMax)
print("La moyenne (coûts en moyenne) :",tempsMoy)
print("Le temps minimum(Coût au mieux) :",tempsMin)



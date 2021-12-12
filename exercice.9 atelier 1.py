def matrice(mat): # fonction qui cherche un élément dans une matrice
     result = np.where(mat == 1) #numpy.where() :trouver l’indice d’une liste en python
     return result

import numpy as np #numpy : tableau multidimensionnels (doit déjà installer en pycharm)
mat= np.array([[1, 4],[2, 8]]) #convertir une liste python en un tableau
print(mat)
print(matrice(mat)) #appelle à la fonction

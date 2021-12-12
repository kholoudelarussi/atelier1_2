def inverse(chaine): #définir une fonction pour inverser les lettres d’une chaine de caractère
 if (chaine == 0):
    return 0
 else:
  reversed_string=''.join(reversed(chaine)) #la fonction reversed() donne l’iterateur inverse de la chaine donnée. Ses éléments sont joints par la chaine vide à l’aide de la méthode join() qui fusionne tous les caractères résultant de l’itération inversée dans une nouvelle chaine.
  return reversed_string
chaine= str(input("entrez la chaine"))
print(" La chaine renversee est", inverse(chaine)) #affichage du résultat avec l’appel à la fonction

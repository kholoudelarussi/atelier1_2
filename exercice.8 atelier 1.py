
def freq(chaine):#la fonction qui construit le dictionnaire contenant toutes les lettres de la chaine    d, compteur = {},# 0  #On initialise le dictionnaire et une variable compteur qui a pour mission de compter toutes les lettres du texte.
  d, compteur = {}, 0
  # on parcourt toute la chaine en faisant une boucle de variable c
  for c in chaine:
        if c.lower() not in d: #si la minuscule de la lettre sur laquelle on est n’est pas encore dans le dictionnaire
                d[c.lower()] = 1
                compteur += 1#une incrémentation de cette variable; à chaque fois que j’ajoute une clé au dictionnaire (un caractère) et à chaque fois que je modifie une valeur.
        else:
            d[c.lower()] += 1
            compteur += 1
  return d, compteur #retourner au dictionnaire d et au compteur
chaine= str(input("entrez la chaine"))#déclarer le type de donnée insérer
d , compteur = freq(chaine) #appel à la fonction
L = sorted(d.items(), key = lambda colonne: colonne[1] , reverse = True) # on construit une liste avec les éléments du dictionnaire. Pour cela, on a avant tout ordonné les valeurs des occurrences; ainsi, la première valeur de la liste est le caractère qui est répété le plus de fois.
for i in L:
    print('{} : {}'.format(i[0],i[1]/compteur)) # “i[1]/compteur” qui correspond à la fréquence de la lettre (nombre d’occurrences par rapport au nombre total de lettres).

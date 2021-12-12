l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(l1)
d = {} #On initialise le dictionnaire
for element in l1:# on parcourt tout la liste en faisant une boucle de variable element
    if element not in d:
        d[element] = 1
    else:
        d[element] += 1
    print(d)
L = sorted(d.items(), key = lambda colonne: colonne[1] , reverse = True)#on construit une liste avec les éléments du dictionnaire. Pour cela, on a avant tout ordonné les valeurs des occurrences; ainsi, la première valeur de la liste est le caractère qui est répété le plus de fois
for i in L:
 print('{} : {}'.format(i[0],i[1]))#nombre d’occurrences dans cette liste

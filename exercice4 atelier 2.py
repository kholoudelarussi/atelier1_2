set1={23, 42, 65, 57, 78, 83, 29}#crée une set
print(set1)
set2={57, 83, 29, 67, 73, 43, 48}
print(set2)
set3=set1.intersection(set2)#l’intersection des deux set (pas des éléments doubles)
print(set3)
print("Set 1 après suppression :",set1.difference(set3))#supprimer les éléments du set3 dans set1

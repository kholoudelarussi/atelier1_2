l1=[47, 64, 69, 37, 76, 83, 95, 97]
print(l1)# affichage du liste
d={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

for i in d.values():#verifier si les valeurs de d existe dans la liste
    print(i)#afficher justement les valeurs qui existe dans la liste
    print(l1[0] in d.values())#si il existe afficher true sinon false(supprimer la liste)
l1=d.values()#la liste egale les valeurs commun entre d et l1
print(l1)#affichage du resultat

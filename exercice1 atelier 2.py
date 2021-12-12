l1=[3, 6, 9, 12, 15, 18, 21] # création une liste avec des nombres
l1impaire=[l1[1],l1[3],l1[5]] # trouve les éléments de la liste  à partir de indices
print([l1impaire]) #affichage le la nouvelle liste (l1impaire)
l2=[4, 8, 12, 16, 20, 24, 28]
l2paire=[l2[0],l2[2],l2[4],l2[6]]
print([l2paire])
l3=l1impaire+l2paire #concaténer les 2 nouveaux listes
print(l3)

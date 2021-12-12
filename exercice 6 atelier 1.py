# définir la fonction du tri à bulle

def tri_bulle(tab):
 n = len(tab)
 for i in range(n):#traverser tous les éléments du tableau
        for j in range(0, n - i - 1):
         if tab[j] > tab[j + 1]:#échanger si l’élément trouve est plus grand que le suivant
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
def tri_selection(tab): #définir la fonction du tri par sélection
    for i in range(len(tab)):
       min = i#trouver le min
    for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j
                tmp = tab[i]
                tab[i] = tab[min]
                tab[min] = tmp
    return tab
def tri_insertion(tab): #definir la fonction du tri par insertion
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
tab = [28, 12, 20, 1, 92]
tri_bulle(tab) #appelle à la fonction du tri à bulle
tri_selection(tab) #appelle à la fonction du tri par sélection
tri_insertion(tab) #appelle à la fonction du tri par insertion
print("Le tableau trié est:") #affichage de cette phrase
for i in range(len(tab)): #pour que i<=la longueur du tableau
    print("%d" % tab[i]) #affichage du resultat

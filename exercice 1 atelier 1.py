def fact(n): #definir la fonction de factoriel
#instruction if else
   if(n<2):
        return 1
   else:
        return n*fact(n-1)#retourner a la fonction factoriel(definir la relation factoriel)
s=0#initialisation du variable s(la somme)
for i in range(1,6):#boucle for pour que i=1 et i<=6
 s=s+(fact(i)/i)#la somme du série avec l’appel du fonction
print("la somme est",s)#affichage du résultat

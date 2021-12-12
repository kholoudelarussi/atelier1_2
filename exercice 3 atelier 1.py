def sommation(n): #definir la fonction du recursivite pour calculer la somme des nombres de 1 à n
 if (n == 1): #instruction if else
    return 1
 else:
   res = n + sommation(n - 1) #la  relation pour calculer la somme des nombres de 1 à n
   return res
som = 0 # initialiser som à 0
n= int(input("Enter n: ")) #déclarer le type de donnée insérer
som = sommation(n) #appeler la fonction
print("la somme des %premiers termes est :", som) #affichage du résultat

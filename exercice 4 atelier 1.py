def fibonacci(n): #definir la finction du recursivite du Fibonacci
 if (n<=0): #instruction if else
  return 1
 else:
  return (fibonacci(n - 1) + fibonacci(n - 2)) #retourner a la fonction

nbr= int(input("Enter nbr: ")) #déclarer le type de donnée insérer
print("Les premiers termes de la série de Fibonacci sont:\n", nbr) #entrer le nombre n pour l’exécution
for i in range(nbr): #pour n<=nbr
        print( fibonacci(i)) #affichage du résultat avec l’appel du fonction

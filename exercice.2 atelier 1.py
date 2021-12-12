def conv(n):# définir la fonction pour convertir un nombre décimal en binaire
#instruction if else
 if n==0:
  return 0
 else:
  return(n%2)+(10*conv(n//2)) # definir la relation pour convertir un nombre décimal en binaire
n=int(input("entrez la valeur de n"))#déclarer le type de donnée insérer
print("la convertission est",conv(n))#affichage du résultat avec l’appel du fonction

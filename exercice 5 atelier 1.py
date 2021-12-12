def compter(n): #definir une fonction pour compter les chiffres d’un nombre
    nombre = len(str(n)) # pour calculer la longueur d’une chaine (nombre)
    return nombre

n=str(input("Enter n: ")) #déclarer le type de donnée insérer
print(compter(n)) #affichage du résultat avec l’appel à la fonction

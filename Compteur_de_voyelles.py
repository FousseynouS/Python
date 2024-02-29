def compter_voyelles(mot):
    voyelles = "aeiouyAEIOUY"
    nombre_voyelles = 0
    
    for lettre in mot:
        if lettre in voyelles:
            nombre_voyelles += 1
            
            
    return nombre_voyelles

mot = input("Veuillez saisir un mot : ")
print("Le nombres de voyelles dans le mot est de ",compter_voyelles(mot))

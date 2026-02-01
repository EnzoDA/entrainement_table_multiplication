def menu_principal():
    # Ici, j'affiche le menu principal
    print("1. Révision")
    print("2. Exercice")
    print("3. Toutes les Tables de multiplications")
    print("4. arreter \n")

    return int(input("Choisi le mode que tu veux : "))

def menu_revision():
    # Ici, j’affiche le menu de révision
    print(" 1. apprendre multiplication par multiplication ")
    print(" 2. Voir la table entière ")
    print(" 3. arreter \n")

    return int(input("Votre choix : "))

def menu_exo():
    # Ici, j’affiche le menu des exercices
    print("1. s'entrainer sur une table ")
    print("2. s'entrainer sur toutes les tables \n")
    return int(input("Choisie le mode que tu veux : "))



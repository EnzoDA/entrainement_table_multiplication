from menus.menus import *
from revision.revision import *
from exercices.exercices import *


def main():
    # Ici, je récupère le choix principal de l’utilisateur
    choix = menu_principal()
    
    if choix == 1:
        # L’utilisateur choisit une table à réviser
        table_choisie = Revision.table()

        # J’affiche ensuite le menu dédié à la révision
        choix_revision = menu_revision()
        
        if choix_revision == 1:
            # Ici, j’explique la table multiplication par multiplication
            Revision.apprendre_multi_par_multi(table_choisie)

        if choix_revision == 2:
            # Ici, je lance l’apprentissage complet de la table choisie
            Revision.apprendre_toute_la_table(table_choisie)

        if choix_revision == 3:
            # Je quitte le programme si l’utilisateur le souhaite
            exit()

    if choix == 2:
        # J’affiche le menu des exercices
        choix_exo = menu_exo()
        
        # Je crée une instance de la classe Exercice
        exo = Exercice()

        if choix_exo == 1:
            # L’utilisateur choisit une table précise pour s’exercer
            table_choisie = Exercice.table()

            # Je lance l’exercice sur une seule table
            start_time = time.perf_counter()
            exo.exo_une_table(table_choisie)

        if choix_exo == 2:
            # Ici, je démarre un exercice avec toutes les tables mélangées
            start_time = time.perf_counter()
            exo.exo_toutes_les_tables()

    if choix == 3:
        # J’affiche toutes les tables de multiplication
        Revision.toutes_les_tables()
            
    if choix == 4:
        # Je ferme proprement le programme
        exit()


# Point d’entrée du programme
main()



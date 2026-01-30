from menus.menus import *
from revision.revision import *
from exercices.exercices import *

def main():
    choix = menu_principal()
    
    if choix == 1 :
        table_choisi = Revision.table()
        choix_revision = menu_revision()
        if choix_revision == 1 :
            Revision.apprendre_multi_par_multi(table_choisi)
                    

        if choix_revision == 2: 
            Revision.apprendre_toute_la_table(table_choisi)
            

        if choix_revision == 3:
            exit()

    if choix == 2 : 
        choix_exo = menu_exo()
        
        exo = Exercice()
        if choix_exo == 1:
            table_choisi = Exercice.table()
            start_time = time.perf_counter()
            exo.exo_une_table(table_choisi)
            

        if choix_exo == 2:

            start_time =time.perf_counter()
            exo.exo_toutes_les_tables()
            

    if choix == 3:
       Revision.toutes_les_tables()
            
    if choix == 4:
        exit()

main()
class Revision:

    def __init__(self):
        # Ici, j’initialise une variable dans mon constructeur qui pourra me servir plus tard
        self.numero = 0 
    
    def table():
        # Là, je demande à l’utilisateur quelle table il veut réviser
        return int(input("Choisis la table : "))
    
    def apprendre_multi_par_multi(table):
        # Ici, j’indique quelle table est en cours de révision
        print("Vous révisez la table du", table)
        
        for numero in range(11):
            print(table, "X", numero, "=")
            
            input("Appuie sur Entrée pour voir le résultat : ")
            
            total = table * numero
            print(" ", total)

    def apprendre_toute_la_table(table):  
        # Là, j’affiche directement toute la table sans pause
        print("Vous révisez la table du", table)
        
        for numero in range(11):
            total = table * numero
            print(table, "X", numero, "=", total)

    def toutes_les_tables():
        # Ici, j’affiche toutes les tables de 0 à 10
        for table in range(11):
            print("\n", "Voici la table du", table)
            
            for numero in range(11):
                total = table * numero
                print(table, "X", numero, "=", total)




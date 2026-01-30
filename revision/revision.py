class Revision:

    def __init__(self):
        self.numero =  0 
    
    def table():
        return int(input("Choisis la table : "))
    
    def apprendre_multi_par_multi(table):
        print("Vous réviser la table du ", table)
        for numero in range(11):
            print(table, " X ", numero, " = ")
            input("Appuie sur Entrée pour voir le résultat : ")  # autre alternative avec la librairie kayboard     keyboard.wait('enter')
            total = table * numero
            print(" ", total)

    def apprendre_toute_la_table(table):  
        print("Vous réviser la table du ", table)
        for numero in range(11):
            total = table * numero
            print(table, " X ", numero, " = ", total)

    def toutes_les_tables():
        for table in range(11):
            print("\n","Voila la table du ", table )
            for numero in range(11):
                total = table * numero
                print(table, " X ", numero, " = ", total)









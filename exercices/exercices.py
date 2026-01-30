import random as rd
import time
class Exercice:
    def __init__(self):
       self.list_bon_resultat = []
       self.list_resultats_utilisateur = []
       self.list_mauvaise_reponse = []
       self.nombre_mauvaise_reponse = 0
       self.note = 0
       self.start_time = time.perf_counter()

    @staticmethod
    def table():
        return int(input("Choisis la table : "))
    
    def exo_une_table(self, table):
        for i in range(10):
        
            random_number = rd.randint(0,10)
            question = print(table, ' X ', random_number, " = ")
            resultats = int(input("Résultat : "))
            total_exo = table * random_number
            self.list_bon_resultat.append({
                "question" : f"{table} X {random_number} = ",
                "resultat" : total_exo
                })
            self.list_resultats_utilisateur.append({
                "question" : f"{table} X {random_number} = ",
                "reponse" : resultats
                })
            

            if resultats == total_exo:
                print("Bonne réponse !\n")
                self.note += 1
            else :
                print("Mauvaise réponse !\n")
                self.list_mauvaise_reponse.append({
                    "question" : f"{table} X {random_number} = ",
                    "resultat" : total_exo
                })
                self.nombre_mauvaise_reponse += 1

        print(f"Vous avez {self.nombre_mauvaise_reponse} mauvaise reponse")
        if self.nombre_mauvaise_reponse > 0 :
            self.rejouer_mauvaise_reponses()
            
        end_time = time.perf_counter()
        time_reflexion = end_time - self.start_time

        self.note_exo()
        
        print(f"Vous avez mis {time_reflexion: .2f} secondes pour faires les calculs")

        
        self.verifier_resultat()

    def exo_toutes_les_tables(self):
        for i in range(10):
            random_number = rd.randint(0,10)
            toutes_table_exo = rd.randint(0,10)
            question = print(toutes_table_exo, ' X ', random_number, " = ")
            resultats = int(input("Résultat : "))
            total_exo = toutes_table_exo * random_number
            self.list_bon_resultat.append({
                "question" : f"{toutes_table_exo} X {random_number} = ",
                "resultat" : total_exo
                })
            self.list_resultats_utilisateur.append({
                "question" : f"{toutes_table_exo} X {random_number} = ",
                "reponse" : resultats
                })
            

            if resultats == total_exo:
                print("Bonne réponse !\n")
                self.note += 1
            else :
                print("Mauvaise réponse !\n")
                self.list_mauvaise_reponse.append({
                    "question" : f"{toutes_table_exo} X {random_number} = ",
                    "resultat" : total_exo
                })
                self.nombre_mauvaise_reponse += 1

            print(f"Vous avez {self.nombre_mauvaise_reponse} mauvaise reponse")

        if self.nombre_mauvaise_reponse > 0 :
            self.rejouer_mauvaise_reponses()


        end_time = time.perf_counter()
        time_reflexion = end_time - self.start_time
        
        self.note_exo()
        print(f"Vous avez mis {time_reflexion: .2f} secondes pour faires les calculs")

        self.verifier_resultat()

    def rejouer_mauvaise_reponses(self):
            while len(self.list_mauvaise_reponse) > 0:
                item = self.list_mauvaise_reponse[0]
                print(item["question"])
                nouveau_resultat = int(input("Résultat : \n"))

                while not nouveau_resultat == item["resultat"]:
                    print("Mauvaise réponse, recommence !\n")
                    print(item["question"])
                    nouveau_resultat = int(input("Résultat : "))
                self.list_mauvaise_reponse.pop(0)
                self.nombre_mauvaise_reponse -= 1

    def note_exo(self):
        print("Vous avez eu ", self.note, "/10 \n")
        if self.note == 10:
            print("Parfait ! Tu maîtrises cette table 💪\n")
        elif self.note >= 7:
            print("Bien joué ! Continue de t’entraîner 👍\n")
        elif self.note >= 5:
            print("Pas mal, mais tu peux faire mieux 🔥\n")
        elif self.note <= 4:
            print("Courage, on révise encore cette table 😅\n")


    def verifier_resultat(self):
        questions_reponse = str(input("Veux-tu revoir toutes les questions avec leurs réponses ? (O/N)"))
        
        if questions_reponse == "o":
            print("Voici les bons résultats : \n")
            for item in self.list_bon_resultat:
                print(item["question"], item["resultat"])
            print("Voici vos réponses : \n")
            for item in self.list_resultats_utilisateur:
                print(item["question"], item["reponse"])
        else:
            exit

        
        
        
        
        
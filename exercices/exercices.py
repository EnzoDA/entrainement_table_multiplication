import random as rd
import time


class Exercice:
    def __init__(self):
        # J’initialise toutes les variables nécessaires pour suivre l’exercice
        self.liste_bons_resultats = []
        self.liste_resultats_utilisateur = []
        self.liste_mauvaises_reponses = []
        self.nombre_mauvaises_reponses = 0
        self.note = 0

        # Je démarre le chrono dès la création de l’exercice
        self.start_time = time.perf_counter()

    @staticmethod
    def table():
        # Je demande à l’utilisateur quelle table il souhaite travailler
        return int(input("Choisis la table : "))
    
    def exo_une_table(self, table):
        # Ici, je fais 10 questions sur une seule table choisie
        for i in range(10):
            random_number = rd.randint(0, 10)

            # J’affiche la question
            print(table, ' X ', random_number, " = ")
            resultat_utilisateur = int(input("Résultat : "))

            # Je calcule le bon résultat
            total_exo = table * random_number

            # Je stocke la question et le bon résultat
            self.liste_bons_resultats.append({
                "question": f"{table} X {random_number} = ",
                "resultat": total_exo
            })

            # Je stocke la réponse de l’utilisateur
            self.liste_resultats_utilisateur.append({
                "question": f"{table} X {random_number} = ",
                "reponse": resultat_utilisateur
            })

            # Je vérifie si la réponse est correcte
            if resultat_utilisateur == total_exo:
                print("Bonne réponse !\n")
                self.note += 1
            else:
                print("Mauvaise réponse !\n")
                self.liste_mauvaises_reponses.append({
                    "question": f"{table} X {random_number} = ",
                    "resultat": total_exo
                })
                self.nombre_mauvaises_reponses += 1

        print(f"Vous avez {self.nombre_mauvaises_reponses} mauvaise(s) réponse(s)")

        # Si l’utilisateur s’est trompé, je lui fais rejouer les mauvaises réponses
        if self.nombre_mauvaises_reponses > 0:
            self.rejouer_mauvaises_reponses()
            
        # Je calcule le temps total de réflexion
        end_time = time.perf_counter()
        temps_reflexion = end_time - self.start_time

        # J’affiche la note finale
        self.note_exo()
        
        print(f"Vous avez mis {temps_reflexion:.2f} secondes pour faire les calculs")

        # Je propose de revoir les questions et réponses
        self.verifier_resultat()

    def exo_toutes_les_tables(self):
        # Ici, je mélange toutes les tables de multiplication
        for i in range(10):
            random_number = rd.randint(0, 10)
            table_aleatoire = rd.randint(0, 10)

            print(table_aleatoire, ' X ', random_number, " = ")
            resultat_utilisateur = int(input("Résultat : "))

            total_exo = table_aleatoire * random_number

            self.liste_bons_resultats.append({
                "question": f"{table_aleatoire} X {random_number} = ",
                "resultat": total_exo
            })

            self.liste_resultats_utilisateur.append({
                "question": f"{table_aleatoire} X {random_number} = ",
                "reponse": resultat_utilisateur
            })

            if resultat_utilisateur == total_exo:
                print("Bonne réponse !\n")
                self.note += 1
            else:
                print("Mauvaise réponse !\n")
                self.liste_mauvaises_reponses.append({
                    "question": f"{table_aleatoire} X {random_number} = ",
                    "resultat": total_exo
                })
                self.nombre_mauvaises_reponses += 1

            print(f"Vous avez {self.nombre_mauvaises_reponses} mauvaise(s) réponse(s)")

        if self.nombre_mauvaises_reponses > 0:
            self.rejouer_mauvaises_reponses()

        end_time = time.perf_counter()
        temps_reflexion = end_time - self.start_time
        
        self.note_exo()
        print(f"Vous avez mis {temps_reflexion:.2f} secondes pour faire les calculs")

        self.verifier_resultat()

    def rejouer_mauvaises_reponses(self):
        # Tant qu’il reste des erreurs, je redemande les questions
        while len(self.liste_mauvaises_reponses) > 0:
            item = self.liste_mauvaises_reponses[0]
            print(item["question"])

            nouveau_resultat = int(input("Résultat : \n"))

            # Je force l’utilisateur à trouver la bonne réponse
            while nouveau_resultat != item["resultat"]:
                print("Mauvaise réponse, recommence !\n")
                print(item["question"])
                nouveau_resultat = int(input("Résultat : "))

            # Une fois la bonne réponse trouvée, je retire l’erreur de la liste
            self.liste_mauvaises_reponses.pop(0)
            self.nombre_mauvaises_reponses -= 1

    def note_exo(self):
        # J’affiche la note finale avec un message adapté
        print("Vous avez eu", self.note, "/10 \n")

        if self.note == 10:
            print("Parfait ! Tu maîtrises cette table 💪\n")
        elif self.note >= 7:
            print("Bien joué ! Continue de t’entraîner 👍\n")
        elif self.note >= 5:
            print("Pas mal, mais tu peux faire mieux 🔥\n")
        else:
            print("Courage, on révise encore cette table 😅\n")

    def verifier_resultat(self):
        # Je propose à l’utilisateur de revoir toutes les questions
        questions_reponse = input(
            "Veux-tu revoir toutes les questions avec leurs réponses ? (O/N) "
        )

        if questions_reponse.lower() == "o":
            print("Voici les bons résultats : \n")
            for item in self.liste_bons_resultats:
                print(item["question"], item["resultat"])

            print("\nVoici vos réponses : \n")
            for item in self.liste_resultats_utilisateur:
                print(item["question"], item["reponse"])
        else:
            exit



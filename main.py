import random as rd
import time



print("1. Révision")
print("2. Exercice")
print("3. Toutes les Tables de multiplications")
print("4. arreter \n")

choix = int(input("Choisi le mode que tu veux : "))

if choix == 1 :
    numero = 0
    sortire = 3
    table_revision = int(input("Quel table veux tu apprendre ? : "))

    print(" 1. apprendre multiplication par multiplication ")
    print(" 2. Voir la table entière ")
    print(" 3. arreter \n")
    choix_revison =int(input("Votre choix : "))
        
    if choix_revison == 1 :
        print("Vous réviser la table du ", table_revision)
        for numero in range(11):
            print(table_revision, " X ", numero, " = ")
            input("Appuie sur Entrée pour voir le résultat")  # autre alternative avec la librairie kayboard     keyboard.wait('enter')
            total = table_revision * numero
            print(" ", total)
                
            
            

    if choix_revison == 2:   
        print("Vous réviser la table du ", table_revision)
        for numero in range(11):
            total = table_revision * numero
            print(table_revision, " X ", numero, " = ", total)

    if choix_revison == 3:
        exit

if choix == 2 : 
    print("1. s'entrainer sur une table ")
    print("2. s'entrainer sur toutes les tables \n")
    choix_exo = int(input("Choisie le mode que tu veux : "))

    if choix_exo == 1:
        table_exo = int(input("Quelle table veut tu ? : "))

        list_bon_resultat = []
        list_resultats_utilisateur = []
        list_mauvaise_reponse = []
        nombre_mauvaise_reponse = 0
        note = 0

        start_time = time.perf_counter()
        for i in range(10):
           
            random_number = rd.randint(0,10)
            question = print(table_exo, ' X ', random_number, " = ")
            resultats = int(input("Résultat : "))
            total_exo = table_exo * random_number
            list_bon_resultat.append({
                "question" : f"{table_exo} X {random_number} = ",
                "resultat" : total_exo
                })
            list_resultats_utilisateur.append({
                "question" : f"{table_exo} X {random_number} = ",
                "reponse" : resultats
                })
            

            if resultats == total_exo:
                print("Bonne réponse !\n")
                note += 1
            else :
                print("Mauvaise réponse !\n")
                list_mauvaise_reponse.append({
                    "question" : f"{table_exo} X {random_number} = ",
                    "resultat" : total_exo
                })
                nombre_mauvaise_reponse += 1

        print(f"Vous avez {nombre_mauvaise_reponse} mauvaise reponse")
        if nombre_mauvaise_reponse > 0 :
            
            while len(list_mauvaise_reponse) > 0:
                item = list_mauvaise_reponse[0]
                print(item["question"])
                nouveau_resultat = int(input("Résultat : \n"))

                while not nouveau_resultat == item["resultat"]:
                    print("Mauvaise réponse, recommence !\n")
                    print(item["question"])
                    nouveau_resultat = int(input("Résultat : "))
                list_mauvaise_reponse.pop(0)
                nombre_mauvaise_reponse -= 1

        end_time = time.perf_counter()
        time_reflexion = end_time - start_time
        print("Vous avez eu ", note, "/10 \n")

        print(f"Vous avez mis {time_reflexion: .2f} secondes pour faires les calculs")

        if note == 10:
            print("Parfait ! Tu maîtrises cette table 💪\n")
        elif note >= 7:
            print("Bien joué ! Continue de t’entraîner 👍\n")
        elif note >= 5:
            print("Pas mal, mais tu peux faire mieux 🔥\n")
        elif note <= 4:
            print("Courage, on révise encore cette table 😅\n")


        questions_reponse = str(input("Veux-tu revoir toutes les questions avec leurs réponses ? (O/N)"))
        
        if questions_reponse == "o":
            print("Voici les bons résultats : \n")
            for item in list_bon_resultat:
                print(item["question"], item["resultat"])
            print("Voici vos réponses : \n")
            for item in list_resultats_utilisateur:
                print(item["question"], item["reponse"])
        else:
            exit
    


    if choix_exo == 2:
        list_bon_resultat = []
        list_resultats_utilisateur = []
        list_mauvaise_reponse = []
        nombre_mauvaise_reponse = 0
        note = 0
        start_time =time.perf_counter()

        for i in range(10):
            random_number = rd.randint(0,10)
            toutes_table_exo = rd.randint(0,10)
            question = print(toutes_table_exo, ' X ', random_number, " = ")
            resultats = int(input("Résultat : "))
            total_exo = toutes_table_exo * random_number
            list_bon_resultat.append({
                "question" : f"{toutes_table_exo} X {random_number} = ",
                "resultat" : total_exo
                })
            list_resultats_utilisateur.append({
                "question" : f"{toutes_table_exo} X {random_number} = ",
                "reponse" : resultats
                })
            

            if resultats == total_exo:
                print("Bonne réponse !\n")
                note += 1
            else :
                print("Mauvaise réponse !\n")
                list_mauvaise_reponse.append({
                    "question" : f"{table_exo} X {random_number} = ",
                    "resultat" : total_exo
                })
                nombre_mauvaise_reponse += 1

            print(f"Vous avez {nombre_mauvaise_reponse} mauvaise reponse")
        if nombre_mauvaise_reponse > 0 :
            
            while len(list_mauvaise_reponse) > 0:
                item = list_mauvaise_reponse[0]
                print(item["question"])
                nouveau_resultat = int(input("Résultat : \n"))

                while not nouveau_resultat == item["resultat"]:
                    print("Mauvaise réponse, recommence !\n")
                    print(item["question"])
                    nouveau_resultat = int(input("Résultat : "))
                list_mauvaise_reponse.pop(0)
                nombre_mauvaise_reponse -= 1


        end_time = time.perf_counter()
        time_reflexion = end_time - start_time
        print("Vous avez eu ", note, "/10 \n")



        print(f"Vous avez mis {time_reflexion: .2f} secondes pour faires les calculs")
        if note == 10:
            print("Parfait ! Tu maîtrises cette table 💪\n")
        elif note >= 7:
            print("Bien joué ! Continue de t’entraîner 👍\n")
        elif note >= 5:
            print("Pas mal, mais tu peux faire mieux 🔥\n")
        elif note <= 4:
            print("Courage, on révise encore cette table 😅\n")
        questions_reponse = str(input("Veux-tu revoir toutes les questions avec leurs réponses ? (O/N)"))
        
        if questions_reponse == "o":
            print("Voici les bons résultats : \n")
            for item in list_bon_resultat:
                print(item["question"], item["resultat"])
            print("Voici vos réponses : \n")
            for item in list_resultats_utilisateur:
                print(item["question"], item["reponse"])
        else:
            exit

if choix == 3:
    table = 0
    numero = 0
    for table in range(11):
        print("Voila la table du ", table , "\n")
        for numero in range(11):
            total = table * numero
            print(table, " X ", numero, " = ", total)
        
if choix == 4:
    exit


import random 
nbre_alea = random.randint(0,9)
print(nbre_alea)
rep_user = None
for i in range(3):

    if rep_user != nbre_alea:
        rep_user = int(input("Entrer un nombre"))
    if rep_user > nbre_alea:
        print("Erreur")
    elif rep_user > nbre_alea:
        print("Erreur essayer à nouveau")
    else:
        print("Félicitation")
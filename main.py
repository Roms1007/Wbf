
liste = {"animaux": ["lion", "dauphin", "chameau", "léopard"],
         "humain": ["Stephane", "Romain", "Kevin", "Alexis", "Toto"], "objet": ["PC", "Stylo", "cahier"]}


def remplacer(key, input, key1, input1):
    liste.pop(key[input])

def remplacermenu():
    flag = True
    while flag :
        print("Que voulez rajouter ?")
        print("1. Un animaux")
        print("2. Un humain")
        print("3. Un objet")
        choix = input()
        match choix:
            case "1":
                print("Quel animal voulez-vous remplacer ?")
                animal = input()
                for i in range (len(liste)):
                    if
                        remplacer(animal, choix)
                    else:
            case "2":
                print("Quel humain souhaitez-vous remplacer ?")
            case "3":
                print("Quel objet voulez-vous remplacer ?")
            case _:
                print("Erreur : commande incorrecte")

print("lol")


# This is a sample Python script.

liste = {"animaux": ["lion", "dauphin", "chameau", "léopard"],
         "humain": ["Stephane", "Romain", "Kevin", "Alexis", "Toto"], "objet": ["PC", "Stylo", "cahier"]}

def menu():
    dico = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1966,
}
    flag = True
    while flag == True:
        print("Bienvenue dans le dictionnaire, que souhaitez vous faire : ")

        print("1 : Ajouter un élément dans le dictionnaire")
        print("2 : Supprimer un élément du dictionnaire")
        print("3 : Modifier un élément du dictionnaire")
        print("4 : Remplacer un élément du dictionaire")
        print("5 : Afficher dictionnaire")
        print("Q : Quitter")
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
        choix = input()

print("lol")

        match choix:
            case "1":
                print("hello")
            case "2":
                supprimer(dico)
            case "3":
                print("hello")
            case "4":
                print("hello")
            case "5":
                afficher(dico)
            case "Q":
                return
            case "p":
                return
            case _:
                print("erreur, entrez une valeur entre 1 et 5, ou entrez Q pour quitter")
                return menu()

def main():
    menu()

if __name__ == '__main__':
    main()

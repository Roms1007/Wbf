# This is a sample Python script.
#salut c est medhi ^^


def menuAjouterMot(list):
    print("Menu pour l'ajout d'un mot, que souhaitez vous faire ?")
    print("1 : Ajouter un mot ")
    print("2 : Retourner au menu principale")
    confirm = input()
    match confirm:
        case "1":
            mot = input("Quel mot ? ")
            type = input("Classe de mot ( Nom, Adjectif, Verbe, Adverbe, Déterminant, Pronom, Preposiotion, Conjonction, Interjection  ) ? : ")
            type = input()
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

            print("Votre mot est : ", mot)
            print("c'est un ", type)
            print("Confirmez vous la saisie ? oui / non")
            choix = input()
            if choix == "oui":
                list = ajouterMot(mot, type, list)
                return menuAjouterMot(list)
            else:
                print("Retour au menu d'ajout de mot")
                return menuAjouterMot(list)
        case "2":
            print("Retour au menu principale...")
            return menuAjouterMot(list)
        case _:
            print("Erreur de saisie...")
            return menuAjouterMot(list)
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

def main():
    list = ["oui", "non"]
    menuAjouterMot(list)


def main():
    menu()

if __name__ == '__main__':
    main()
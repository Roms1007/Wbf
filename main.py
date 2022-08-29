
def supprimer(dico):
    print("Quel élément du dictionnaire souhaitez vous supprimer ")

def afficher(dico):
    print(dico)
    return menu()

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

        choix = input()

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

def ajouterMot(mot, type):
    list.append([mot, type])
    return list

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


def main():
    list = ["oui", "non"]
    menuAjouterMot(list)


if __name__ == '__main__':
    main()
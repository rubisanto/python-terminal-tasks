def afficher_menu():
    print("Menu principal :")
    print("1. Ajouter une tâche")
    print("2. Modifier une tâche")
    print("3. Supprimer une tâche")
    print("4. Afficher les tâches")
    print("5. Rechercher une tâche")
    print("6. Marquer une tâche comme terminée")
    print("7. Quitter le programme")


def main():
    while True:
        afficher_menu()
        choix = input("Veuillez entrer le numéro de l'option choisie : ")

        if choix == "1":
            # Ajouter une tâche
            pass
        elif choix == "2":
            # Modifier une tâche
            pass
        elif choix == "3":
            # Supprimer une tâche
            pass
        elif choix == "4":
            # Afficher les tâches
            pass
        elif choix == "5":
            # Rechercher une tâche
            pass
        elif choix == "6":
            # Marquer une tâche comme terminée
            pass
        elif choix == "7":
            # Quitter le programme
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()

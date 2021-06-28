"""Menu Tournoi"""
def tournament_menu(list):
    menu1 = input("""
-------- 1. TOURNOI -------
1. Créer un nouveau tournoi
2. Tournoi en cours
3. Liste des tournois
4. Retour

    """)
    list.append(int(menu1))
    return list

"""Menu tournoi création"""
def tournament_menu_create(list):
    menu2 = input("""
-------- 1.1 TOURNOI.CREATION  -------
Voulez-vous créer un tournoi ? O/N

    """)
    if menu2 == "N":
        list.pop()
    else:
        list.pop()
        return list


"""Menu tournoi en cours"""
def tournament_menu_current():
    print(f"""
-------- 1.2  TOURNOI.EN COURS -------
1. Ajouter des joueurs (max {Tournament.limit_players})
2. Entrer les résultats du tour en cours
3. Modifier des résultats
4. Valider tous les résultats et clôturer le tournoi en cours
5. Retour

    """)


"""Menu tournoi en cours ajouter joueurs"""
def tournament_menu_current_add_players():
    print(f"""
-------- 1.2.1 TOURNOI.EN COURS.AJOUTER JOUEURS -------
Veuillez choisir les joueurs à ajouter: (Appuyer sur "Echap" pour revenir au menu) 
{players_list} 

    """)

"""Menu tournoi en cours entrer résultats"""
def tournament_menu_current_new_results():
    print("""
-------- 1.2.2 TOURNOI.EN COURS.AJOUTER RESULTATS  -------
Veuillez entrer les résultats d'un match: (Appuyer sur "Echap" pour revenir au menu) 

    """)

"""Menu tournoi en cours entrer résultats"""
def tournament_menu_current_modify_results():
    print("""
-------- 1.2.3 TOURNOI.EN COURS.MODIFIER RESULTATS  -------
Veuillez choisir les resultats à modifier du tournoi en cours: (Appuyer sur "Echap" pour revenir au menu) 

    """)

"""Menu liste tournois"""
def tournament_menu_list_finished():
    print("""
-------- 1.3 TOURNOI.LISTE  -------
Veuillez trouver ci-dessous la liste des tournois:

    """)

"""Menu tournoi retour"""
def tournament_menu_back(list):
    list.pop()
    list.pop()
    return list


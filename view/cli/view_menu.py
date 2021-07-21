from view.cli.view_match import show_match_current_round


# avoid a wrong input for int data
def menu_input():
    try:
        choice = int(input("Quel est votre choix ?"))
    except ValueError:
        choice = 0
        print("Veuillez entre un chiffre")
    return choice


# check if the input for the menu is in the range of the menu list
def check_input_num(choice, menu_list, input_list):
    if choice in input_list:
        menu_list.append(choice)
    else:
        pass


# check if the answer is Y or N
def check_input_str(choice, menu_list):
    while choice not in ["O", "N"]:
        choice = (input("Veuillez choisir O ou N")).capitalize()
    menu_list.pop()
    return choice


# this is the start menu
def menu_start(tournament_list, round_list, match_list):
    # if no tournament is currently opened no additional display
    if len(tournament_list) == 0 or tournament_list[-1].closed == "Y":
        print("""
Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter des joueurs au tournoi
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    # if the tournament is created but no round has been created yet, it displays the tournament name
    elif len(round_list) == 0:
        print(f"""
----- Tournoi en cours: {tournament_list[-1].name}

Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} joueurs au tournoi \
({len(tournament_list[-1].players)} / {tournament_list[-1].max_players})
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    # if all rounds have been played then new display shows that matches are over
    elif len(match_list) == 0:
        print(f"""
----- Tournoi en cours: {tournament_list[-1].name}
----- Tous les tours ont été joués

Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} \
joueurs au tournoi ({len(tournament_list[-1].players)} / {tournament_list[-1].max_players})
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    # displays the tournament current status
    else:
        print(f"""
----- Tournoi en cours: {tournament_list[-1].name}
----- {round_list[-1].name} en cours
----- Matchs en cours:""")
        show_match_current_round(match_list)
        print(f"""
Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} joueurs au tournoi \
({len(tournament_list[-1].players)} / {tournament_list[-1].max_players})
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")


#   ask user if he does want to create a tournament
def menu_tournament_create(menu_list):
    choice = (input("""
-------- 1. CREATION TOURNOI  -------
Voulez-vous créer un tournoi ? O/N

""")).capitalize()
    choice = check_input_str(choice, menu_list)
    return menu_list, choice


# shows that a tournament is already opened
def menu_tournament_created():
    print("Il y a déjà un tournoi en cours, vous ne pouvez en créer un nouveau qu'après l'avoir clôturé")


# menu display for adding a player in a tournament
def menu_tournament_add_player(menu_list, round_list, tournament_list):
    if len(round_list) == 0:
        print("Veuillez créer un nouveau tournoi")
    else:
        print(f"""
-------- 2.1 AJOUTER JOUEURS AU TOURNOI -------
Veuillez entrer les informations du joueur à ajouter au tournoi {tournament_list[-1].name}:

""")
    menu_list.pop()


# display message that round and matches have been generated
def menu_tournament_new_round(round_list, tournament_list, match_list):
    if len(tournament_list) == 0:
        print("Veuillez créer un nouveau tournoi")
    elif len(tournament_list[-1].players) < tournament_list[-1].max_players:
        print("Veuillez terminer d'ajouter les joueurs")
    elif len(match_list) == 0:
        print(f"""
-------- 2.2 GENERER UN NOUVEAU TOUR -------
Les paires du Round {(len(round_list)) + 1} sont créées""")
    else:
        print("Un tour est déjà en cours, veuillez le clôturer quand il sera terminé")


# show message to enter the score
def menu_enter_score(menu_list):
    print("""
-------- 3.1 ENTRER LES SCORES -------
""")
    menu_list.pop()


# show message that round is closed
def menu_close_round(round_list):
    print(f"""
-------- 3.2 CLOTURER LE TOUR -------
Le Round {len(round_list)} est clôturé
""")


# show message all matchs have been played
def menu_all_match_played(menu_list):
    print("Tous les matchs ont été joués, vous pouvez clôturer le tournoi")
    menu_list.pop()


# ask if user wants to close the tournament
def menu_close_tournament(menu_list, tournament_list, match_list, round_list):
    print("""
-------- 4. CLOTURER LE TOURNOI -------
""")
    if tournament_list[-1].closed == "N" and len(match_list) == 0 and len(round_list) == tournament_list[-1].nbtours:
        choice = (input(f"Voulez_vous clôturer le tournoi {tournament_list[-1].name} ? O/N")).capitalize()
        choice = check_input_str(choice, menu_list)
    elif len(round_list) < tournament_list[-1].nbtours:
        choice = "N"
        print("Le tournoi n'est pas terminé")
    else:
        choice = "N"
        "Vous devez créer un nouveau tournoi"
    return choice, menu_list


# shows message to change palyer rank
def menu_change_player_rank(menu_list):
    print("""
-------- 5. CHANGER CLASSEMENT D'UN JOUEUR -------
""")
    menu_list.pop()
    return menu_list


# shows the reports menu
def menu_reports_start():
    print("""
1. Afficher tous les joueurs par ordre alphabétique
2. Afficher tous les joueurs par classement
3. Afficher tous les joueurs d'un tournoi par ordre alphabétique
4. Afficher tous les joueurs d'un tournoi par classement
5. Afficher tous les tournois
6. Afficher tous les tours d'un tournoi
7. Afficher tous les matchs d'un tournoi
8. Retour
    """)


# shows menu to save load db
def menu_save_load():
    print("""
1. Sauvegarder les données
2. Charger les données
3. Retour
""")


# shows message for saving data
def menu_save(menu_list):
    print("Sauvegarde des données")
    menu_list.pop()


# shows message for loading data
def menu_load(menu_list):
    print("Chargement des données")
    menu_list.pop()

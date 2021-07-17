from view.cli.view_match import show_match_current_round


def menu_input():
    try:
        choice = int(input("Quel est votre choix ?"))
    except ValueError:
        choice = 0
        print("Veuillez entre un chiffre")
    return choice


def menu_start(tournament_list, round_list, match_list):
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

    elif len(round_list) == 0:
        print(f"""
----- Tournoi en cours: {tournament_list[-1].name}

Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter \
{tournament_list[-1].max_players - len(tournament_list[-1].players)} \
joueurs au tournoi \
({len(tournament_list[-1].players)} / {tournament_list[-1].max_players})
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    elif len(match_list) == 0:
        print(f"""
----- Tournoi en cours: {tournament_list[-1].name}
----- Tous les tours ont été joués

Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter \
{tournament_list[-1].max_players - len(tournament_list[-1].players)} \
joueurs au tournoi \
({len(tournament_list[-1].players)} / {tournament_list[-1].max_players})
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    else:
        print(f"""
----- Tournoi en cours: {tournament_list[-1].name}
----- {round_list[-1].name} en cours
----- Matchs en cours:""")
        show_match_current_round(match_list)
        print(f"""
Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter \
{tournament_list[-1].max_players - len(tournament_list[-1].players)} \
joueurs au tournoi \
({len(tournament_list[-1].players)} / {tournament_list[-1].max_players})
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")


def menu_tournament_create(menu_list):
    choice = (input("""
-------- 1. CREATION TOURNOI  -------
Voulez-vous créer un tournoi ? O/N

""")).capitalize()
    while choice not in ["O", "N"]:
        choice = (input("Veuillez choisir O ou N")).capitalize()
    menu_list.pop()
    return menu_list, choice


"""Menu tournament already created"""


def menu_tournament_created():
    print("Il y a déjà un tournoi en cours, "
          "vous ne pouvez en créer un nouveau qu'après l'avoir clôturé")


"""Menu add player to tournament"""


def menu_tournament_add_player(menu_list, tournament_list):
    if len(tournament_list) == 0:
        print("Veuillez créer un nouveau tournoi")
    else:
        print(f"""
-------- 2.1 AJOUTER JOUEURS AU TOURNOI -------
Veuillez entrer les informations du \
joueur à ajouter au tournoi {tournament_list[-1].name}:

""")
    menu_list.pop()


"""Menu new round"""


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
        print("Un tour est déjà en cours, "
              "veuillez le clôturer quand il sera terminé")


"""Menu entrer score"""


def menu_enter_score(menu_list):
    print("""
-------- 3.1 ENTRER LES SCORES -------
""")
    menu_list.pop()


def menu_close_round(round_list):
    print(f"""
-------- 3.2 CLOTURER LE TOUR -------
Le Round {len(round_list)} est clôturé
""")


def menu_all_match_played(menu_list):
    print("Tous les matchs ont été joués, vous pouvez clôturer le tournoi")
    menu_list.pop()


def menu_close_tournament(menu_list, tournament_list, match_list, round_list):
    print("""
-------- 4. CLOTURER LE TOURNOI -------
""")
    if tournament_list[-1].closed == "N" \
            and len(match_list) == 0 \
            and len(round_list) == tournament_list[-1].nbtours:
        choice = input(f"Voulez_vous clôturer le tournoi "
                       f"{tournament_list[-1].name} ? O/N")
    else:
        choice = "N"
        "Vous devez créer un nouveau tournoi"
    menu_list.pop()
    return choice, menu_list


def menu_change_player_rank(menu_list):
    print("""
-------- 5. CHANGER CLASSEMENT D'UN JOUEUR -------
""")
    menu_list.pop()
    return menu_list


def menu_reports_start(menu_list):
    menu6 = input("""
1. Afficher tous les joueurs par ordre alphabétique
2. Afficher tous les joueurs par classement
3. Afficher tous les joueurs d'un tournoi par ordre alphabétique
4. Afficher tous les joueurs d'un tournoi par classement
5. Afficher tous les tournois
6. Afficher tous les tours d'un tournoi
7. Afficher tous les matchs d'un tournoi
8. Retour
    """)
    menu_list.append(int(menu6))


def menu_save_load(menu_list):
    menu7 = input("""
1. Sauvegarder les données
2. Charger les données
3. Retour
""")
    menu_list.append(int(menu7))


def menu_save(menu_list):
    print("Sauvegarde des données")
    menu_list.pop()


def menu_load(menu_list):
    print("Chargement des données")
    menu_list.pop()

from view.cli.view_match import show_match_current_round

"""Chess drawing launch"""
def show_logo():
    print("""                                    =||=
                                 o   |\ ,'`. /||\ ,'`. /|    o
         _   _   _   |\__      /\^/\ | `'`'`' || `'`'`' |  /\^/\   |\__     _   _   _
        | |_| |_| | /   o\__  |  /  ) \      /  \      /  |  /  ) /   o\__ | |_| |_| |
         \       / |    ___=' | /  /   |    |    |    |   | /  / |    ___=' \       /
          |     |  |    \      Y  /    |    |    |    |    Y  /  |    \      |     |
          |     |   \    \     |  |    |    |    |    |    |  |   \    \     |     |
          |     |    >    \    |  |    |    |    |    |    |  |    >    \    |     |
         /       \  /      \  /    \  /      \  /      \  /    \  /      \  /       |
        |_________||________||______||________||________||______||________||_________|
            __         __       __       __        __       __       __         __
           (  )       (  )     (  )     (  )      (  )     (  )     (  )       (  )
            ><         ><       ><       ><        ><       ><       ><         ><
           |  |       |  |     |  |     |  |      |  |     |  |     |  |       |  |
          /    \     /    \   /    \   /    \    /    \   /    \   /    \     /    |
         |______|   |______| |______| |______|  |______| |______| |______|   |______|
        
                            CHESS TOURNAMENT V1.0""")


"""Start Menu"""
def menu_start(list, tournament_list, round_list, match_list):
    if len(tournament_list) == 0 or tournament_list[-1].closed == "Y":
        menu0 = input("""        
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
        menu0 = input(f"""
----- Tournoi en cours: {tournament_list[-1].name}

Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} joueurs au tournoi ({len(tournament_list[-1].players)} / {tournament_list[-1].max_players}) 
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    elif len(match_list) == 0:
        menu0 = input(f"""
----- Tournoi en cours: {tournament_list[-1].name}
----- Tous les tours ont été joués

Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} joueurs au tournoi ({len(tournament_list[-1].players)} / {tournament_list[-1].max_players}) 
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
----- Matchs en cours:""" )
        show_match_current_round(match_list)
        menu0 = input(f"""
Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} joueurs au tournoi ({len(tournament_list[-1].players)} / {tournament_list[-1].max_players}) 
3. Entrer les scores
4. Clôturer le tournoi
5. Changer le classement d'un joueur
6. Rapports
7. Sauvegarder/Charger
8. Quitter
""")
    if int(menu0) in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        list.append(int(menu0))
    else:
        pass
    return list

"""Menu new tournament"""
def menu_tournament_create(list):
    choice = input("""
-------- 1. CREATION TOURNOI  -------
Voulez-vous créer un tournoi ? O/N

""")
    list.pop()
    return list, choice

"""Menu tournament already created"""
def menu_tournament_created():
    print("Il y a déjà un tournoi en cours, vous ne pouvez en créer un nouveau qu'après l'avoir clôturé")

"""Menu add player to tournament"""
def menu_tournament_add_player(list, tournament_list):
    if len(tournament_list) == 0:
        print("Veuillez créer un nouveau tournoi")
    else:
        print(f"""
-------- 2.1 AJOUTER JOUEURS AU TOURNOI -------
Veuillez entrer les informations du joueur à ajouter au tournoi {tournament_list[-1].name}: 

""")
    list.pop()
    return list

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
        print("Un tour est déjà en cours, veuillez le clôturer quand il sera terminé")


"""Menu entrer score"""
def menu_enter_score(list):
    print(f"""
-------- 3.1 ENTRER LES SCORES -------
""")
    list.pop()
    return list

def menu_close_round(round_list):
    print(f"""
-------- 3.2 CLOTURER LE TOUR -------
Le Round {len(round_list)} est clôturé
""")


def menu_all_match_played(list):
    print("Tous les matchs ont été joués, vous pouvez clôturer le tournoi")
    list.pop()
    return list

def menu_close_tournament(list, tournament_list, match_list, round_list):
    print("""
-------- 4. CLOTURER LE TOURNOI -------
""")
    if tournament_list[-1].closed == "N" and len(match_list) == 0 and len(round_list) == tournament_list[-1].nbtours:
        choice = input(f"Voulez_vous clôturer le tournoi {tournament_list[-1].name} ? O/N")
    else:
        choice = "N"
        "Vous devez créer un nouveau tournoi"
    list.pop()
    return choice, list

def menu_change_player_rank(list):
    print("""
-------- 5. CHANGER CLASSEMENT D'UN JOUEUR -------    
""")
    list.pop()
    return list

def menu_reports_start(list):
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
    list.append(int(menu6))
    return list

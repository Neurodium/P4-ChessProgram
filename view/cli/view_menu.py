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
        
                            CHESS TOUNRNAMENT V1.0""")


"""Start Menu"""
def menu_start(list, tournament_list):
    if len(tournament_list) == 0:
        menu0 = input("""        
Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter des joueurs au tournoi
3. Générer un nouveau tour
4. Sauvegarder/Charger
5. Quitter
""")

    else:
        menu0 = input(f"""
Que souhaitez-vous faire ?
1. Créer un tournoi
2. Ajouter {tournament_list[-1].max_players - len(tournament_list[-1].players)} joueurs au tournoi ({len(tournament_list[-1].players)} / {tournament_list[-1].max_players}) 
3. Générer un nouveau tour
4. Sauvegarder/Charger
5. Quitter
""")
    list.append(int(menu0))
    return list

"""Menu new tournament"""
def menu_tournament_create(list):
    choice = input("""
-------- 1. CREATION TOURNOI  -------
Voulez-vous créer un tournoi ? O/N

""")
    if choice == "N":
        list.pop()
    else:
        list.pop()
    return list, choice

"""Menu add player to tournament"""
def menu_tournament_add_player(list, tournament_list):
    if len(tournament_list) == 0:
        print("Veuillez créer un nouveau tournoi")
    else:
        print(f"""
-------- 2. AJOUTER JOUEURS AU TOURNOI -------
Veuillez entrer les informations du joueur à ajouter au tournoi {tournament_list[-1].name}: 

""")
    list.pop()
    return list

"""Menu new round"""
def menu_tournament_new_round(list, round_list, tournament_list):
    if len(tournament_list) == 0:
        print("Veuillez créer un nouveau tournoi")
    elif round_list[-1].closed == "N":
        print("Un tour est déjà en cours, veuillez le clôturer quand il sera terminé")
    else:
        print(f"""
-------- 3. GENERER UN NOUVEAU TOUR -------
Les paires du Round {(len(round_list))+1} vont être créées""")
    list.pop()
    return list

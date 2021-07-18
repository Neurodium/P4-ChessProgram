import pandas as pd


def show_player_list_name(menu_list, player_list):
    player_list = sorted(player_list, key=lambda player: player.last_name)
    player_array = []
    for player in player_list:
        player_array.append([player.last_name,
                             player.first_name,
                             player.birthdate,
                             player.gender,
                             player.rank,
                             player.tournament_points])
    player_df = pd.DataFrame(data=player_array,
                             columns=["Nom de Famille",
                                      "Prénom",
                                      "Date de Naissance",
                                      "Sexe",
                                      "Classement",
                                      "Points"])
    print(player_df.to_string(index=False))
    menu_list.pop()


def show_player_list_rank(menu_list, player_list):
    player_list = sorted(player_list, key=lambda player: player.rank)
    player_array = []
    for player in player_list:
        player_array.append([player.rank,
                             player.tournament_points,
                             player.last_name,
                             player.first_name,
                             player.birthdate,
                             player.gender])
    player_df = pd.DataFrame(data=player_array,
                             columns=["Classement",
                                      "Points",
                                      "Nom de Famille",
                                      "Prénom",
                                      "Date de Naissance",
                                      "Sexe"])
    print(player_df.to_string(index=False))
    menu_list.pop()


def show_player_tournament_list_name(menu_list, tournament_list):
    for tournament in tournament_list:
        print(f"Tournoi: {tournament.name}")
    tournament_name = input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")
    player_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            player_list = sorted(tournament.players,
                                 key=lambda player: player.last_name)
            for player in player_list:
                player_array.append([player.last_name,
                                     player.first_name,
                                     player.birthdate,
                                     player.gender,
                                     player.rank,
                                     player.tournament_points])
    player_df = pd.DataFrame(data=player_array,
                             columns=["Nom de Famille",
                                      "Prénom",
                                      "Date de Naissance",
                                      "Sexe",
                                      "Classement",
                                      "Points"])
    print(player_df.to_string(index=False))
    menu_list.pop()


def show_player_tournament_list_rank(menu_list, tournament_list):
    for tournament in tournament_list:
        print(f"Tournoi: {tournament.name}")
    tournament_name = input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")
    player_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            player_list = sorted(tournament.players,
                                 key=lambda player: player.rank)
            for player in player_list:
                player_array.append([player.rank,
                                     player.tournament_points,
                                     player.last_name,
                                     player.first_name,
                                     player.birthdate,
                                     player.gender])
    player_df = pd.DataFrame(data=player_array,
                             columns=["Classement",
                                      "Points",
                                      "Nom de Famille",
                                      "Prénom",
                                      "Date de Naissance",
                                      "Sexe"])
    print(player_df.to_string(index=False))
    menu_list.pop()

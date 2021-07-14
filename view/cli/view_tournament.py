import pandas as pd

"""View all tournaments"""
def view_tournaments_all(list, tournament_list):
    tournament_list = sorted(tournament_list, key=lambda tournament: tournament.name)
    tournament_array = []
    for tournament in tournament_list:
        tournament_array.append([tournament.name, tournament.place, tournament.date, tournament.nbtours, tournament.max_players, tournament.time_control])
    tournament_df = pd.DataFrame(data=tournament_array, columns=["Nom", "Lieu", "Date", "Nb Tours", "Nb Joueurs", "Contrôle du Temps"])
    print(tournament_df.to_string(index=False))
    list.pop()
    return list

def view_tournament_all_rounds(list, tournament_list):
    for tournament in tournament_list:
        print(f"Tournoi: {tournament.name}")
    tournament_name = input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")
    round_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            for round in tournament.rounds:
                round_array.append([round.name, round.date_begin.strftime("%d/%m/%Y (%H:%M:%S)"), round.date_end.strftime("%d/%m/%Y (%H:%M:%S)")])
            round_df = pd.DataFrame(data=round_array, columns=["Nom", "Date début", "Date fin"])
            print(round_df.to_string(index=False))
        else:
            print("Ce tournoi n'existe pas")

    list.pop()
    return list

def view_tournament_all_matchs(list, tournament_list):
    for tournament in tournament_list:
        print(f"Tournoi: {tournament.name}")
    tournament_name = input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")
    match_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            for round in tournament.rounds:
                for match in round.matchs_round:
                    match_array.append([match.players[0].last_name, match.players[0].first_name, "contre", match.players[1].last_name, match.players[1].first_name, match.score[0], "-", match.score[1]])
            match_df = pd.DataFrame(data=match_array,
                                columns=["Joueur 1", "", "", "Joueur 2", "", "Score 1", "-", "Score 2"])
            print(match_df.to_string(index=False))
        else:
            print("Ce tournoi n'existe pas")

    list.pop()
    return list




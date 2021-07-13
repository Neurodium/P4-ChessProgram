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
    print(view_tournaments_all(list, tournament_list))
    tournament_name = input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")
    round_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            for round in tournament.rounds:
                round_array.append([round.name, round.date_begin, round.date_end])
        else:
            print("Ce tournoi n'existe pas")
    round_df = pd.DataFrame(data=round_array, columns=["Nom", "Date début", "Date fin"])
    print(round_df.to_string(index=False))
    list.pop()
    return list





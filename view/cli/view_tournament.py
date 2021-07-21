import pandas as pd


# view the list of tournaments
def view_tournaments_all(menu_list, tournament_list):
    tournament_list = sorted(tournament_list,
                             key=lambda tournament: tournament.name)
    tournament_array = []
    for tournament in tournament_list:
        tournament_array.append([tournament.name,
                                 tournament.place,
                                 tournament.date,
                                 tournament.nbtours,
                                 tournament.max_players,
                                 tournament.time_control])
    # use dataframe to show the list of tournaments
    tournament_df = pd.DataFrame(data=tournament_array,
                                 columns=["Nom",
                                          "Lieu",
                                          "Date",
                                          "Nb Tours",
                                          "Nb Joueurs",
                                          "Contrôle du Temps"])
    print(tournament_df.to_string(index=False))
    menu_list.pop()


# shows the list of rounds of a tournament
def view_tournament_all_rounds(menu_list, round_list, tournament_list):
    for tournament in tournament_list:
        print(f"Tournoi: {tournament.name}")
    tournament_name = (input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")).capitalize()
    round_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            # if tournament is not over shows the current rounds
            if tournament.rounds == []:
                for round in round_list:
                    round_array.append([round.name,
                                        round.date_begin.strftime("%d/%m/%Y (%H:%M:%S)"),
                                        round.date_end.strftime("%d/%m/%Y (%H:%M:%S)")])
            # if the tournament is over shows the history of tournament
            else:
                for round in tournament.rounds:
                    round_array.append([round.name,
                                        round.date_begin.strftime("%d/%m/%Y (%H:%M:%S)"),
                                        round.date_end.strftime("%d/%m/%Y (%H:%M:%S)")])
            # use dataframe to show the list of rounds
            round_df = pd.DataFrame(data=round_array,
                                    columns=["Nom",
                                             "Date début",
                                             "Date fin"])
            print(round_df.to_string(index=False))
        else:
            print("Ce tournoi n'existe pas")
    menu_list.pop()


# show the list of matches of a tournament
def view_tournament_all_matchs(menu_list, round_list, tournament_list):
    for tournament in tournament_list:
        print(f"Tournoi: {tournament.name}")
    tournament_name = (input("Veuillez entrer le nom du tournoi que vous souhaitez consulter")).capitalize()
    match_array = []
    for tournament in tournament_list:
        if tournament_name == tournament.name:
            if tournament.rounds == []:
                # check if the first round has been played
                if round_list[0].matchs_round == []:
                    print("Le round 1 n'est pas terminé")
                # shows the list of matches played
                else:
                    for round in round_list:
                        for match in round.matchs_round:
                            match_array.append([round.name,
                                                match.name,
                                                match.players[0].last_name,
                                                match.players[0].first_name,
                                                "contre",
                                                match.players[1].last_name,
                                                match.players[1].first_name,
                                                match.score[0],
                                                "-",
                                                match.score[1]])
                    # use a dataframe to shows the list of matches
                    match_df = pd.DataFrame(data=match_array,
                                            columns=["Round",
                                                     "Match",
                                                     "Joueur 1",
                                                     "",
                                                     "",
                                                     "Joueur 2",
                                                     "",
                                                     "Score 1",
                                                     "-",
                                                     "Score 2"])
                    print(match_df.to_string(index=False))
            else:
                for round in tournament.rounds:
                    # shows the list of rounds of tournament that is finished
                    for match in round.matchs_round:
                        match_array.append([round.name,
                                            match.name,
                                            match.players[0].last_name,
                                            match.players[0].first_name,
                                            "contre",
                                            match.players[1].last_name,
                                            match.players[1].first_name,
                                            match.score[0],
                                            "-",
                                            match.score[1]])
                # use a dataframe to shows the list of matches
                match_df = pd.DataFrame(data=match_array,
                                        columns=["Round",
                                                 "Match",
                                                 "Joueur 1",
                                                 "",
                                                 "",
                                                 "Joueur 2",
                                                 "",
                                                 "Score 1",
                                                 "-",
                                                 "Score 2"])
                print(match_df.to_string(index=False))
        else:
            print("Ce tournoi n'existe pas")

    menu_list.pop()

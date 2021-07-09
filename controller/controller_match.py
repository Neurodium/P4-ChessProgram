from model.match import Match
from controller.controller_player import find_player_previous_match

"""Attribution des matchs"""
def match_first_round(tournament_list, round_list, match_list):
    if len(match_list) == 0 and len(round_list) == 1:
        players_match = tournament_list[-1].players
        players_match = sorted(players_match, key=lambda player: player.rank)
        half_list = int(len(players_match)/2)
        for player in range(half_list):
            match_list.append(Match((players_match[player], players_match[player + half_list])))
        round_list[-1].matchs_round = match_list
    else:
        pass
    return match_list, round_list, tournament_list

def match_next_round(tournament_list, round_list, match_list):
    if len(match_list) == 0:
        players_match = tournament_list[-1].players
        players_match = sorted(players_match, key=lambda player: (player.tournament_points, player.rank), reverse=True)
        if find_player_previous_match(players_match, round_list) == False:
            player = 0
            while player < len(players_match):
                match_list.append(Match((players_match[player], players_match[player + 1])))
                player += 2
            round_list[-1].matchs_round = match_list
        else:
            match_list.append(Match((players_match[0], players_match[2])))
            match_list.append(Match((players_match[1], players_match[3])))
            player = 4
            while player < len(players_match):
                match_list.append(Match((players_match[player], players_match[player+1])))
                player += 2
            round_list[-1].matchs_round = match_list
    else:
        pass
    return tournament_list, round_list, match_list

def enter_match_score(match_list, round_list, tournament_list):
    """    for match in range(len(match_list)):
        answer = input(f"Voulez-vous entrer les scores pour le Match {match + 1} ? O/N")
        if answer == "O":
            score_1 = float(input(f"Score de {match_list[match].players[0].last_name} {match_list[match].players[0].first_name} (0 / 0.5 / 1): "))
            score_2 = float(input(f"Score de {match_list[match].players[1].last_name} {match_list[match].players[1].first_name} (0 / 0.5 / 1): "))
            if score_1 + score_2 == 1.0:
                match_list[match].score = [score_1, score_2]
            else:
                print("Le score est incorrect")"""
    match_list[0].score = [1, 0]
    match_list[1].score = [0.5, 0.5]
    match_list[2].score = [0, 1]
    match_list[3].score = [1, 0]
    round_list[-1].matchs_round = match_list
    return match_list, round_list, tournament_list
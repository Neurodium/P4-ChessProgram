from model.round import Round
from datetime import datetime

"""Round initialization"""
def add_new_round(round_list, tournament_list, match_list):
    if len(tournament_list) == 0:
        pass
    elif len(tournament_list[-1].players) == 0:
        pass
    elif len(match_list) == 0:
        nb_round = len(round_list)
        round_list.append(Round(f"Round {nb_round + 1}", datetime.now, []))
        return round_list

def check_match_points(match_list):
    total_points = 0
    for i in range(len(match_list)):
        total_points += match_list[i].score[0]
        total_points += match_list[i].score[1]
    if total_points == float(len(match_list)):
        return True

def close_round(match_list, tournament_list, round_list):
    for match in range(len(match_list)):
        for i in range(len(tournament_list[-1].players)):
            if match_list[match].players[0].last_name == tournament_list[-1].players[i].last_name and match_list[match].players[0].first_name == tournament_list[-1].players[i].first_name:
                tournament_list[-1].players[i].tournament_points += match_list[match].score[0]
            elif match_list[match].players[1].last_name == tournament_list[-1].players[i].last_name and match_list[match].players[1].first_name == tournament_list[-1].players[i].first_name:
                tournament_list[-1].players[i].tournament_points += match_list[match].score[1]
        round_list[-1].matchs_round.append(match_list[match])
    match_list[:] = []
    round_list[-1].date_end = datetime.now
    return match_list, tournament_list, round_list




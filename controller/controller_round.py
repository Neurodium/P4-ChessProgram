from model.round import Round
import datetime


"""Round initialization"""


def add_new_round(round_list, tournament_list, match_list):
    if len(tournament_list) == 0:
        pass
    elif len(tournament_list[-1].players) == 0:
        pass
    elif len(match_list) == 0:
        nb_round = len(round_list)
        round_list.append(Round(f"Round {nb_round + 1}",
                                datetime.datetime.now(),
                                []))
        return round_list


def check_match_points(match_list):
    total_points = 0
    for match in match_list:
        total_points += match.score[0]
        total_points += match.score[1]
    if total_points == float(len(match_list)):
        return True


def close_round(match_list, tournament_list, round_list):
    for match in match_list:
        for player in tournament_list[-1].players:
            if match.players[0].last_name == player.last_name and match.players[0].first_name == player.first_name:
                player.tournament_points += match.score[0]
            elif match.players[1].last_name == player.last_name and match.players[1].first_name == player.first_name:
                player.tournament_points += match.score[1]
        round_list[-1].matchs_round.append(match)
    match_list[:] = []
    round_list[-1].date_end = datetime.datetime.now()

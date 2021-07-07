from model.round import Round
from datetime import datetime

"""Round initialization"""
def add_new_round(round_list, tournament_list):
    if len(tournament_list) == 0:
        pass
    elif len(tournament_list[-1].players) == 0:
        pass
    elif len(round_list) == 0 or round_list[-1].closed == "Y":
        nb_round = len(round_list)
        round_list.append(Round(f"Round {nb_round + 1}", datetime.now))
        tournament_list[-1].rounds = round_list
        return round_list, tournament_list
    elif round_list[-1].closed == "N":
        pass



from model.round import Round

"""Round initialization"""
def add_new_round(round_list, tournament_list):
    if len(tournament_list) == 0:
        pass
    elif round_list[-1].closed == "N":
        pass
    else:
        nb_round = len(round_list)
        round_list[nb_round] = Round(f"Round {nb_round + 1}", datetime.now)
        tournament_list[-1].rounds = round_list
        return round_list, tournament_list


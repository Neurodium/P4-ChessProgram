"""Attribution des matchs"""
def match_round_1(tournament_list):
    if len(tournament_list) != 0:
        tournament_list[-1].players = sorted(tournament_list[-1].players, key=lambda tournament_list[-1].players: player.rank)
        match_list = []
        half_list = int(len(tournament_list[-1].players)/2)
        for i in range(half_list):
            match_list.append((tournament_list[-1].players[i], tournament_list[-1].players[i + half_list]))
        return match_list
    else:
        pass

def match_round_2(tournament_list):
    if len(tournament_list) != 0:
        tournament_list[-1].players = sorted(tournament_list[-1].players, key=lambda player: (player.tournament_points, player.rank))
        match_list = []
        half_list = int(len(tournament_list[-1].players)/2)
        for i in range(half_list):
            match_list.append((tournament_list[-1].players[i], tournament_list[-1].players[i+1]))
            i += 1
            return match_list
    else:
        pass
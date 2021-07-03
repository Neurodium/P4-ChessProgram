"""Attribution des matchs"""
def match_round_1(player_list):
    player_list = sorted(player_list, key=lambda player: player.rank)
    match_list = []
    half_list = int(len(player_list)/2)
    for player in range(half_list):
        match_list.append((player_list[player], player_list[player + half_list]))
    return match_list

def match_round_2(player_list):
    player_list = sorted(player_list, key=lambda player: (player.tournament_points, player.rank))
    match_list = []
    half_list = int(len(player_list)/2)
    for player in range(half_list):
        match_list.append((player_list[player], player_list[player+1]))
        player += 1
        return match_list

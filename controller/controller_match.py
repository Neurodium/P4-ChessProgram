"""Attribution des matchs"""
def match_round_1(player_list):
    player_list = sorted(player_list, key=lambda player: player.rank)
    for player in range(len(player_list)):
        match_list = [(player_list[0], player_list[4]),
                      (player_list[1], player_list[5]),
                      (player_list[2], player_list[6]),
                      (player_list[3], player_list[7]))
        return match_list

def match_round_2(player_list):
    player_list = sorted(player_list, key=lambda player: (player.tournament_points, player.rank))
    for player in range(len(player_list)):
        match_list = [(player_list[0], player_list[1]),
                      (player_list[2], player_list[3]),
                      (player_list[4], player_list[5]),
                      (player_list[6], player_list[7]))
        return match_list

def match_round_3(player_list):
    for player in range(len(player_list)):
        match_list = [(player_list[0], player_list[1]),
                      (player_list[2], player_list[3]),
                      (player_list[4], player_list[5]),
                      (player_list[6], player_list[7]))
        return match_list

for i in range(len(player_list)):
    if player_list[i]
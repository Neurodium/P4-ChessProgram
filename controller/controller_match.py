"""Attribution des matchs"""
def match_first_round(list, tournament_list):
    if len(tournament_list) == 0:
        pass
    else:
        players_match = tournament_list[-1].players
        players_match = sorted(players_match, key=lambda player: player.rank)
        print(players_match)
        match_list = []
        half_list = int(len(players_match)/2)
        print(half_list)
        for player in range(half_list):
            match_list.append((players_match[player], players_match[player + half_list]))
    list.pop()
    print(match_list)
    return match_list

def match_next_round(player_list):
    player_list = sorted(player_list, key=lambda player: (player.tournament_points, player.rank))
    match_list = []
    half_list = int(len(player_list)/2)
    for player in range(half_list):
        match_list.append((player_list[player], player_list[player+1]))
        player += 1
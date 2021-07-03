def show_player_list_name(player_list):
    player_list = sorted(player_list, key=lambda player: player.last_name)
    print("Last Name, First Name, Birthdate, Gender, Rank" )
    for player in range(len(player_list)):
        print(f"{player_list[player].last_name}, "
              f"{player_list[player].first_name}, "
              f"{player_list[player].birthdate}, "
              f"{player_list[player].gender}, "
              f"{player_list[player].rank}"
              )

def show_player_list_rank(player_list):
    player_list = sorted(player_list, key=lambda player: player.rank)
    print("Last Name, First Name, Birthdate, Gender, Rank")
    for player in range(len(player_list)):
        print(f"{player_list[player].last_name}, "
              f"{player_list[player].first_name}, "
              f"{player_list[player].birthdate}, "
              f"{player_list[player].gender}, "
              f"{player_list[player].rank}"
              )


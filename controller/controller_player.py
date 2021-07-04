from model.player import Player
from datetime import datetime

def add_player(tournament_list, player_list):
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    date = input("Date de naissance (JJ/MM/AAAA): ")
    gender = input("Genre (M/F): ")
    player = Player(last_name, first_name, date, gender)
    if len(tournament_list[-1].players) == 0 or player.last_name not in tournament_list[-1].players.last_name:
        tournament_list[-1].players.append(player)
        if player.last_name in player_list[0].last_name:
            pass
        else:
            player_list.append(player)
    else:
        print(f"Le joueur est déjà dans le tournoi {tournament_list[-1].name}")
        pass

    return player_list, tournament_list


from model.player import Player
from datetime import datetime

def add_player(tournament_list, player_list):
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    date = input("Date de naissance (JJ/MM/AAAA): ")
    gender = input("Genre (M/F): ")
    player = Player(last_name, first_name, date, gender)
    if player in tournament_list[-1].players:
        print(f"Le joueur est déjà dans le tournoi {tournament_list[-1].name}")
        pass
    else:
        tournament_list[-1].players.append(player)
        if player in player_list:
            pass
        else:
            player_list.append(player)
    return player_list, tournament_list


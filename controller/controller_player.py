from model.player import Player
from datetime import datetime

def new_player(player_list):
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    date = input("Date de naissance (JJ/MM/AAAA): ")
    gender = input("Genre (M/F): ")
    rank = int(input("Rank ?"))
    player = Player(last_name, first_name, date, gender, rank)
    player_list.append(player)
    return player_list


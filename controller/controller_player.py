from model.player import Player
from datetime import datetime

def new_player(player_list):
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    date = input("Date de naissance (JJ/MM/AAAA): ")
    sex = input("Sexe (M/F): ")
    rank = int(input("Rank ?"))
    player = Player(last_name, first_name, date, sex, rank)
    player_list.append(player)
    return player_list


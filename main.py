from datetime import datetime
from controller.controller_player import new_player
from view.cli.view_player import show_player_list_rank
from model.player import Player
from helpers import menu_navigation


menu = []
players = []
tournament = []

"""new_player(players)
new_player(players)
print(players)
show_player_list_rank(players)"""



while menu != [5]:
    menu_navigation(menu, tournament, players)

print(tournament[0].name)


print("Au revoir !")

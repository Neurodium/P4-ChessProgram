from datetime import datetime
from controller.controller_player import new_player
from controller.controller_match import match_round_1
from view.cli.view_player import show_player_list_rank
from view.cli.view_match import show_match_current_round
from model.player import Player
from helpers import menu_navigation


menu = []
players = []
tournament = []

players = [Player("CRETENET", "Julien", "03/05/1983", "M", rank=0, tournament_points=0),
            Player("DE ANDRADE", "Laurie", "03/04/1987", "F", rank=0, tournament_points=0),
            Player("TUIL", "Laurent", "19/11/1973", "M", rank=0, tournament_points=0),
            Player("BRAVARD", "Sophie", "24/06/1977", "F", rank=0, tournament_points=0),
            Player("DERY", "Stephane", "04/09/1971", "M", rank=0, tournament_points=0),
            Player("GABISON", "Marlene", "03/07/1990", "F", rank=0, tournament_points=0),
            Player("JOUVERT", "Nicolas", "08/10/1982", "M", rank=0, tournament_points=0),
            Player("ARGO", "Sandra", "11/11/1991", "F", rank=0, tournament_points=0)
           ]

matchs = match_round_1(players)
show_match_current_round(matchs)


while menu != [5]:
    menu_navigation(menu, tournament, players)

print(tournament[0].name)


print("Au revoir !")

from view.cli.view_menu import show_logo
from helpers import menu_navigation

show_logo()

menu = []
rounds = []
players = []
tournament = []
matchs = []
players = []

while menu != [8]:
    menu_navigation(menu, tournament, players, rounds, matchs)

print("Au revoir !")

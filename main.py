from helpers import menu_navigation


# init lists
menu = []
rounds = []
players = []
tournament = []
matchs = []

# manage menu
while menu != [8]:
    menu_navigation(menu, tournament, players, rounds, matchs)
# leave program
print("Au revoir !")

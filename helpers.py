from view.cli.view_tournament import menu_tournament, menu_tournament_back, menu_tournament_create, menu_tournament_current, menu_tournament_add_player
from view.cli.view_menu import menu_start
from controller.controller_tournament import create_tournament
from controller.controller_player import add_player

def menu_navigation(list, tournament_list, player_list):
    if list == []:
        menu_start(list)
    elif list == [1]:
        menu_tournament(list)
    elif list == [1, 1]:
        list, choice = menu_tournament_create(list)
        if choice == "O":
            create_tournament(tournament_list)
    elif list == [1, 2]:
        menu_tournament_current(list, tournament_list)
    elif list == [1, 2, 1]:
        menu_tournament_add_player(list)
        add_player(tournament_list, player_list)
        print(tournament_list[-1].players)
        print(player_list)
    elif list == [1, 4]:
        menu_tournament_back(list)

from view.cli.view_tournament import tournament_menu, tournament_menu_back, tournament_menu_create
from view.cli.view_menu import start_menu
from controller.controller_tournament import create_tournament

def menu_navigation(list, tournament_list, player_list):
    if list == []:
        start_menu(list)
    elif list == [1]:
        tournament_menu(list)
    elif list == [1, 1]:
        tournament_menu_create(list)
        create_tournament(tournament_list)
    elif list == [1, 4]:
        tournament_menu_back(list)

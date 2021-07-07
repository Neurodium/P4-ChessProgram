from view.cli.view_tournament import menu_tournament_back
from view.cli.view_menu import menu_start, menu_tournament_create, menu_tournament_add_player, menu_tournament_new_round
from view.cli.view_match import show_match_current_round
from controller.controller_tournament import create_tournament
from controller.controller_player import add_player
from controller.controller_match import match_first_round
from controller.controller_round import add_new_round

def menu_navigation(list, tournament_list, player_list, round_list, match_list):
    if list == []:
        menu_start(list, tournament_list, round_list, match_list)
    elif list == [1]:
        list, choice = menu_tournament_create(list)
        if choice == "O":
            create_tournament(tournament_list)
    elif list == [2]:
        menu_tournament_add_player(list, tournament_list)
        add_player(tournament_list, player_list)
    elif list == [3]:
        menu_tournament_new_round(list, round_list, tournament_list)
        add_new_round(round_list, tournament_list)
        match_first_round(tournament_list, round_list, match_list)
        show_match_current_round(match_list)
    elif list == [1, 4]:
        menu_tournament_back(list)

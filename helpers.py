from view.cli.view_tournament import menu_tournament_back
from view.cli.view_menu import menu_start, menu_tournament_create, menu_tournament_add_player, menu_tournament_new_round, menu_enter_score, menu_close_round
from view.cli.view_match import show_match_current_round
from controller.controller_tournament import create_tournament
from controller.controller_player import add_player
from controller.controller_match import match_first_round, match_next_round, enter_match_score
from controller.controller_round import add_new_round, close_round

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
        menu_tournament_new_round(list, round_list, tournament_list, match_list)
        add_new_round(round_list, tournament_list, match_list)
        if len(round_list) == 1:
            match_first_round(tournament_list, round_list, match_list)
        else:
            match_next_round(tournament_list, round_list, match_list)
    elif list == [4]:
        menu_enter_score(list)
        enter_match_score(match_list, round_list, tournament_list)
    elif list == [5]:
        list, choice = menu_close_round(list)
        if choice == "O":
            close_round(match_list, tournament_list)
            print(tournament_list[-1].players[0].tournament_points)
    elif list == [1, 4]:
        menu_tournament_back(list)

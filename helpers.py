from view.cli.view_tournament import menu_tournament_back
from view.cli.view_menu import menu_start, menu_tournament_create, menu_tournament_add_player, menu_tournament_new_round, menu_enter_score, menu_close_round, menu_all_match_played, menu_close_tournament
from view.cli.view_match import show_match_current_round
from controller.controller_tournament import create_tournament, close_tournament
from controller.controller_player import add_player, update_players_rank, change_player_rank
from controller.controller_match import match_first_round, match_next_round, enter_match_score
from controller.controller_round import add_new_round, close_round, check_match_points

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
        if len(tournament_list[-1].players) == tournament_list[-1].max_players:
            menu_tournament_new_round(round_list, tournament_list, match_list)
            add_new_round(round_list, tournament_list, match_list)
            match_first_round(tournament_list, round_list, match_list)
    elif list == [3]:
        if len(match_list) != 0:
            menu_enter_score(list)
            enter_match_score(match_list, round_list, tournament_list)
            if check_match_points(match_list) == True:
                if len(round_list) < (len(tournament_list[-1].players)-1):
                    menu_close_round(round_list)
                    close_round(match_list, tournament_list, round_list)
                    menu_tournament_new_round(round_list, tournament_list, match_list)
                    add_new_round(round_list, tournament_list, match_list)
                    match_next_round(tournament_list, round_list, match_list)
                else:
                    menu_close_round(round_list)
                    close_round(match_list, tournament_list, round_list)
        else:
            menu_all_match_played(list)
    elif list == [4]:
        choice, list = menu_close_tournament(list, tournament_list, match_list, round_list)
        if choice == "O":
            close_tournament(tournament_list, player_list, round_list)
            update_players_rank(player_list)
            print(round_list)
            print(tournament_list[-1].rounds)
        else:
            pass
    elif list == [5]:
        change_player_rank(player_list)
    elif list == [1, 4]:
        menu_tournament_back(list)

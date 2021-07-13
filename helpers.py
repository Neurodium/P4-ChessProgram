from view.cli.view_menu import menu_start, menu_tournament_create, menu_tournament_add_player, menu_tournament_new_round, \
    menu_enter_score, menu_close_round, menu_all_match_played, menu_close_tournament, menu_tournament_created,menu_reports_start
from view.cli.view_match import show_match_current_round
from view.cli.view_player import show_player_list_name, show_player_list_rank, show_player_tournament_list_name, show_player_tournament_list_rank
from view.cli.view_tournament import view_tournaments_all
from controller.controller_tournament import create_tournament, close_tournament
from controller.controller_player import add_player, update_players_rank, change_player_rank
from controller.controller_match import match_first_round, match_next_round, enter_match_score
from controller.controller_round import add_new_round, close_round, check_match_points

def menu_navigation(list, tournament_list, player_list, round_list, match_list):
    if list == []:
        list = menu_start(list, tournament_list, round_list, match_list)
    elif list == [1]:
        list, choice = menu_tournament_create(list)
        if choice == "O":
            if len(tournament_list) == 0 or tournament_list[-1].closed == "Y":
                tournament_list = create_tournament(tournament_list)
            else:
                menu_tournament_created()
    elif list == [2]:
        list = menu_tournament_add_player(list, tournament_list)
        tournament_list = add_player(tournament_list, player_list)
        if len(tournament_list[-1].players) == tournament_list[-1].max_players:
            menu_tournament_new_round(round_list, tournament_list, match_list)
            round_list = add_new_round(round_list, tournament_list, match_list)
            match_list = match_first_round(tournament_list, round_list, match_list)
    elif list == [3]:
        if len(match_list) != 0:
            list = menu_enter_score(list)
            match_list = enter_match_score(match_list)
            if check_match_points(match_list) == True:
                if len(round_list) < tournament_list[-1].nbtours:
                    menu_close_round(round_list)
                    match_list, tournament_list, round_list = close_round(match_list, tournament_list, round_list)
                    menu_tournament_new_round(round_list, tournament_list, match_list)
                    round_list = add_new_round(round_list, tournament_list, match_list)
                    match_list = match_next_round(tournament_list, round_list, match_list)
                else:
                    menu_close_round(round_list)
                    match_list, tournament_list, round_list = close_round(match_list, tournament_list, round_list)
        else:
            list = menu_all_match_played(list)
    elif list == [4]:
        choice, list = menu_close_tournament(list, tournament_list, match_list, round_list)
        if choice == "O":
            tournament_list, round_list = close_tournament(tournament_list, round_list)
            player_list = update_players_rank(player_list)
        else:
            pass
    elif list == [5]:
        change_player_rank(player_list)
    elif list == [6]:
        list = menu_reports_start(list)
    elif list == [6, 1]:
        list = show_player_list_name(list, player_list)
    elif list == [6, 2]:
        list = show_player_list_rank(list, player_list)
    elif list == [6, 3]:
        list = show_player_tournament_list_name(list, tournament_list)
    elif list == [6, 4]:
        list = show_player_tournament_list_rank(list, tournament_list)
    elif list == [6, 5]:
        list = view_tournaments_all(list, tournament_list)




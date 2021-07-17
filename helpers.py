from view.cli.view_menu import menu_start, \
    menu_tournament_create, menu_tournament_add_player, \
    menu_tournament_new_round, menu_enter_score, \
    menu_close_round, menu_all_match_played, \
    menu_close_tournament, menu_tournament_created,\
    menu_reports_start, menu_save_load, \
    menu_save, menu_load, menu_input
from view.cli.view_player import show_player_list_name, \
    show_player_list_rank, show_player_tournament_list_name, \
    show_player_tournament_list_rank
from view.cli.view_tournament import view_tournaments_all, \
    view_tournament_all_rounds, view_tournament_all_matchs
from controller.controller_tournament import create_tournament, \
    close_tournament
from controller.controller_player import add_player, \
    update_players_rank, change_player_rank
from controller.controller_match import match_first_round, \
    match_next_round, enter_match_score
from controller.controller_round import add_new_round, \
    close_round, check_match_points
from controller.controller_db import save_players, \
    save_tournaments, load_players, \
    load_tournaments, load_players_tournaments, \
    load_rounds_tournaments, load_matchs_tournaments


# manage which page will be displayed
def menu_navigation(menu_list, tournament_list, player_list,
                    round_list, match_list):
    if menu_list is []:
        menu_start(tournament_list, round_list, match_list)
        choice = menu_input()
        if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
            menu_list.append(choice)
        else:
            pass
    elif menu_list is [1]:
        menu_list, choice = menu_tournament_create(menu_list)
        if choice == "O":
            if len(tournament_list) == 0 or tournament_list[-1].closed == "Y":
                create_tournament(tournament_list)
            else:
                menu_tournament_created()
    elif menu_list == [2]:
        menu_tournament_add_player(menu_list, tournament_list)
        tournament_list = add_player(tournament_list, player_list)
        if len(tournament_list[-1].players) == tournament_list[-1].max_players:
            menu_tournament_new_round(round_list,
                                      tournament_list,
                                      match_list)
            round_list = add_new_round(round_list,
                                       tournament_list,
                                       match_list)
            match_first_round(tournament_list,
                              round_list,
                              match_list)
    elif menu_list == [3]:
        if len(match_list) != 0:
            menu_enter_score(menu_list)
            match_list = enter_match_score(match_list)
            if check_match_points(match_list) is True:
                if len(round_list) < tournament_list[-1].nbtours:
                    menu_close_round(round_list)
                    match_list, tournament_list, round_list = close_round(
                        match_list,
                        tournament_list,
                        round_list)
                    menu_tournament_new_round(round_list,
                                              tournament_list,
                                              match_list)
                    round_list = add_new_round(round_list,
                                               tournament_list,
                                               match_list)
                    match_next_round(tournament_list,
                                     round_list,
                                     match_list)
                else:
                    menu_close_round(round_list)
                    close_round(match_list,
                                tournament_list,
                                round_list)
        else:
            menu_all_match_played(menu_list)
    elif menu_list == [4]:
        choice, menu_list = menu_close_tournament(menu_list,
                                                  tournament_list,
                                                  match_list,
                                                  round_list)
        if choice == "O":
            close_tournament(tournament_list,
                             round_list)
            update_players_rank(player_list)
        else:
            pass
    elif menu_list == [5]:
        menu_list, player_list = change_player_rank(menu_list, player_list)
        update_players_rank(player_list)
    elif menu_list == [6]:
        menu_reports_start(menu_list)
    elif menu_list == [6, 1]:
        show_player_list_name(menu_list, player_list)
    elif menu_list == [6, 2]:
        show_player_list_rank(menu_list, player_list)
    elif menu_list == [6, 3]:
        show_player_tournament_list_name(menu_list, tournament_list)
    elif menu_list == [6, 4]:
        show_player_tournament_list_rank(menu_list, tournament_list)
    elif menu_list == [6, 5]:
        view_tournaments_all(menu_list, tournament_list)
    elif menu_list == [6, 6]:
        view_tournament_all_rounds(menu_list, tournament_list)
    elif menu_list == [6, 7]:
        view_tournament_all_matchs(menu_list, tournament_list)
    elif menu_list == [6, 8]:
        menu_list.pop()
        menu_list.pop()
    elif menu_list == [7]:
        menu_save_load(menu_list)
    elif menu_list == [7, 1]:
        menu_save(menu_list)
        save_players(player_list)
        save_tournaments(tournament_list)
    elif menu_list == [7, 2]:
        menu_load(menu_list)
        load_players(player_list)
        load_tournaments(tournament_list)
        load_players_tournaments(tournament_list)
        load_rounds_tournaments(tournament_list)
        load_matchs_tournaments(tournament_list)
    elif menu_list == [7, 3]:
        menu_list.pop()
        menu_list.pop()

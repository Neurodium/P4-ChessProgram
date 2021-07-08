from model.player import Player
from datetime import datetime
def find_player_global(player, player_list):
    for i in range(len(player_list)):
        if player.last_name == player_list[i].last_name and player.first_name == player_list[i].first_name:
            return True
    return False

def find_player_tournament(player, tournament_list):
    for i in range(len(tournament_list[-1].players)):
        if player.last_name == tournament_list[-1].players[i].last_name and player.first_name == tournament_list[-1].players[i].first_name:
            return True
    return False

def find_player_previous_match(players_match, round_list):
    for i in range(len(round_list)-1):
        for j in range(len(round_list[i].matchs_round)):
            if round_list[i].matchs_round[j] == (players_match[0], players_match[1]) or round_list[i].matchs_round[j] == (players_match[1], players_match[0]):
                return True
    return False

def add_player(tournament_list, player_list):
    if len(tournament_list) == 0:
        pass
    elif len(tournament_list[-1].players) == tournament_list[-1].max_players:
        print("Le tournoi est complet.")
        pass
    else:
        """add_new_player = "O"
        while add_new_player == "O" and len(tournament_list[-1].players) < tournament_list[-1].max_players:
            last_name = input("Nom: ")
            first_name = input("Prénom: ")
            date = input("Date de naissance (JJ/MM/AAAA): ")
            gender = input("Genre (M/F): ")
            player = Player(last_name, first_name, date, gender)
            if find_player_tournament(player, tournament_list) == False:
                tournament_list[-1].players.append(player)
                if find_player_global(player, player_list) == False:
                    player_list.append(player)
                else:
                    pass
            else:
                print(f"Le joueur est déjà dans le tournoi {tournament_list[-1].name}")
                pass
            if len(tournament_list[-1].players) < tournament_list[-1].max_players:
                add_new_player = input("Voulez-vous ajouter un autre joueur ? O/N")
            else:
                add_new_player = "N"
                """
        tournament_list[-1].players = player_list

    return player_list, tournament_list

def update_player_rank(player_list, tournament_list):
    for i in range(len(tournament_list[-1].matchs)):
        tournament_list[-1].matchs
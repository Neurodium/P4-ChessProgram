from model.player import Player
from datetime import datetime
def find_player_global(player_last_name, player_first_name, player_list):
    for i in range(len(player_list)):
        if player_last_name == player_list[i].last_name and player_first_name == player_list[i].first_name:
            return i


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
                print(f"Le joueur ou la joueuse est déjà dans le tournoi {tournament_list[-1].name}")
                pass
            if len(tournament_list[-1].players) < tournament_list[-1].max_players:
                add_new_player = input("Voulez-vous ajouter un autre joueur ou une autre joueuse ? O/N")
            else:
                add_new_player = "N"
                """
        for player in range(len(player_list)):
            tournament_list[-1].players.append(player_list[player])

    return tournament_list

def update_players_rank(player_list):
    player_list = sorted(player_list, key=lambda player: player.tournament_points, reverse=True)
    for player in range(len(player_list)):
        player_list[player].rank = player + 1
    return player_list

def change_player_rank(player_list):
    player_last_name = input("Quel est le nom du joueur ou de la joueuse ?")
    player_first_name = input("Quel est le prénom du joueur ou de la joueuse ?")
    player = find_player_global(player_last_name, player_first_name, player_list)
    print(f"Le classement de {player_list[player].last_name} {player_list[player].first_name} est {player_list[player].rank} et a {player_list[player].tournament_points} points")
    choice = input("Voulez_vous changez ses informations ? O/N")
    if choice == "O":
        player_list[player].rank = int(input("Quel est son nouveau classement ?"))
        player_list[player].tournament_points = float(input("Quel est son nouveau nombre de points ?"))
    else:
        pass
    return player_list


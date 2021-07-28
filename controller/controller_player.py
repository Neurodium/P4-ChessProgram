from model.player import Player
from datetime import datetime


# checks if a player is found in the global ranking
def check_player_global(player_last_name, player_first_name, player_list):
    for player in player_list:
        if player_last_name == player.last_name and player_first_name == player.first_name:
            return True
    return False


# find a player in the global ranking
def find_player_global(player_last_name, player_first_name, player_list):
    for player in player_list:
        if player_last_name == player.last_name and player_first_name == player.first_name:
            return player


# add a player in the global ranking
def add_global_player(player_last_name, player_first_name, player_list):
    for player in player_list:
        if player_last_name == player.last_name and player_first_name == player.first_name:
            return player


# look for a player in the tournament's player list
def find_player_tournament(player_last_name, player_first_name, tournament_list):
    for player_tournament in tournament_list[-1].players:
        if player_last_name == player_tournament.last_name and player_first_name == player_tournament.first_name:
            return True
    return False


# look if 2 player faced each other in previous rounds
def find_player_previous_match(players_match, round_list):
    for i in range(len(round_list)-1):
        for j in range(len(round_list[i].matchs_round)):
            if round_list[i].matchs_round[j] == (players_match[0], players_match[1]) \
                    or round_list[i].matchs_round[j] == (players_match[1], players_match[0]):
                return True
    return False


# add a player in the tournament
def add_player(tournament_list, player_list):
    if len(tournament_list) == 0:
        pass
    # checks if the tournament is full
    elif len(tournament_list[-1].players) == tournament_list[-1].max_players:
        print("Le tournoi est complet.")
        pass
    else:
        # ask if user wants to add a new player
        add_new_player = (input(
            "Voulez-vous ajouter un joueur O/N ?")).capitalize()
        # check the user input
        while add_new_player not in ["O", "N"]:
            add_new_player = (input("Entrer O ou N")).capitalize()
        while add_new_player == "O" and len(tournament_list[-1].players) < tournament_list[-1].max_players:
            last_name = (input("Nom: ")).upper()
            first_name = (input("Prénom: ")).capitalize()
            # if the player is already added to the tournament, player is not added
            if find_player_tournament(last_name, first_name, tournament_list) is True:
                print("Ce joueur est déjà dans le tournoi")
            # if player is found in the global player list, it is added to the tournament
            elif check_player_global(last_name, first_name, player_list) is True:
                tournament_list[-1].players.append(add_global_player(last_name, first_name, player_list))
                print("Le joueur ou la joueuse a été ajouté au tournoi")
            else:
                # check if the input is a date
                while True:
                    try:
                        date = datetime.strptime(input("Date de naissance (JJ/MM/AAAA): "), '%d/%m/%Y')
                        break
                    except ValueError:
                        print("Vous devez entrer une date")
                gender = (input("Genre (M/F): ")).capitalize()
                # check if gender input is correct
                while gender not in ["M", "F"]:
                    print("Veuillez choisir entre M et F")
                    gender = (input())
                # crate a new instance of player and add in the global list and tournament
                player = Player(last_name, first_name, date, gender)
                tournament_list[-1].players.append(player)
                player_list.append(player)
            # prompt if user wants to add a new player
            if len(tournament_list[-1].players) < tournament_list[-1].max_players:
                add_new_player = (input("Voulez-vous ajouter un autre joueur ou une autre joueuse ? O/N")).capitalize()
            else:
                add_new_player = "N"
    return tournament_list


# update the global ranking
def update_players_rank(player_list):
    player_list = sorted(player_list,
                         key=lambda player: player.tournament_points,
                         reverse=True)
    for player in range(len(player_list)):
        if player != 0:
            if player_list[player].tournament_points == player_list[player - 1].tournament_points:
                player_list[player].rank = player_list[player - 1].rank
            else:
                player_list[player].rank = player + 1
        else:
            player_list[player].rank = player + 1


# change the player ranking and tournament points
def change_player_rank(menu_list, player_list):
    player_last_name = (input("Quel est le nom du joueur ou de la joueuse ?")).upper()
    player_first_name = (input("Quel est le prénom du joueur ou de la joueuse ?")).capitalize()
    player = find_player_global(player_last_name, player_first_name, player_list)
    print(f"Le classement de {player.last_name} {player.first_name} "
          f"est {player.rank} et a {player.tournament_points} points")
    choice = (input("Voulez_vous changez ses informations ? O/N")).capitalize()
    if choice == "O":
        # checks the input for int value
        while True:
            try:
                player.rank = int(input("Quel est son nouveau classement ?"))
                # checks if the input is not negative
                if player.rank >= 0:
                    break
                else:
                    print("La valeur doit être positive")
            except ValueError:
                print("Veuillez choisir son nouveau classement")
        # checks if the input is a float number
        while True:
            try:
                player.tournament_points = float(
                    input("Quel est son nouveau nombre de points ?"))
                break
            except ValueError:
                print("Veuillez choisir un nombre de points")
    else:
        pass
    menu_list.pop()
    return menu_list, player_list

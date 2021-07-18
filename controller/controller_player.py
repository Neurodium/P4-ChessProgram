from model.player import Player


def find_player_global(player_last_name, player_first_name, player_list):
    for player in player_list:
        if player_last_name == player.last_name and player_first_name == player.first_name:
            return player


def find_player_tournament(player, tournament_list):
    for player_tournament in tournament_list[-1].players:
        if player.last_name == player_tournament.last_name and player.first_name == player_tournament.first_name:
            return True
    return False


def find_player_previous_match(players_match, round_list):
    for i in range(len(round_list)-1):
        for j in range(len(round_list[i].matchs_round)):
            if round_list[i].matchs_round[j] == (players_match[0], players_match[1]) \
                    or round_list[i].matchs_round[j] == (players_match[1], players_match[0]):
                return True
    return False


def add_player(tournament_list, player_list):
    if len(tournament_list) == 0:
        pass
    elif len(tournament_list[-1].players) == tournament_list[-1].max_players:
        print("Le tournoi est complet.")
        pass
    else:
        add_new_player = (input(
            "Voulez-vous ajouter un joueur O/N ?")).capitalize()
        while add_new_player not in ["O", "N"]:
            add_new_player = (input("Entrer O ou N")).capitalize()
        while add_new_player == "O" and len(tournament_list[-1].players) < tournament_list[-1].max_players:
            last_name = (input("Nom: ")).upper()
            first_name = (input("Prénom: ")).capitalize()
            date = input("Date de naissance (JJ/MM/AAAA): ")
            gender = (input("Genre (M/F): ")).capitalize()
            while gender not in ["M", "F"]:
                print("Veuillez choisir entre M et F")
                gender = (input())
            player = Player(last_name, first_name, date, gender)
            if find_player_tournament(player, tournament_list) is False:
                tournament_list[-1].players.append(player)
                if find_player_global(last_name, first_name, player_list) is False:
                    player_list.append(player)
                else:
                    pass
            else:
                print(f"Le joueur ou la joueuse est déjà "
                      f"dans le tournoi {tournament_list[-1].name}")
                pass
            if len(tournament_list[-1].players) < tournament_list[-1].max_players:
                add_new_player = (input("Voulez-vous ajouter un autre joueur ou une autre joueuse ? O/N")).capitalize()
            else:
                add_new_player = "N"

        for player in player_list:
            tournament_list[-1].players.append(player)

    return tournament_list


def update_players_rank(player_list):
    player_list = sorted(player_list,
                         key=lambda player: player.tournament_points,
                         reverse=True)
    for player in range(len(player_list)):
        player_list[player].rank = player + 1


def change_player_rank(menu_list, player_list):
    player_last_name = (input("Quel est le nom du joueur ou de la joueuse ?")).upper()
    player_first_name = (input("Quel est le prénom du joueur ou de la joueuse ?")).capitalize()
    player = find_player_global(player_last_name, player_first_name, player_list)
    print(f"Le classement de {player.last_name} {player.first_name} "
          f"est {player.rank} et a {player.tournament_points} points")
    choice = (input("Voulez_vous changez ses informations ? O/N")).capitalize()
    if choice == "O":
        while True:
            try:
                player.rank = int(input("Quel est son nouveau classement ?"))
                break
            except ValueError:
                print("Veuillez choisir son nouveau classement")
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

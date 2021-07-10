from model.tournament import Tournament
from datetime import datetime
from model.player import Player

def create_tournament(tournament_list):
    """
    if len(tournament_list) == 0 or tournament_list[-1].closed == "Y":
        name = input("Quel est le nom de votre tournoi ?")
        place = input("Où se déroulera le tournoi ?")
        date = datetime.strptime(input("Quand se déroulera le tournoi ?"), '%d/%m/%Y')
        time_control = input("Quelle est la méthode de contrôle du temps: Bullet, Blitz ou Coup Rapide ?")
        description = input("Avez-vous des commentaires pour le tournoi ?")
        obj_tournament = Tournament(name, place, date, time_control, description)
        tournament_list.append(obj_tournament)
        return tournament_list
    else:
        print("Il y a déjà un tournoi en cours, vous ne pouvez en créer un nouveau qu'après l'avoir clôturé")
        """
    tournament_list.append(Tournament("Miro", "Paris", "24/07/2021", "Blitz"))
    return tournament_list

def close_tournament(tournament_list, player_list, round_list):
    tournament_list[-1].closed = "Y"
    for round in range(len(round_list)):
        tournament_list[-1].rounds.append(round_list[round])
    round_list[:] = []
    for player in range(len(tournament_list[-1].players)):
        for i in range(len(player_list)):
            if tournament_list[-1].players[player].last_name == player_list[i].last_name and tournament_list[-1].players[player].first_name == player_list[i].first_name:
                player_list[i].tournament_points += float(tournament_list[-1].players[player].tournament_points)
    return tournament_list, player_list, round_list







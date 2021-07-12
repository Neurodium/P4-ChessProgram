from model.tournament import Tournament
from datetime import datetime
from model.player import Player

def create_tournament(tournament_list):
    name = input("Quel est le nom de votre tournoi ?")
    place = input("Où se déroulera le tournoi ?")
    date = datetime.strptime(input("Quand se déroulera le tournoi ?"), '%d/%m/%Y')
    time_control = input("Quelle est la méthode de contrôle du temps: Bullet, Blitz ou Coup Rapide ?")
    description = input("Avez-vous des commentaires pour le tournoi ?")
    obj_tournament = Tournament(name, place, date, time_control, description, players = [], rounds = [])
    tournament_list.append(obj_tournament)
    return tournament_list


def close_tournament(tournament_list, round_list):
    tournament_list[-1].closed = "Y"
    for round in round_list:
        tournament_list[-1].rounds.append(round)
    round_list[:] = []
    return tournament_list, round_list







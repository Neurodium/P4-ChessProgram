from model.tournament import Tournament
from datetime import datetime
from model.player import Player

def create_tournament(tournament_list):
    name = input("Quel est le nom de votre tournoi ?")
    place = ("Où se déroulera le tournoi ?")
    date = datetime.strptime(input("Quand se déroulera le tournoi ?"), '%d/%m/%Y')
    time_control = input("Quelle est la méthode de contrôle du temps: Bullet, Blitz ou Coup Rapide ?")
    obj_tournament = Tournament(name, place, date, time_control)
    tournament_list.append(obj_tournament)
    return tournament_list





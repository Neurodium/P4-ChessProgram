from model.tournament import Tournament
from datetime import datetime
from model.player import Player

def create_tournament(tournament_list):
    if len(tournament_list) == 0 or tournament_list[-1].closed == "Y":
        name = input("Quel est le nom de votre tournoi ?")
        place = ("Où se déroulera le tournoi ?")
        date = datetime.strptime(input("Quand se déroulera le tournoi ?"), '%d/%m/%Y')
        time_control = input("Quelle est la méthode de contrôle du temps: Bullet, Blitz ou Coup Rapide ?")
        obj_tournament = Tournament(name, place, date, time_control)
        tournament_list.append(obj_tournament)
        return tournament_list
    else:
        print("Il y a déjà un tournoi en cours, vous ne pouvez en créer un nouveau qu'après l'avoir clôturé")





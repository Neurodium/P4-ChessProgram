from model.tournament import Tournament
from datetime import datetime


# create a tournament object
def create_tournament(tournament_list):
    name = (input("Quel est le nom de votre tournoi ?")).capitalize()
    place = (input("Où se déroulera le tournoi ?")).capitalize()
    # checks if it is a date
    while True:
        try:
            date = datetime.strptime(input("Quand se déroulera le tournoi (JJ/MM/AAAA) ?"), '%d/%m/%Y')
            break
        except ValueError:
            print("Ce n'est pas une date")
    time_control = (input("Quelle est la méthode de contrôle du temps: Bullet, Blitz ou Coup rapide ?")).capitalize()
    # checks if input is one in the list
    while time_control not in ["Bullet", "Blitz", "Coup rapide"]:
        print("Veuillez choisir entre Bullet, Blitz ou Coup rapide")
        time_control = (input()).capitalize()
    description = input(
        "Avez-vous des commentaires pour le tournoi ?")
    obj_tournament = Tournament(name, place, date, time_control, description, players=[], rounds=[])
    tournament_list.append(obj_tournament)


# close a tournament and update the rounds attached
def close_tournament(tournament_list, round_list):
    tournament_list[-1].closed = "Y"
    for round in round_list:
        tournament_list[-1].rounds.append(round)
    round_list[:] = []

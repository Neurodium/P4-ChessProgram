from model.player import Players
from datetime import datetime

def add_new_player():
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    year = input("Année de naissance: ")
    month = input("Mois de naissance: ")
    day = input("Jour de naissance: ")
    sex = input("Sexe (M/F): ")
    return Players(last_name, first_name, datetime(int(year), int(month), int(day)), sex)
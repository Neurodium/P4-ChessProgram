from model.tournament import Tournament
from datetime import datetime
from model.player import Players

def init_tournament():
    players = [
        Players("Van", "John", datetime(1990, 05, 31), "M"),
        Players("Van", "Charkls", datetime(1991, 05, 31), "M"),
        Players("Van", "Ta", datetime(1989, 05, 31), "F"),
        Players("Star", "John", datetime(1991, 04, 12), "M"),
        Players("Tar", "Julie", datetime(1992, 01, 31), "F"),
        Players("Saz", "John", datetime(1989, 06, 14), "M"),
        Players("Tay", "Sarah", datetime(1988, 07, 31), "F"),
        Players("Zat", "Paul", datetime(1987, 07, 31), "M")
            ]
    tournament = Tournament("Chess1", "Paris", datetime.today(), 3, players, "bullet")
    return tournament



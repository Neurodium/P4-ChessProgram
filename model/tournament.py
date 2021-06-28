class Tournament:
    def __init__(self, name, place, date, rounds, players, time_control, description="", nbtours = 4):
        self.name = name
        self.place = place
        self.date = date
        self.nbtours = nbtours
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description




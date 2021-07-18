class Tournament:
    def __init__(self, name, place, date, time_control, description="", players=[],
                 rounds=[], nbtours=4, max_players=8, closed="N"):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.time_control = time_control
        self.players = players
        self.description = description
        self.nbtours = nbtours
        self.max_players = max_players
        self.closed = closed

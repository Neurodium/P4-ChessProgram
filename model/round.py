from datetime import datetime

class Round:
    def __init__(self, name, date_begin, date_end="", matchs_round = [], closed="N"):
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end
        self.matchs_round = matchs_round
        self.closed = closed


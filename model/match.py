class Round:
    def __init__(self, name, date_begin = '', date_end = ''):
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end

    def start_round(self, date_begin):
        self.date_begin = date_begin

    def end_round(self, date_end):
        self.date_end = date_end

class Match:
    def __init__(self, player, score):
        self.player = player
        self.score = score

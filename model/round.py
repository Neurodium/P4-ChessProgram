class Round:
    def __init__(self,
                 name,
                 date_begin,
                 matchs_round=[],
                 date_end=""):
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end
        self.matchs_round = matchs_round

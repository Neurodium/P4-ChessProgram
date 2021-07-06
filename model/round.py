from datetime import datetime

class Round:
    def __init__(self, name, date_begin, date_end="", match_list=[], closed="N"):
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end
        self.match_list = match_list
        self.closed = closed


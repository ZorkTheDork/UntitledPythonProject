import pandas
from classes.misc import read_excel

class Race:
    
    def __init__(self):
        self.races = read_excel('./config/playable_races.xlsx', 'race')

    def get_races(self):
        return self.races
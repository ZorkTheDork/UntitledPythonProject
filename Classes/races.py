import pandas
from Classes.misc import read_excel

class Race:
    
    def __init__(self):
        self.races = read_excel('./Config/Races.xlsx', 'race')

    def get_races(self):
        return self.races
from Classes.statblock import *
from Classes.Character import Character
from Classes.races import Race

race = Race()
races = race.get_races()

for item in races:
    x = races.get(item)
    for y in x:
        if len(x) < 2:
            print(y)
        else:
            print(y, item)
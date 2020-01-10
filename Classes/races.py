

class Race:
    def __init__(self):
        self.races = {"Dragonborn": {"Dragonborn":"STR2/CHA1"},
        "Dwarf": {"Hill": "CON2/WIS1", "Mountain":"CON2/STR2"}, "Elf": {"High": "DEX2/INT1", "Wood": "DEX2/WIS1", "Drow": "DEX2/CHA1"},
        "Gnome": {"Deep": "INT2/DEX1", "Rock": "INT2/CON1"}, "Half-Elf": {"Half-Elf": "CHA2/ANY1"},
        "Halfling": {"Stout": "DEX2/CON1", "Lightfoot": "DEX2/CHA1"}, "Half-Orc": {"Half-Orc": "STR2/CON1"}}

    def get_races(self):
        return self.races
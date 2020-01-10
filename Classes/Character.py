from .statblock import PrimaryStats, PhysicalStats, Skills, MiscStats, Statblock

class Character:
    def __init__(self, user):
        self.user = user
        self.name = None
        self.race = None
        self.background = None
        self.xp = 0
        self.statblock = None

    def create_character(self):
        pass

    def get_user(self):
        return self.user

    def get_statblock(self):
        return self.statblock
from .statblock import PrimaryStats, PhysicalStats, Skills, MiscStats, Statblock

class Character:
    def __init__(self, user):
        self.user = user
        self.name = ""
        self.race = None
        self.background = None
        self.xp = 0
        self.statblock = None

    def create_character(self):
        prime_stats = PrimaryStats()
        print("Enter values for abilities: \n")
        keys = prime_stats.get_keys()
        keys2 = prime_stats.get_keys2()
        for ability in keys:
            val = input(str(ability).capitalize() + ": ")
            prime_stats.set_ability_score_value(ability, val)
        print("")
        for ability in keys:
            print(str(ability).capitalize() + ": " + str(prime_stats.get_ability_score_value(ability)))
        
        print("")
        prime_stats.update_modifiers()
        for ability_mod in keys2:
            print(str(ability_mod).capitalize() + "_mod: " + str(prime_stats.get_ability_mod_value(ability_mod)))


    def get_user(self):
        return self.user

    def get_statblock(self):
        return self.statblock
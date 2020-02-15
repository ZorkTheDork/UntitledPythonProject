import math, json
from Classes.misc import read_json

class PrimaryStats:
    def __init__(self):
        self.ability_scores = {
            "str": {"value": 0, "proficiency": False}, 
            "dex": {"value": 0, "proficiency": False}, 
            "con": {"value": 0, "proficiency": False}, 
            "int": {"value": 0, "proficiency": False}, 
            "wis": {"value": 0, "proficiency": False}, 
            "cha": {"value": 0, "proficiency": False}
            }

        self.ability_modifiers = {
            "str_mod": math.floor((self.ability_scores["str"]["value"] - 10) / 2),
            "dex_mod": math.floor((self.ability_scores["dex"]["value"] - 10) / 2),
            "con_mod": math.floor((self.ability_scores["con"]["value"] - 10) / 2),
            "int_mod": math.floor((self.ability_scores["int"]["value"] - 10) / 2),
            "wis_mod": math.floor((self.ability_scores["wis"]["value"] - 10) / 2),
            "cha_mod": math.floor((self.ability_scores["cha"]["value"] - 10) / 2)
            }

    def get_ability_scores(self):
        return self.ability_scores

    def get_ability_modifiers(self):
        return self.ability_modifiers

    def add_ability_score(self, ability, amount):
        if ability in self.ability_scores.keys():
            self.ability_scores[ability] += amount
            return 0
        return -1

class PhysicalStats:
    def __init__(self):
        self.hitpoints = 0
        self.temp_hp = 0
        self.armor_class = 10
        self.speed = 0
    
    def set_hitpoints(self, hitpoints):
        self.hitpoints = hitpoints

    def set_temp_hp(self, temp_hp):
        self.temp_hp = temp_hp

    def set_armor_class(self, armor_class):
        self.armor_class = armor_class

    def set_speed(self, speed):
        self.speed = speed

class Skills:
    def __init__(self):
        self.skills = read_json('Config/skills.json')
        if self.skills == -1:
            print("read error")
            self.skills = None

    def get_skills(self):
        return self.skills

    def update_values(self, ability_modifiers, prof_bonus):
        for skill in self.skills:
            for key in ability_modifiers.keys():
                if skill["mod"] == key:
                    skill["value"] = ability_modifiers[key]
                    if skill["prof"] != 0:
                        skill["value"] += math.floor(skill["prof"] * prof_bonus)

class MiscStats:
    def __init__(self):
        self.skills = None
        self.sav_throws = None
        self.dmg_resists = None
        self.dmg_immunes = None
        self.cond_immunes = None
        self.senses = None
        self.languages = None
        self.CR = None

    def set_skills(self, skills):
        self.skills = skills

    def set_sav_throws(self, sav_throws):
        self.sav_throws = sav_throws

    def set_dmg_resists(self, dmg_resists):
        self.dmg_resists = dmg_resists

class Statblock:
    def __init__(self, level, prime_stats, phys_stats, prof_bonus, misc_stats): #, sav_throws, dmg_resists, dmg_immunes, cond_immunes, senses, languages, CR, spells):
        self.level = level
        self.prime_stats = prime_stats
        self.phys_stats = phys_stats
        self.misc_stats = misc_stats
        self.prof_bonus = prof_bonus

    def get_level(self):
        return self.level

    def get_primary_stats(self):
        return self.prime_stats

    def get_physical_stats(self):
        return self.phys_stats

    def get_proficiency(self):
        return self.prof_bonus

    def get_misc_stats(self):
        return self.misc_stats

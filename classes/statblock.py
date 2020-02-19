import math 
import json
from classes.misc import read_json

class PrimaryStats:
    def __init__(self):
        self.ability_scores = {
            "str": {"value": 0, "proficiency": False}, 
            "dex": {"value": 0, "proficiency": False}, 
            "con": {"value": 0, "proficiency": False}, 
            "int": {"value": 0, "proficiency": False}, 
            "wis": {"value": 0, "proficiency": False}, 
            "cha": {"value": 0, "proficiency": False}}

        self.ability_modifiers = {
            "str": math.floor((self.ability_scores["str"]["value"] - 10) / 2),
            "dex": math.floor((self.ability_scores["dex"]["value"] - 10) / 2),
            "con": math.floor((self.ability_scores["con"]["value"] - 10) / 2),
            "int": math.floor((self.ability_scores["int"]["value"] - 10) / 2),
            "wis": math.floor((self.ability_scores["wis"]["value"] - 10) / 2),
            "cha": math.floor((self.ability_scores["cha"]["value"] - 10) / 2)}

    def __set_ability_mod_value(self, ability, val):
        self.ability_modifiers[ability] = val

    def get_ability_scores(self):
        return self.ability_scores

    def get_keys(self):
        return self.ability_scores.keys()

    def get_ability_modifiers(self):
        return self.ability_modifiers
    
    def get_ability_score_value(self, ability):
        return self.ability_scores[ability]["value"]

    def get_ability_mod_value(self, ability):
        return self.ability_modifiers[ability]

    def get_ability_proficiency(self, ability):
        return self.ability_scores[ability]["proficiency"]

    def set_ability_score_value(self, ability, val):
        self.ability_scores[ability]["value"] = val

    def set_ability_proficiency(self, ability, val):
        self.ability_scores[ability]["proficiency"] = val

    def update_modifiers(self):
        for key in self.get_keys():
            val = math.floor((int(self.get_ability_score_value(key)) - 10) / 2)
            self.__set_ability_mod_value(key, val) 

                   

class PhysicalStats:
    def __init__(self):
        self.hitpoints = 0
        self.temp_hp = 0
        self.armor_class = 10
        self.speed = 0
    
    def get_hitpoints(self):
        return self.hitpoints

    def get_temp_hp(self):
        return self.temp_hp

    def get_armor_class(self):
        return self.armor_class

    def get_speed(self):
        return self.speed

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
        self.skills = read_json('config/skills.json')

    def __set_skill_val(self, skill, val):
        self.skills[skill]["value"] = val

    def get_skills(self):
        return self.skills

    def get_skill_val(self, skill):
        return self.skills[skill]["value"]
    
    def get_skill_prof(self, skill):
        return self.skills[skill]["is_prof"]

    def get_keys(self):
        return self.skills.keys()

    def get_mod(self, skill):
        return self.skills[skill]["mod"]

    def update_values(self, ability_modifiers, prof_bonus):
        for skill in self.get_keys():
            for key in ability_modifiers.keys():
                if self.get_mod(skill) == key:
                    total_bonus = ability_modifiers[key]
                    if self.get_skill_prof(skill) != 0:
                        total_bonus += math.floor(self.get_skill_prof(skill) * prof_bonus)
                    self.__set_skill_val(skill, total_bonus)

class Resistances:
    def __init__(self):
        self.dmg_resists = []
        self.dmg_immune = []
        self.cond_immune = []

    def add_dmg_resist(self, resist):
        self.dmg_resists.append(resist)

    def add_dmg_immune(self, immune):
        self.dmg_immune.append(immune)

    def add_cond_immune(self, cond):
        self.cond_immune.append(cond)

    def get_dmg_resists(self):
        return self.dmg_resists

    def get_dmg_immune(self):
        return self.dmg_immune

    def get_cond_immune(self):
        return self.cond_immune

    def remove_dmg_resist(self, resist):
        if resist in self.dmg_resists:
            self.dmg_resists.remove(resist)

class Senses:
    def __init__(self):
        self.senses = []
        self.languages = []
        self.CR = 0

    def add_sense(self, sense):
        self.senses.append(sense)

    def add_language(self, lang):
        self.languages.append(lang)

    def set_CR(self, CR):
        self.CR = CR

    def get_senses(self):
        return self.senses

    def get_languages(self):
        return self.languages

    def get_CR(self):
        return self.CR



class Statblock:
    def __init__(self):
        self.level = None
        self.prime_stats = None
        self.phys_stats = None
        self.skills = None
        self.misc_stats = None
        self.prof_bonus = None

    def get_level(self):
        return self.level

    def get_primary_stats(self):
        return self.prime_stats

    def get_physical_stats(self):
        return self.phys_stats

    def get_skills(self):
        return self.skills

    def get_proficiency(self):
        return self.prof_bonus

    def get_misc_stats(self):
        return self.misc_stats

    def set_skills(self, skills):
        self.skills = skills

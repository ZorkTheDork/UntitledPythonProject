import math 
import json
from classes.enums import RaceSizes, MoveSpeeds
from classes.misc import read_json


class PrimaryStats:
    def __init__(self):
        self._abilities = {
            "str": {"value": 0, "proficiency": False, 
            "mod": -5, "sav_throw": -5}, 
            "dex": {"value": 0, "proficiency": False, 
            "mod": -5, "sav_throw": -5}, 
            "con": {"value": 0, "proficiency": False, 
            "mod": -5, "sav_throw": -5}, 
            "int": {"value": 0, "proficiency": False, 
            "mod": -5, "sav_throw": -5}, 
            "wis": {"value": 0, "proficiency": False, 
            "mod": -5, "sav_throw": -5}, 
            "cha": {"value": 0, "proficiency": False, 
            "mod": -5, "sav_throw": -5}}

    def __set_ability_mod_value(self, ability, val):
        self._abilities[ability]["mod"] = val

    def get_abilities(self):
        return self._abilities

    def get_keys(self):
        return self._abilities.keys()
    
    def get_ability_score_value(self, ability):
        return self._abilities[ability]["value"]

    def get_ability_mod_value(self, ability):
        return self._abilities[ability]["mod"]

    def get_ability_proficiency(self, ability):
        return self._abilities[ability]["proficiency"]

    def get_ability_save(self, ability):
        return self._abilities[ability]["sav_throw"]

    def set_ability_score_value(self, ability, val):
        self._abilities[ability]["value"] = val
        self.__update_modifiers()

    def set_ability_proficiency(self, ability, val):
        self._abilities[ability]["proficiency"] = val
        self.__update_modifiers()

    def __update_modifiers(self):
        for key in self.get_keys():
            val = math.floor((int(self.get_ability_score_value(key)) - 10) / 2)
            self.__set_ability_mod_value(key, val) 

class PhysicalStats:
    def __init__(self):
        self._max_hp = 0
        self._curr_hp = 0
        self._temp_hp = 0
        self._size = RaceSizes.TINY
        self._armor_class = 0
        self._bonus_ac = 0
        self._base_speeds = {MoveSpeeds.WALK: 0, MoveSpeeds.FLY: 0, 
                            MoveSpeeds.SWIM: 0, MoveSpeeds.CLIMB: 0}
        self._bonus_speeds = {MoveSpeeds.WALK: 0, MoveSpeeds.FLY: 0, 
                            MoveSpeeds.SWIM: 0, MoveSpeeds.CLIMB: 0}
    
    def add_curr_hp(self, amt):
        self._curr_hp += amt
        if self._curr_hp > self._max_hp:
            self._curr_hp = self.get_max_hp()        

    def add_temp_hp(self, amt):
        self._temp_hp += amt

    def add_bonus_ac(self, amt):
        self._bonus_ac += amt

    def get_max_hp(self):
        return self._max_hp

    def get_curr_hp(self):
        return self._curr_hp

    def get_temp_hp(self):
        return self._temp_hp

    def get_armor_class(self):
        return self._armor_class

    def get_bonus_ac(self):
        return self._bonus_ac

    def get_base_speeds(self):
        return self._base_speeds

    def get_bonus_speeds(self):
        return self._bonus_speeds

    def reset_temp_hp(self):
        self._temp_hp = 0

    def set_max_hp(self, amt):
        self._max_hp = amt

    def set_armor_class(self, amt):
        self._armor_class = amt

    def set_walk_speed(self, amt):
        self._base_speeds["W"] = amt

    def set_fly_speed(self, amt):
        self._base_speeds["F"] = amt

    def set_swim_speed(self, amt):
        self._base_speeds["S"] = amt

    def set_climb_speed(self, amt):
        self._base_speeds["C"] = amt

class Skills:
    def __init__(self):
        self._skills = read_json('config/skills.json')

    def __set_skill_val(self, skill, val):
        self._skills[skill]["value"] = val

    def get_skills(self):
        return self._skills

    def get_skill_val(self, skill):
        return self._skills[skill]["value"]
    
    def get_skill_prof(self, skill):
        return self._skills[skill]["is_prof"]

    def get_keys(self):
        return self._skills.keys()

    def get_mod(self, skill):
        return self._skills[skill]["mod"]

    def update_values(self, abilities, prof_bonus):
        for skill in self.get_keys():
            for key in abilities.keys():
                if self.get_mod(skill) == key:
                    total_bonus = abilities[key]["mod"]
                    if self.get_skill_prof(skill) != 0:
                        total_bonus += math.floor(self.get_skill_prof(skill) * prof_bonus)
                    self.__set_skill_val(skill, total_bonus)

class Resistances:
    def __init__(self):
        self._dmg_resists = set()
        self._dmg_immunes = set()
        self._cond_immunes = set()

    def add_dmg_resist(self, dmg):
        self._dmg_resists.add(dmg)

    def add_dmg_immune(self, dmg):
        self._dmg_immunes.add(dmg)

    def add_cond_immune(self, cond):
        self._cond_immunes.add(cond)

    def get_dmg_resists(self):
        return self._dmg_resists

    def get_dmg_immunes(self):
        return self._dmg_immunes

    def get_cond_immunes(self):
        return self._cond_immunes

    def remove_dmg_resist(self, dmg):
        try:
            self._dmg_resists.remove(dmg)
        except:
            raise IndexError

    def remove_dmg_immune(self, dmg):
        try:
            self._dmg_immunes.remove(dmg)
        except:
            raise IndexError

    def remove_cond_immune(self, cond):
        try:
            self._cond_immunes.remove(cond)
        except:
            raise IndexError

class Senses:
    def __init__(self):
        self._senses = []
        self._languages = []
        self._CR = 0
        self._passive_perc = 0
        self._passive_inv = 0

    def add_sense(self, sense):
        self._senses.append(sense)

    def add_language(self, lang):
        self._languages.append(lang)

    def set_CR(self, _CR):
        self._CR = _CR

    def get_senses(self):
        return self._senses

    def get_languages(self):
        return self._languages

    def get_CR(self):
        return self._CR



class Statblock:
    def __init__(self):
        self.level = None
        self.prime_stats = None
        self.phys_stats = None
        self._skills = None
        self.misc_stats = None
        self.prof_bonus = None

    def get_level(self):
        return self.level

    def get_primary_stats(self):
        return self.prime_stats

    def get_physical_stats(self):
        return self.phys_stats

    def get_skills(self):
        return self._skills

    def get_proficiency(self):
        return self.prof_bonus

    def get_misc_stats(self):
        return self.misc_stats

    def set_skills(self, skills):
        self._skills = skills

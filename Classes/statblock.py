import math

class PrimaryStats:
    def __init__(self, stng, dex, con, inte, wis, cha):
        self.stng = stng
        self.dex = dex
        self.con = con
        self.inte = inte
        self.wis = wis
        self.cha = cha
        self.str_mod = math.floor((self.stng - 10) / 2)
        self.dex_mod = math.floor((self.dex - 10) / 2)
        self.con_mod = math.floor((self.con - 10) / 2)
        self.int_mod = math.floor((self.inte - 10) / 2)
        self.wis_mod = math.floor((self.wis - 10) / 2)
        self.cha_mod = math.floor((self.cha - 10) / 2)

class PhysicalStats:
    def __init__(self, hitpoints, armor_class, speed):
        self.hitpoints = hitpoints
        self.armor_class = armor_class
        self.speed = speed

class Skills:
    def __init__(self, athl, acro, slei, stea, arca, hist, inve, natu, reli, anim, insi, medi, perc, surv, dece, inti, perf, pers):
        self.athl = athl
        self.acro = acro
        self.slei = slei
        self.stea = stea
        self.arca = arca
        self.hist = hist
        self.inve = inve
        self.natu = natu
        self.reli = reli
        self.anim = anim
        self.insi = insi
        self.medi = medi
        self.perc = perc
        self.surv = surv
        self.dece = dece
        self.inti = inti
        self.perf = perf
        self.pers = pers

class MiscStats:
    def __init__(self, skills, sav_throws, dmg_resists, dmg_immunes, cond_immunes, senses, languages, CR):
        self.skills = skills
        self.sav_throws = sav_throws
        self.dmg_resists = dmg_resists
        self.dmg_immunes = dmg_immunes
        self.cond_immunes = cond_immunes
        self.senses = senses
        self.languages = languages
        self.CR = CR

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

    def get_stng(self):
        return self.prime_stats.stng

    def get_str_mod(self):
        return self.prime_stats.str_mod

    def get_dex(self):
        return self.prime_stats.dex
    
    def get_dex_mod(self):
        return self.prime_stats.dex_mod

    def get_con(self):
        return self.prime_stats.con

    def get_con_mod(self):
        return self.prime_stats.con_mod

    def get_inte(self):
        return self.prime_stats.inte

    def get_inte_mod(self):
        return self.prime_stats.int_mod

    def get_wis(self):
        return self.prime_stats.wis

    def get_wis_mod(self):
        return self.prime_stats.wis_mod

    def get_cha(self):
        return self.prime_stats.cha

    def get_cha_mod(self):
        return self.prime_stats.cha_mod

    def get_hitpoints(self):
        return self.phys_stats.hitpoints

    def get_armor_class(self):
        return self.phys_stats.armor_class

    def get_speed(self):
        return self.phys_stats.speed

    def get_proficiency(self):
        return self.prof_bonus

    def get_skills(self):
        return self.misc_stats.skills
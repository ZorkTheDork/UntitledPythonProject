from enum import Enum, IntEnum
import json

class EnumEncoder(json.JSONEncoder):
    def default(self, obj): # pylint: disable=E0202
        if isinstance(obj, (RaceSizes, MoveSpeeds, IsProficient, DmgTypes, CondTypes, Senses, Languages, ChallengeRatings)):
            return (obj.__class__.__name__, obj._name_, obj._value_)
        return json.JSONEncoder.default(self, obj)

class RaceSizes(Enum):
    TINY = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4
    GARGANTUAN = 5

class MoveSpeeds(Enum):
    WALK = 0
    FLY = 1
    SWIM = 2
    CLIMB = 3

class IsProficient(Enum):
    NOT = 0
    HALF = 1
    FULL = 2
    DOUBLE = 3

class DmgTypes(Enum):
    ACID = 0
    BLUDGEON = 1
    COLD = 2
    FIRE = 3
    FORCE = 4
    LIGHTNING = 5
    NECROTIC = 6
    PIERCE = 7
    POISON = 8
    PSYCHIC = 9
    RADIANT = 10
    SLASH = 11
    THUNDER = 12

class CondTypes(Enum):
    BLIND = 0
    CHARM = 1
    DEAF = 2
    FATIGUE = 3
    FRIGHTEN = 4
    GRAPPLE = 5
    INCAPACITATE = 6
    INVISIBLE = 7
    PAALYZE = 8
    PETRIFY = 9
    POISONED = 10
    PRONE = 11
    RESTRAIN = 12
    STUN = 13
    UNCONSCIOUS = 14
    EXHAUST = 15

class Senses(Enum):
    NORMAL = 0
    BLINDSIGHT = 1
    DARKVISION = 2
    TREMORSENSE = 3
    TRUESIGHT = 4

class Languages(Enum):
    ABYSSAL = 0
    AQUAN = 1
    AURAN = 2
    CELESTIAL = 3
    COMMON = 4
    DEEPSPEECH = 5
    DRACONIC = 6
    DRUIDIC = 7
    DWARVISH = 8
    ELVISH = 9
    GIANT = 10
    GNOMISH = 11
    GOBLIN = 12
    GNOLL = 13
    HALFLING = 14
    IGNAN = 15
    INFERNAL = 16
    ORCISH = 17
    PRIMORDIAL = 18
    SYLVAN = 19
    TERRAN = 20
    UNDERCOMMON = 21

class ChallengeRatings(Enum):
    CR0 = 0
    CR_EIGTH = 1
    CR_QTR = 3
    CR_HALF = 4
    CR1 = 5
    CR2 = 6
    CR3 = 7
    CR4 = 8
    CR5 = 9
    CR6 = 10
    CR7 = 11
    CR8 = 12
    CR9 = 13
    CR10 = 14
    CR11 = 15
    CR12 = 16
    CR13 = 17
    CR14 = 18
    CR15 = 19
    CR16 = 20
    CR17 = 21
    CR18 = 22
    CR19 = 23
    CR20 = 24
    CR21 = 25
    CR22 = 26
    CR23 = 27
    CR24 = 28
    CR30 = 29
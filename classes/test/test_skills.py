import pytest
import json
from classes.statblock import Skills

@pytest.fixture
def setup():
    retval = Skills()
    return retval

def test_init(setup):
    assert setup.get_skills() != json.JSONDecodeError

def test_get_skills(setup):
    skills = setup.get_skills()
    refr = { "acrobatics": {"value": 0, "mod": "dex", "prof": 0}, 
            "animal_handling": {"value": 0, "mod": "wis", "prof": 0}, 
            "arcana": {"value": 0, "mod": "int", "prof": 0}, 
            "athletics": {"value": 0, "mod": "str", "prof": 0},
            "deception": {"value": 0, "mod": "cha", "prof": 0},
            "history": {"value": 0, "mod": "int", "prof": 0},
            "insight": {"value": 0, "mod": "wis", "prof": 0},
            "intimidation": {"value": 0, "mod": "cha", "prof": 0},
            "investigation": {"value": 0, "mod": "int", "prof": 0},
            "medicine": {"value": 0, "mod": "wis", "prof": 0},
            "nature": {"value": 0, "mod": "int", "prof": 0},
            "perception": {"value": 0, "mod": "wis", "prof": 0},
            "performance": {"value": 0, "mod": "cha", "prof": 0},
            "persuasion": {"value": 0, "mod": "cha", "prof": 0},
            "religion": {"value": 0, "mod": "int", "prof": 0},
            "sleight of hand": {"value": 0, "mod": "dex", "prof": 0},
            "stealth": {"value": 0, "mod": "dex", "prof": 0},
            "survival": {"value": 0, "mod": "wis", "prof": 0}}
    assert skills == refr

def test_get_skill_val(setup):
    skills = setup

    for key in skills.get_keys():
        assert skills.get_skill_val(key) == 0
        assert skills.get_skill_prof(key) == 0

def test_update_values(setup):
    assert True

import pytest
from classes.statblock import PrimaryStats

@pytest.fixture
def setup():
    retval = []
    test_stats = PrimaryStats()
    blank_refr = {
            "str": {"value": 0, "proficiency": False, "mod": -5, "sav_throw": -5}, 
            "dex": {"value": 0, "proficiency": False, "mod": -5, "sav_throw": -5}, 
            "con": {"value": 0, "proficiency": False, "mod": -5, "sav_throw": -5}, 
            "int": {"value": 0, "proficiency": False, "mod": -5, "sav_throw": -5}, 
            "wis": {"value": 0, "proficiency": False, "mod": -5, "sav_throw": -5}, 
            "cha": {"value": 0, "proficiency": False, "mod": -5, "sav_throw": -5}}
    retval.append(test_stats)
    retval.append(blank_refr)
    return retval


def test_get_abilities(setup):
    test_data = setup
    test_score = test_data[0].get_abilities()

    assert test_score == test_data[1]


def test_get_keys(setup):
    test_data = setup
    assert test_data[0].get_keys() == test_data[1].keys()


def test_get_ability_score_value(setup):
    test_data = setup

    for key in test_data[0].get_keys():
        assert test_data[0].get_ability_score_value(key) == 0


def test_get_ability_mod_value(setup):
    test_data = setup

    for key in test_data[0].get_keys():
        assert test_data[0].get_ability_mod_value(key) == -5


def test_get_ability_profciency(setup):
    test_data = setup

    for key in test_data[0].get_keys():
        assert test_data[0].get_ability_proficiency(key) == False


def test_set_ability_score_value(setup):
    test_data = setup
    refr = [20, 0, 0, 0, 0, 0]
    test_data[0].set_ability_score_value("str", 20)
    i = 0

    for key in test_data[0].get_keys():
        assert test_data[0].get_ability_score_value(key) == refr[i]
        i += 1

def test_update_modifiers(setup):
    test_data = setup
    test_data[0].set_ability_score_value("str", 20)
    refr = [5, -5, -5, -5, -5, -5]
    i = 0

    for key in test_data[0].get_keys():
        assert test_data[0].get_ability_mod_value(key) == refr[i]
        i += 1
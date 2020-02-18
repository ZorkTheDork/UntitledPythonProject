import pytest
from classes.statblock import PrimaryStats

@pytest.fixture
def setup():
    retval = []
    test_stats = PrimaryStats()
    blank_refr = {
        "str": {"value": 0, "proficiency": False}, 
        "dex": {"value": 0, "proficiency": False}, 
        "con": {"value": 0, "proficiency": False}, 
        "int": {"value": 0, "proficiency": False}, 
        "wis": {"value": 0, "proficiency": False}, 
        "cha": {"value": 0, "proficiency": False}}
    blank_mod_refr = {
        "str": int((0 - 10) / 2),
        "dex": int((0 - 10) / 2),
        "con": int((0 - 10) / 2),
        "int": int((0 - 10) / 2),
        "wis": int((0 - 10) / 2),
        "cha": int((0 - 10) / 2)}
    random_refr = {
        "str": {"value": 20, "proficiency": True}, 
        "dex": {"value": 18, "proficiency": False}, 
        "con": {"value": 17, "proficiency": True}, 
        "int": {"value": 8, "proficiency": False}, 
        "wis": {"value": 9, "proficiency": False}, 
        "cha": {"value": 12, "proficiency": False}}
    retval.append(test_stats)
    retval.append(blank_refr)
    retval.append(blank_mod_refr)
    retval.append(random_refr)
    return retval


def test_get_ability_scores(setup):
    test_data = setup
    test_score = test_data[0].get_ability_scores()

    assert test_score == test_data[1]


def test_get_keys(setup):
    test_data = setup
    #test keys with ability score keys
    assert test_data[0].get_keys() == test_data[2].keys()

    #test keys with ability mod keys
    assert test_data[0].get_keys() == test_data[1].keys()


def test_get_ability_modifiers(setup):
    test_data = setup

    assert test_data[0].get_ability_modifiers() == test_data[2]


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
    test_data[0].update_modifiers()
    refr = [5, -5, -5, -5, -5, -5]
    i = 0

    for key in test_data[0].get_keys():
        assert test_data[0].get_ability_mod_value(key) == refr[i]
        i += 1
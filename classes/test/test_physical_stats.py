import pytest
from classes.statblock import PhysicalStats

@pytest.fixture(scope = 'module')
def setup():
    retval = PhysicalStats()
    return retval

def test_get_max_hp(setup):
    assert setup.get_max_hp() == 0

def test_get_curr_hp(setup):
    assert setup.get_curr_hp() == 0

def test_get_temp_hp(setup):
    assert setup.get_temp_hp() == 0

def test_get_armor_class(setup):
    assert setup.get_armor_class() == 0

def test_get_bonuc_ac(setup):
    assert setup.get_bonus_ac() == 0

def test_get_base_speeds(setup):
    assert setup.get_base_speeds() == {"W": 0, "F": 0, "S": 0, "C": 0}

def test_get_bonus_speeds(setup):
    assert setup.get_bonus_speeds() == {"W": 0, "F": 0, "S": 0, "C": 0}

def test_reset_temp_hp(setup):
    setup.add_temp_hp(5)
    assert setup._temp_hp == 5
    setup.reset_temp_hp()
    assert setup._temp_hp == 0

def test_set_max_hp(setup):
    setup.set_max_hp(10)
    assert setup.get_max_hp() == 10

def test_set_armor_class(setup):
    setup.set_armor_class(12)
    assert setup.get_armor_class() == 12

def test_set_various_speeds(setup):
    setup.set_walk_speed(25)
    assert setup.get_base_speeds() == {"W": 25, "F": 0, "S": 0, "C": 0}
    setup.set_fly_speed(30)
    assert setup.get_base_speeds() == {"W": 25, "F": 30, "S": 0, "C": 0}
    setup.set_swim_speed(12)
    assert setup.get_base_speeds() == {"W": 25, "F": 30, "S": 12, "C": 0}
    setup.set_climb_speed(12)
    assert setup.get_base_speeds() == {"W": 25, "F": 30, "S": 12, "C": 12}
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

def test_set_max_hp(setup):
    setup.set_max_hp(10)
    assert setup.get_max_hp() == 10

def test_set_armor_class(setup):
    data = setup
    data.set_armor_class(12)
    assert data.get_armor_class() == 12
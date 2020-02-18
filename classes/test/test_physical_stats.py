import pytest
from classes.statblock import PhysicalStats

@pytest.fixture(scope = 'module')
def setup():
    retval = PhysicalStats()
    return retval

def test_get_hitpoints(setup):
    assert setup.get_hitpoints() == 0

def test_get_temp_hp(setup):
    assert setup.get_temp_hp() == 0

def test_get_armor_class(setup):
    assert setup.get_armor_class() == 10

def test_get_speed(setup):
    assert setup.get_speed() == 0

def test_set_hitpoints(setup):
    data = setup
    data.set_hitpoints(10)
    assert data.get_hitpoints() == 10

def test_set_temp_hp(setup):
    data = setup
    data.set_temp_hp(3)
    assert data.get_temp_hp() == 3

def test_set_armor_class(setup):
    data = setup
    data.set_armor_class(12)
    assert data.get_armor_class() == 12

def test_set_speed(setup):
    data = setup
    data.set_speed(30)
    assert data.get_speed() == 30
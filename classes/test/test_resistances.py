import pytest
from classes.statblock import Resistances

@pytest.fixture
def setup():
    res = Resistances()
    return res

def test_get_dmg_resists(setup):
    assert setup.get_dmg_resists() == set()


def test_get_dmg_immunes(setup):
    assert setup.get_dmg_immunes() == set()


def test_get_cond_immunes(setup):
    assert setup.get_cond_immunes() == set()


def test_add_remove_dmg_immune(setup):
    setup.add_dmg_immune("pr")
    assert "pr" in setup.get_dmg_immunes()
    setup.remove_dmg_immune("pr")
    assert "pr" not in setup.get_dmg_immunes()


def test_add_remove_cond_immune(setup):
    setup.add_cond_immune("ch")
    assert "ch" in setup.get_cond_immunes()
    setup.remove_cond_immune("ch")
    assert "ch" not in setup.get_cond_immunes()


def test_add_remove_dmg_resist(setup):
    setup.add_dmg_resist("pr")
    assert "pr" in setup.get_dmg_resists()
    setup.remove_dmg_resist("pr")
    assert "pr" not in setup.get_dmg_resists()
import pytest
from classes.statblock import PrimaryStats

class TestPrimaryStats:
    def test_get_ability_scores(self):
        test_stats = PrimaryStats()
        test_score = test_stats.get_ability_scores()
        refr = {
            "str": {"value": 0, "proficiency": False}, 
            "dex": {"value": 0, "proficiency": False}, 
            "con": {"value": 0, "proficiency": False}, 
            "int": {"value": 0, "proficiency": False}, 
            "wis": {"value": 0, "proficiency": False}, 
            "cha": {"value": 0, "proficiency": False}}
        
        assert test_score == refr

    def test_get_keys(self):
        test_stats = PrimaryStats()
        test_keys = test_stats.get_keys()
        refr = {
            "str": ((0 - 10) / 2),
            "dex": ((0 - 10) / 2),
            "con": ((0 - 10) / 2),
            "int": ((0 - 10) / 2),
            "wis": ((0 - 10) / 2),
            "cha": ((0 - 10) / 2)}

        assert test_keys == refr.keys()
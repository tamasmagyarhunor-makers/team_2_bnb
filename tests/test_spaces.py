from lib.spaces import *

"""
Given an a space instance is created,
all of its attributes correctly generate
"""

def test_space_attributes_are_correct():
space = Space(1, "House by the Lake", "Italy", "It is a house by the lake", 50, 1)
assert space.id == 1
assert space.name == "House by the Lake"
assert space.location == "Italy"
assert space.description == "It is a house by the lake"
assert space.price_per_night == 50
assert space.owner_id == 1
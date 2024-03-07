from lib.space import *

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
    assert space.price == 50
    assert space.user_id == 1

"""
When two objects are compared with identical data
they are assessed as equal
"""
def test_same_values_are_equal():
    space_1 = Space(1, "House by the Lake", "Italy", "It is a house by the lake", 50, 1)
    space_2 = Space(1, "House by the Lake", "Italy", "It is a house by the lake", 50, 1)
    assert space_1 == space_2

"""
Given a space's information is completed
it is returned in a nice format
"""
def test_space_is_correctly_formatted():
    space = Space(1, "House by the Lake", "Italy", "It is a house by the lake", 50, 1)
    assert str(space) == "1, House by the Lake, Italy, It is a house by the lake, 50, 1"
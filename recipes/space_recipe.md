# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user, 
I want to view a list of all spaces on MakersBnb
So that I can decide where I want to stay

Model object to be created


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Space:
    # User-facing properties:
    #   name: string

    def __init__(self, id, name, location, description, price_per_night, owner_id):
        # Parameters:
        #   id = int
        #   name = string
        #   location = string
        #   description = string
        #   price_per_night = float
        #   owner_id = int
        #   Side effects:
        #   Sets the properties of the space object
        pass # No code here yet


    def __eq__(self, other):
        # Parameters:
        #   task: tests equality of identical data
        # Returns:
        #   True/False
        # Side-effects
        #   N/A
        pass # No code here yet

    def __repr__(self):
        # Returns:
        #   A formatted string of the space - name, location, description, price_per_night, owner_id
        # Side-effects:
        #   N/A
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

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
    
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

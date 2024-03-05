# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user, 
I want to view a list of all spaces on MakersBnb
So that I can decide where I want to stay


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class SpaceRepository:
    # User-facing properties:
    #   name: string

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute("SELECT * FROM Spaces")
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["location"], row["description"], row["price"], row["user_id"])
            spaces.append(item)
        return spaces
    

    def find(self, space_id):
        rows = self._connection.execute(
                 'SELECT * from spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["description"], row["price"], row["user_id"])

    def create(self, space):
        self._connection.execute('INSERT INTO spaces (name, location, description, price, user_id) VALUES (%s, %s, %s, %s, %s)', [
            space.name, space.location, space.description, space.price, space.user_id])
        return None

    def delete(self, space_id):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [space_id])
        return None

    def update(self, space):
        self._connection.execute(
            'UPDATE spaces SET name = %s,  location = %s,  description = %s, price = %s, user_id = %s WHERE id = %s',
            [space.name, space.location, space.description, space.price, space.user_id, space.id])
        return None

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
from lib.space_repository import SpaceRepository
from lib.space import Space

``` python
"""
When we call SpaceRepository#all
We get a list of Space objects reflecting the seed data.
"""
def test_get_all_spaces(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/bnb_seed.sql") # Seed our database with some test data
    repository = SpaceRepository(db_connection) # Create a new SpaceRepository

    spaces = repository.all() # Get all spaces

    # Assert on the results
    assert spaces == [
        Space(1, 'Cozy Studio Apartment', 'New York', 'A small but comfortable studio in downtown.', 100.00, 1),
        Space(2, 'Spacious Loft', 'Los Angeles', 'A modern loft with city views.', 150.00, 2),
        Space(3, 'Beach House', 'Miami', 'A beautiful house steps away from the beach.', 200.00, 3)
    ]

"""
When we call SpaceRepository#find
We get a single Space object reflecting the seed data.
"""
def test_get_single_space(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find(3)
    assert space == Space(3, 'Beach House', 'Miami', 'A beautiful house steps away from the beach.', 200.00, 3)

"""
When we call SpaceRepository#create
We get a new space in the database.
"""
def test_create_space(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = SpaceRepository(db_connection)

    repository.create(Space(None, 'Lake House', 'Iowa', 'A large house with a balcony near the lake.', 185.00, 3))

    result = repository.all()
    assert result == [
        Space(1, 'Cozy Studio Apartment', 'New York', 'A small but comfortable studio in downtown.', 100.00, 1),
        Space(2, 'Spacious Loft', 'Los Angeles', 'A modern loft with city views.', 150.00, 2),
        Space(3, 'Beach House', 'Miami', 'A beautiful house steps away from the beach.', 200.00, 3),
        Space(4, 'Lake House', 'Iowa', 'A large house with a balcony near the lake.', 185.00, 3),
    ]

"""
When we call SpaceRepository#delete
We remove a space from the database.
"""
def test_delete_Space(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    repository.delete(2) 

    result = repository.all()
    assert result == [
        Space(1, 'Cozy Studio Apartment', 'New York', 'A small but comfortable studio in downtown.', 100.00, 1),
        Space(3, 'Beach House', 'Miami', 'A beautiful house steps away from the beach.', 200.00, 3),
    ]

"""
When we update one piece of informaiton in a space
it is updated in the database

"""

def test_update_single_piece_of_info_for_space(db_connection):
    db_connection.seed("seeds/bnb_seed.sql") 
    repository = SpaceRepository(db_connection) 
    space = repository.find(2)
    space.name = "Log Cabin"
    repository.update(space)
    updated_space = repository.find(2)

    expected_space = Space(id=2, name='Log Cabin', location='Los Angeles', description='A modern loft with city views.', price=150.0, user_id=2)
    assert updated_space == expected_space

"""
When we update multiple pieces of informaiton in a space
it is updated in the database

"""

def test_update_multiple_pieces_of_info_for_space(db_connection):
    db_connection.seed("seeds/bnb_seed.sql") 
    repository = SpaceRepository(db_connection) 
    space = repository.find(2)
    space.name = "Log Cabin"
    space.location = "Vancouver"
    space.description = "A modern cabin with modern features."
    repository.update(space)
    updated_space = repository.find(2)

    expected_space = Space(id=2, name='Log Cabin', location='Vancouver', description='A modern cabin with modern features.', price=150.0, user_id=2)
    assert updated_space == expected_space


```
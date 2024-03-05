from lib.space_repository import SpaceRepository
from lib.space import Space

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



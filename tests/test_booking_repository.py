from lib.booking_repository import BookingRepository
from lib.bookings import Booking

"""
When we call BookRepository#all
We get a list of Booking objects reflecting the seed data.
"""
def test_get_all_bookings(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/bnb_seed.sql") # Seed our database with some test data
    repository = BookingRepository(db_connection) # Create a new BookingRepository

    booking = repository.all() # Get all bookings
    print(type(booking))
    print(type(booking[0]))
    print(type(booking[1]))

    # Assert on the results
    assert booking == [
        Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1),
        Booking(2, 'Spacious Loft', 'Approved', '2024-03-05', '2024-03-08', 2, 2),
        Booking(3, 'Beach House', 'Pending', '2024-04-06', '2024-04-10', 3, 3)
    ]

"""
When we call BookingRepository#find
We get a single Booking object reflecting the seed data.
"""
def test_get_single_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)

    booking = repository.find(3)
    assert booking == Booking(3, 'Beach House', 'Pending', '2024-04-06', '2024-04-10', 3, 3)

"""
When we call BookingRepository#create
We get a new space in the database.
"""
def test_create_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)

    repository.create(Booking(None, 'Log cabin', 'Pending', '2024-07-11', '2024-07-20', 3, 3))

    result = repository.all()
    assert result == [
        Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1),
        Booking(2, 'Spacious Loft', 'Approved', '2024-03-05', '2024-03-08', 2, 2),
        Booking(3, 'Beach House', 'Pending', '2024-04-06', '2024-04-10', 3, 3),
        Booking(4, 'Log cabin', 'Pending', '2024-07-11', '2024-07-20', 3, 3)
        ]


"""
When we call BookingRepository#delete
We remove a Booking from the database.
"""
def test_delete_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)
    repository.delete(2) 

    result = repository.all()
    assert result == [
        Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1),
        Booking(3, 'Beach House', 'Pending', '2024-04-06', '2024-04-10', 3, 3),
    ]

"""
When we update one piece of informaiton in a booking
it is updated in the database
"""

def test_update_single_piece_of_info_for_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql") 
    repository = BookingRepository(db_connection) 
    booking = repository.find(2)
    booking.space_name = "Log Cabin"
    repository.update(booking)
    updated_booking = repository.find(2)

    expected_booking = Booking(id= 2, space_name='Log Cabin', booking_status='Approved', start_date='2024-03-05', end_date='2024-03-08', space_id=2, user_id=2)
    assert updated_booking == expected_booking

"""
When we update multiple pieces of informaiton in a booking
it is updated in the database

"""

def test_update_multiple_piece_of_info_for_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql") 
    repository = BookingRepository(db_connection) 
    booking = repository.find(2)
    booking.space_name = "Ocean Hotel"
    booking.booking_status = "Pending"
    repository.update(booking)
    updated_booking = repository.find(2)

    expected_booking = Booking(id= 2, space_name='Ocean Hotel', booking_status='Pending', start_date='2024-03-05', end_date='2024-03-08', space_id=2, user_id=2)
    assert updated_booking == expected_booking



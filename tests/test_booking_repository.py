from lib.booking import Booking

"""
Given an a booking instance is created,
all of its attributes correctly generate
"""
def test_booking_attributes_are_correct():
    booking = Booking(1, "Pending", "2024-03-04", 1, 2)
    assert Booking.id == 1
    assert Booking.space_id == space_id
    assert Booking.space_name == space_name
    assert Booking.booking_status == booking_status
    assert Booking.start_date == start_date
    assert Booking.end_date == end_date
    assert Booking.booking_id == booking_id



"""
When two objects are compared with identical data
they are assessed as equal
"""
def test_same_booking_values_are_equal():
    booking_1 = Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1)
    booking_2 = Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1)
    assert booking_1 == booking_2

"""
Given a booking's information is completed
it is returned in a nice format
"""
def test_booking_is_correctly_formatted():
    booking = Booking(1, "Mr", "John", "Smith", "email@testmail.com", "Password2", "07926345037")
    assert str(booking) == "1, Mr, John, Smith, email@testmail.com, Password2, 07926345037"
from lib.bookings import Booking

"""
Given an a booking instance is created,
all of its attributes correctly generate
"""
def test_booking_attributes_are_correct():
    booking = Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1)
    assert booking.id == 1
    assert booking.space_name == "Cozy Studio Apartment"
    assert booking.booking_status == "Pending"
    assert booking.start_date == "2024-03-04"
    assert booking.end_date == "2024-03-06"
    assert booking.space_id == 1
    assert booking.user_id == 1


"""
When two objects are compared with identical data
they are assessed as equal
"""
def test_same_booking_values_are_equal():
    booking_1 = Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1)
    booking_2 = Booking(1, 'Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1)
    assert booking_1 == booking_2

"""
Given a booking's information is completed
it is returned in a nice format
"""
def test_booking_is_correctly_formatted():
    booking = Booking(1, "Mr", "John", "Smith", "email@testmail.com", "Password2", "07926345037")
    assert str(booking) == "1, Mr, John, Smith, email@testmail.com, Password2, 07926345037"
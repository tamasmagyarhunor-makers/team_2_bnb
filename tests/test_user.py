from lib.user import User

"""
Given an a user instance is created,
all of its attributes correctly generate
"""
def test_user_attributes_are_correct():
    user = User(1, "Mr", "John", "Smith", "email@testmail.com", "Password2", "07926345037")
    assert user.id == 1
    assert user.title == "Mr"
    assert user.first_name == "John"
    assert user.last_name == "Smith"
    assert user.email_address == "email@testmail.com"
    assert user.password == "Password2"
    assert user.phone_number == "07926345037"
"""
When two objects are compared with identical data
they are assessed as equal
"""
def test_same_values_are_equal():
    user_1 = User(1, "Mr", "John", "Smith", "email@testmail.com", "Password2", "07926345037")
    user_2 = User(1, "Mr", "John", "Smith", "email@testmail.com", "Password2", "07926345037")
    assert user_1 == user_2

"""
Given a user's information is completed
it is returned in a nice format
"""
def test_user_is_correctly_formatted():
    user = User(1, "Mr", "John", "Smith", "email@testmail.com", "Password2", "07926345037")
    assert str(user) == "1, Mr, John, Smith, email@testmail.com, Password2, 07926345037"
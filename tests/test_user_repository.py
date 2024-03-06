from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#create
We get a new user in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, 'Dr', 'Drake', 'Ramoray', 'dr_drake_actor@daysofourlives.com', 'MyTwinIsAWrongin', '07415103842'))

    result = repository.all()
    assert result == [
        User(1, "Mr", "John", "Smith", "email@testmail.com", "Password1", "07926345037"),
        User(2, "Miss", "Regina", "Phalange", "Regina_phalange@testmail.com", "Password2", "07926345048"),
        User(3, "Mr", "Ken", "Adams", "ken_adams@testmail.com", "Password3", "07926345081"),
        User(4, 'Dr', 'Drake', 'Ramoray', 'dr_drake_actor@daysofourlives.com', 'MyTwinIsAWrongin', "07415103842")
    ]
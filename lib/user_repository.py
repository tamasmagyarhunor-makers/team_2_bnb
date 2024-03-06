from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            item = User(row["id"], row["title"], row["first_name"], row["last_name"], row["email_address"], row["password"], row["phone_number"])
            users.append(item)
        return users

    def create(self, user):
        self._connection.execute('INSERT INTO users (title, first_name, last_name, email_address, password, phone_number) VALUES (%s, %s, %s, %s, %s, %s)', [
            user.title, user.first_name, user.last_name, user.email_address, user.password, user.phone_number])
        return None

    # def delete(self, space_id):
    #     self._connection.execute(
    #         'DELETE FROM spaces WHERE id = %s', [space_id])
    #     return None

    # def update(self, space):
    #     self._connection.execute(
    #         'UPDATE spaces SET name = %s,  location = %s,  description = %s, price = %s, user_id = %s WHERE id = %s',
    #         [space.name, space.location, space.description, space.price, space.user_id, space.id])
    #     return None

    
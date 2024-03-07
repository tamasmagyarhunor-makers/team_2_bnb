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
    
    def find(self, user_id):
        rows = self._connection.execute(
                 'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["title"], row["first_name"], row["last_name"], row["email_address"], row["password"], row["phone_number"])
    
    # def find_by_email(self, email):
    #     rows = self._connection.execute(
    #              'SELECT * from users WHERE id = %s', [email])
    #     row = rows[0]
    #     return User(row["id"], row["title"], row["first_name"], row["last_name"], row["email_address"], row["password"], row["phone_number"])
    

    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * from users WHERE email_address = %s', [email])
        if rows == []:
            return None
        row = rows[0]
        user_dict = {
            "id": row["id"],
            "title": row["title"],
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "email_address": row["email_address"],
            "password": row["password"],
            "phone_number": row["phone_number"]
        }
        
        return user_dict

    # def get_user_details_by_email(self, email):
    #     query = f"SELECT id, password FROM users WHERE email_address = ?"
    #     self._connection.execute(query, (email,))
    #     user = self._connection.fetchone()
    #     return user

    # def delete(self, space_id):
    #     self._connection.execute(
    #         'DELETE FROM spaces WHERE id = %s', [space_id])
    #     return None

    # def update(self, space):
    #     self._connection.execute(
    #         'UPDATE spaces SET name = %s,  location = %s,  description = %s, price = %s, user_id = %s WHERE id = %s',
    #         [space.name, space.location, space.description, space.price, space.user_id, space.id])
    #     return None

    
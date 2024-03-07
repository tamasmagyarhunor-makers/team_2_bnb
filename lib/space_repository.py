from lib.space import Space

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
        rows_id = self._connection.execute('INSERT INTO spaces (name, location, description, price, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id', [
            space.name, space.location, space.description, space.price, space.user_id])
        return rows_id[0]["id"]

    def delete(self, space_id):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [space_id])
        return None

    def update(self, space):
        self._connection.execute(
            'UPDATE spaces SET name = %s,  location = %s,  description = %s, price = %s, user_id = %s WHERE id = %s',
            [space.name, space.location, space.description, space.price, space.user_id, space.id])
        return None




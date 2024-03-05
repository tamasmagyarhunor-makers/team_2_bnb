class Space:
    def __init__(self, id, name, location, description, price, user_id):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.price = price
        self.user_id = user_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.location}, {self.description}, {self.price}, {self.user_id}"
class Space:
    def __init__(self, id, name, location, description, price_per_night, owner_id):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.price_per_night = price_per_night
        self.owner_id = owner_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.location}, {self.description}, {self.price_per_night}, {self.owner_id}"
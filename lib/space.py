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
    
    # These next two methods will be used by the controller to check if
    # spaces are valid and if not show errors to the user.
    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.location == None or self.location == "":
            return False
        if self.description == None or self.description == "":
            return False
        if self.price == None or self.price == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("Name can't be blank")
        if self.location == None or self.location == "":
            errors.append("Location can't be blank")
        if self.description == None or self.description == "":
            errors.append("Description can't be blank")   
        if self.price == None or self.price == "":
            errors.append("Price can't be blank")     
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
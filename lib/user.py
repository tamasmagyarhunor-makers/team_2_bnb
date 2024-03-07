class User:
    def __init__(self, id, title, first_name, last_name, email_address, password, phone_number):
        self.id = id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password
        self.phone_number = phone_number


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}, {self.title}, {self.first_name}, {self.last_name}, {self.email_address}, {self.password}, {self.phone_number}"
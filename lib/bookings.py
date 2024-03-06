class Booking:
    def __init__(self, id, space_name, booking_status, start_date, end_date, space_id, user_id):
        self.id = id
        self.space_name = space_name
        self.booking_status = booking_status
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.space_id = space_id
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}, {self.space_name}, {self.booking_status}, {self.start_date}, {self.end_date}, {self.space_id}, {self.user_id}"
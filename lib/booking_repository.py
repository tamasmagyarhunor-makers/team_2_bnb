from lib.bookings import Booking

class BookingRepository():
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["space_name"], row["booking_status"], row["start_date"], row["end_date"], row["space_id"], row["user_id"])
            bookings.append(item)
        return bookings
    
    def find(self, booking_id):
        rows = self._connection.execute(
                 'SELECT * from bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row["id"], row["space_name"], row["booking_status"], row["start_date"], row["end_date"], row["space_id"], row["user_id"])

    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (space_name, booking_status, start_date, end_date, space_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)', [
            booking.space_name, booking.booking_status, booking.start_date, booking.end_date, booking.space_id, booking.user_id])
        return None
    
    def delete(self, booking_id):
        self._connection.execute(
            'DELETE FROM Bookings WHERE id = %s', [booking_id])
        return None
    
    def update(self, booking):
        self._connection.execute(
            'UPDATE bookings SET space_name = %s,  booking_status = %s,  start_date = %s, end_date = %s, space_id = %s, user_id = %s WHERE id = %s',
            [booking.space_name, booking.booking_status, booking.start_date, booking.end_date, booking.space_id, booking.user_id, booking.id])
        return None

    
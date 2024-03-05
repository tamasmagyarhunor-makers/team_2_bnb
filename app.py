import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection


# Create a new Flask app
app = Flask(__name__)

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

# --------- LOGIN -----------

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html')

# -------- SPACES ----------

# Get details of all spaces - GET /space - SELECT * FROM spaces
@app.route('/space', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = space_repo(connection)
    spaces = repository.all()
    return render_template('spaces/spaces.html', space = spaces)


# Get details of a single space - GET /space/<id> - SELECT * FROM spaces WHERE id = <id>
@app.route('/space/<int:space_id>', methods=['GET'])
def get_space(space_id):
    connection = get_flask_database_connection(app)
    repository = space_repo(connection)
    space = repository.find(space_id)
    return render_template('spaces/space.html', space=space)


# GET /spaces/new
# Returns a form to create a new spaces
@app.route('/space/new', methods=['GET'])
def get_new_space():
    return render_template('spaces/new.html')

# Create a new space - POST /space - INSERT INTO spaces VALUES ...
@app.route('/space', methods=['POST'])
def create_new_space():
    connection = get_flask_database_connection(app)
    repository = space_repo(connection)
    new_space = space(
        None,
        request.form['name'],
        request.form['location'],
        request.form['description'],
        request.form['price'],
        request.form['user_id'])
    new_space = repository.create(new_space)
    return redirect(f"/space/{space.id}")


# -------- USERS ----------

# Get details of all users - GET /user - SELECT * FROM users

@app.route('/user', methods=['GET'])
def get_all_users():
    connection = get_flask_database_connection(app)
    repository = user_repo(connection)
    users = repository.all()
    return render_template('users/users.html', user = users)

# Get details of a user - GET /user/<id> - SELECT * FROM users WHERE id = <id>

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    connection = get_flask_database_connection(app)
    repository = user_repo(connection)
    user = repository.find(user_id)
    return render_template('users/user.html', user=user)

# -------- AVAILABILITY ----------

# Get availability of all spaces - GET /availability - SELECT * FROM availability

@app.route('/space/availability', methods=['GET'])
def get_all_users():
    connection = get_flask_database_connection(app)
    repository = space_repo(connection)
    users = repository.all()
    return render_template('spaces/spaces.html', user = users)

# Get availability of a single space - GET /availability/<space_id> - SELECT * FROM availability WHERE space_id = <space_id>

@app.route('spaces/availability/<int:space_id>', methods=['GET'])
def get_space_availability(space_id):
    connection = get_flask_database_connection(app)
    repository = space_repo(connection)
    space = repository.find(space_id)
    return render_template('spaces/space.html', space=space)

# -------- REQUESTS ----------

# Get booking requests by booker - GET /requests/<booker_id> - SELECT * FROM bookings WHERE booker_id = <booker_id>

@app.route('requests/booker/<int:booker_id>', methods=['GET'])
def get_requests_by_booker(booker_id):
    connection = get_flask_database_connection(app)
    repository = user_repo(connection)
    booking_requests = repository.find(booker_id)
    return render_template('booking_requests/booking_request.html', booking_requests=booking_request)

# Get booking requests by owner - GET /requests/<owner_id> - SELECT * FROM bookigns WHERE owner_id = <booker_id>

# Get booking requests by space  - GET /requests/<space_id> - SELECT * FROM spaces WHERE spcae_id = <space_id>


# Create a new booking request
#     - SELECT <date> FROM availability WHERE space_id = <space_id>
#     if available....
#     - INSERT INTO bookings VALUES <space_id>, <date>, <user_id>, <status = 'pending'>

# Accept a booking request

#     - PATCH availability SET <date> = False WHERE space_id = <space_id>
#     - PATCH bookings SET <status> = 'accepted' WHERE space_id = <space_id>

# END ROUTES

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


import os
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.user import *
from lib.user_repository import *
from flask import Flask, request, render_template, redirect, url_for, session



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

@app.route('/list_a_space', methods=['GET'])
def get_list_a_space():
    return render_template('list_a_space.html')

# -------- SPACES ----------

# Get details of all spaces - GET /space - SELECT * FROM spaces
@app.route('/spaces', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces)


# Get details of a single space - GET /space/<id> - SELECT * FROM spaces WHERE id = <id>
@app.route('/space/<int:space_id>', methods=['GET'])
def get_space(space_id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(space_id)
    return render_template('show_space.html', space=space)


# GET /spaces/new
# Returns a form to create a new spaces
@app.route('/space/new', methods=['GET'])
def get_new_space():
    return render_template('list_a_space.html')

# Create a new space - POST /space - INSERT INTO spaces VALUES ...
# @app.route('/list_a_space', methods=['POST'])
# def create_new_space():
#     connection = get_flask_database_connection(app)
#     repository = SpaceRepository(connection)
#     new_space = Space(
#         None,
#         request.form['name'],
#         request.form['location'],
#         request.form['description'],
#         request.form['price'],
#         request.form['user_id'])
#     new_space = repository.create(new_space)
#     return redirect(f"/list_a_space/{new_space.id}")


# Creates a new space
@app.route('/list_a_space', methods=['POST'])
def create_space():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    # Get the fields from the request form
    name = request.form['name']
    location = request.form['location']
    description = request.form['description']
    price = request.form['price']
    user_id = 1 #replace with session id when ready
    # Create a book object
    space = Space(None, name, location, description, price, user_id)
    # Check for validity and if not valid, show the form again with errors
    if not space.is_valid():
        return render_template('list_a_space.html', space=space, errors=space.generate_errors()), 400
    # Save the book to the database
    space = repository.create(space)
    #space_id = TO RETRIEVE

    # Redirect to the book's show route to the user can see it
    return render_template('space_successfully_listed.html')
    #return redirect(f"/list_a_space/{space.id}")

   
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
    repository = UserRepository(connection)
    user = repository.find(user_id)
    return render_template('users/<int:user_id>.html', user=user)

# Submit a new user - POST /user - INSERT INTO user VALUES ...
@app.route('/sign_up/submit', methods=['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = User(
        None,
        request.form['title'],
        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['phone_number'],
        request.form['password'])
    new_user = repository.create(new_user)
    return redirect(f"/user/{user.id}")

# Submit a login request - POST /login/submit - SELECT password FROM users WHERE email=<email>
@app.route('/login/submit', methods=['POST'])
def submit_login_request():
    # making the connection to the database
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    # storing the user's entered credentials in a dictionary
    entered_email = request.form.get('email_address')
    entered_password = request.form.get('password')
    # getting the user in dictionary format which matches the email from the database
    # in format {
    #     "id": 1,
    #     "title": "Mr",
    #     "first_name": "John",
    #     "last_name": "Smith",
    #     "email_address": "email@testmail.com",
    #     "password": "Password1",
    #     "phone_number": '07926345037'
    # }
    stored_password = repository.find_by_email(entered_email).get('password')
    if entered_password == stored_password:
        return redirect("/spaces")
    else:
        return render_template('login.html', invalid_login=True)
    # user_id = repository.get_id(entered_email) # this will need adding to user repository
    #     session['user_id'] = user_id
    #     return redirect(f"/spaces")
    # else:
    #     pass

# -------- REQUESTS ----------
# Use this code to retrieve logged in user id --> user_id = session.get('user_id')



# Get booking requests by booker - GET /requests/<booker_id> - SELECT * FROM bookings WHERE booker_id = <booker_id>

@app.route('/requests/booker/<int:booker_id>', methods=['GET'])
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

# -------- AVAILABILITY ----------

# Get availability of all spaces - GET /availability - SELECT * FROM availability

@app.route('/space/availability', methods=['GET'])
def get_availability():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    users = repository.all()
    return render_template('spaces/spaces.html', user = users)

# Get availability of a single space - GET /availability/<space_id> - SELECT * FROM availability WHERE space_id = <space_id>

@app.route('/spaces/availability/<int:space_id>', methods=['GET'])
def get_space_availability(space_id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(space_id)
    return render_template('spaces/space.html', space=space)

# END ROUTES

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


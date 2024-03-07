import os
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.user import *
from lib.user_repository import *
from flask import Flask, request, render_template, redirect, url_for, session



# Create a new Flask app
app = Flask(__name__)


app.secret_key = 'secret'
# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

# --------- LOGIN -----------

@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if 'user_id' in session:
        user = repository.find(session['user_id'])
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')
@app.route('/login', methods=['GET'])
def get_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if 'user_id' in session:
        user = repository.find(session['user_id'])
        return render_template('login.html', user=user)
    else:
        return render_template('login.html')
    
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index.html'))

@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if 'user_id' in session:
        user = repository.find(session['user_id'])
        return render_template('sign_up.html', user=user)
    else:
        return render_template('sign_up.html')

@app.route('/list_a_space', methods=['GET'])
def get_list_a_space():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find(session['user_id'])
    return render_template('list_a_space.html', user=user)

@app.route('/am_i_logged_in', methods=['GET'])
def get_am_i_logged_in():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find(session['user_id'])
    return render_template('am_i_logged_in.html', user=user)

# -------- SPACES ----------

# Get details of all spaces - GET /space - SELECT * FROM spaces
@app.route('/spaces', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    repository2 = UserRepository(connection)
    user = repository2.find(session['user_id'])
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces, user=user)


# Get details of a single space - GET /space/<id> - SELECT * FROM spaces WHERE id = <id>
@app.route('/space/<int:space_id>', methods=['GET'])
def get_space(space_id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    repository2 = UserRepository(connection)
    user = repository2.find(session['user_id'])
    space = repository.find(space_id)
    return render_template('show_space.html', space=space, user=user)


# GET /spaces/new
# Returns a form to create a new spaces
@app.route('/space/new', methods=['GET'])
def get_new_space():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.find(session['user_id'])
    return render_template('list_a_space.html', user=user)

# Create a new space - POST /space - INSERT INTO spaces VALUES ...
@app.route('/space', methods=['POST'])
def create_new_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    new_space = Space(
        None,
        request.form['name'],
        request.form['location'],
        request.form['description'],
        request.form['price'],
        request.form['user_id'])
    new_space = repository.create(new_space)
    user = repository.find(session['user_id'])
    return redirect(f"/space/{space.id}", user=user)


# -------- USERS ----------

# Get details of all users - GET /user - SELECT * FROM users

@app.route('/user', methods=['GET'])
def get_all_users():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
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

@app.route('/login/submit', methods=['POST'])
def submit_login_request():
    # making the connection to the database
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    
    # Clearing session (assuming you want to clear the session upon login)
    session.clear()
    
    # Storing the user's entered credentials in a dictionary
    entered_email = request.form.get('email_address')
    entered_password = request.form.get('password')
    
    # Getting the user from the database based on the entered email
    user = repository.find_by_email(entered_email)
    
    if user is not None and user['password'] == entered_password:
        # Set the user ID in the session upon successful login
        session['user_id'] = user['id']
        return redirect("/spaces")
    else:
        return render_template('login.html', invalid_login=True)

# Submit a login request - POST /login/submit - SELECT password FROM users WHERE email=<email>
# @app.route('/login/submit', methods=['POST'])
# def submit_login_request():
#     # making the connection to the database
#     # session.clear()
#     connection = get_flask_database_connection(app)
#     repository = UserRepository(connection)
#     user = repository.find(session['user_id'])
#     # storing the user's entered credentials in a dictionary
#     entered_email = request.form.get('email_address')
#     entered_password = request.form.get('password')
#     # getting the user in dictionary format which matches the email from the database
#     stored_password = repository.find_by_email(entered_email).get('password')
#     if entered_password == stored_password:
#         session['user_id'] = repository.find_by_email(entered_email).get('id')
#         return redirect("/spaces")
#     else:
#         return render_template('login.html', invalid_login=True)


# -------- REQUESTS ----------
# Use this code to retrieve logged in user id --> user_id = session.get('user_id')



# Get booking requests by booker - GET /requests/<booker_id> - SELECT * FROM bookings WHERE booker_id = <booker_id>

@app.route('/requests/booker/<int:booker_id>', methods=['GET'])
def get_requests_by_booker(booker_id):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
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


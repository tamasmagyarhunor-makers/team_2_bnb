from playwright.sync_api import Page, expect



# --------- LOGIN ------------------------------------------------

def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")
    # We look at the <h1> tag
    # strong_tag = page.locator("p")
    tag = page.locator("h1")
    print(str(tag))
    # We assert that it has the text "This is the homepage."
    expect(tag).to_have_text("Welcome to MakersBnB")




def test_get_login(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/login")
    # We look at the <h1> tag
    tag = page.locator("h1")
    # We assert that it has the text "This is the homepage."
    expect(tag).to_have_text("Log in to MakersBnB")    




def test_get_sign_up(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/sign_up")
    # We look at the <h1> tag
    tag = page.locator("h1")
    # We assert that it has the text "This is the homepage."
    expect(tag).to_have_text("Sign up to MakersBnB")    



# -------- SPACES -------------------------------------------


#test to list all the spaces
def test_get_all_space(db_connection, page, test_web_address):
    # We seed our database with the book store seed file
    db_connection.seed("seeds/bnb_seed.sql")

    # We load a virtual browser and navigate to the /space page
    page.goto(f"http://{test_web_address}/spaces")

    # # We look at all the <li> tags
    list_items = page.locator("li")

    # We assert that it has the spaces in it
    expect(list_items).to_contain_text([
        "Cozy Studio Apartment",
        "Spacious Loft",
        "Beach House",
    ])



#test to get a single space
def test_get_space(db_connection, page, test_web_address):
    db_connection.seed("/seeds/bnb_seed.sql")

    # We visit the space page
    page.goto(f"http://{test_web_address}/space")
    # Click the link with the text 'Cozy Studio Apartment, New York, A small but comfortable studio in downtown., 100.00, 1'
    page.click("Cozy Studio Apartment, New York, A small but comfortable studio in downtown., 100.00, 1")
    
    # The virtual browser acts just like a normal browser and goes to the next
    # page without us having to tell it to.

    # Then we look for specific test classes that we have put into the HTML
    # as targets for our tests to look for. This one is called `t-title`.
    # You can see it in `templates/space/listing.html`     <---- this needs to be created, if you create this make sure you delete this line
    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("name: Cozy Studio Apartment")

    location_element = page.locator(".t-location")
    expect(location_element).to_have_text("location: New York")
    
    description_element = page.locator(".t-description")
    expect(description_element).to_have_text("description: A small but comfortable studio in downtown.")

    price_element = page.locator(".t-price")
    expect(price_element).to_have_text("price: 100.00")

    user_id_element = page.locator(".t-user_id")
    expect(user_id_element).to_have_text("user_id: 1")




#test for new listing form pages
def test_get_new_listing_form(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/space/new")
    # We look at the <p> tag
    strong_tag = page.locator("p")
    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("Create a new listing")




#test for creating a new listing
def test_create_space(db_connection, page, test_web_address):
    db_connection.seed("/seeds/bnb_seed.sql")
    page.goto(f"http://{test_web_address}/space/new")

    page.click("text=List a space")

    # Then we fill out the field with the name attribute 'name'
    page.fill("input[name='name']", "Luxurious villa")
    # And the field with the name attribute 'location', etc....
    page.fill("input[name='location']", "bali")
    page.fill("input[name='description']", "A magnificent seaside villa with a personal chef")
    page.fill("input[name='price']", "700.00")
    page.fill("input[name='user_id']", "5") #should the user id be generated? if so it shouldnt be filled. comfused rn
    
    name_element = page.locator(".t-name")
    expect(name_element).to_have_text("name: Luxurious villa")

    location_element = page.locator(".t-location")
    expect(location_element).to_have_text("location: bali")
    
    description_element = page.locator(".t-description")
    expect(description_element).to_have_text("description: A magnificent seaside villa with a personal chef")

    price_element = page.locator(".t-price")
    expect(price_element).to_have_text("price: 400.00")

    user_id_element = page.locator(".t-user_id")
    expect(user_id_element).to_have_text("user_id: 5")



# -------- USERS -----------------------------------------------------------


#test to get one specific user, a link to the user will be found on the space they have listed
def test_get_all_users(db_connection, page, test_web_address):
    db_connection.seed("/seeds/bnb_seed.sql")
    # We visit the space page in question
    page.goto(f"http://{test_web_address}/space")
    # Click choose a certain space
    page.click("Cozy Studio Apartment, New York, A small but comfortable studio in downtown., 100.00, 1")

    page.click("Your host details")  # the route on this link will be /user/1. user 1 listed this property as shown above

    #after navigating to the user through their listing page, we check that some details are present on this page
    first_name_element = page.locator(".t-first_name")
    expect(first_name_element).to_have_text("first_name: john")

    phone_number_element = page.locator(".t-phone_number")
    expect(phone_number_element).to_have_text("Phone_number: 07926345037")
    
    # description_element = page.locator(".t-description")
    # expect(description_element).to_have_text("description: i enjoy long walks on the beach and cooking for friends")













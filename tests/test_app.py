from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/home")
    # We look at the <p> tag
    strong_tag = page.locator("p")
    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


#test to list all the spaces
def test_get_all_space(db_connection, page, test_web_address):
    # We seed our database with the book store seed file
    db_connection.seed("/seeds/database_connection.sql")

    # We load a virtual browser and navigate to the /books page
    page.goto(f"http://{test_web_address}/space")

    # We look at all the <li> tags
    list_items = page.locator("li")

    # We assert that it has the books in it
    expect(list_items).to_have_text([
        "Cozy Studio Apartment, New York, A small but comfortable studio in downtown., 100.00, 1"
        "Spacious Loft, Los Angeles, A modern loft with city views., 150.00, 2"
        "Beach House, Miami, A beautiful house steps away from the beach., 200.00"
    ])


#test to get a single space
def test_get_space(db_connection, page, test_web_address):
    db_connection.seed("/seeds/database_connection.sql")

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




#test for creating a new listing
def test_create_space(db_connection, page, test_web_address):
    db_connection.seed("/seeds/database_connection.sql")
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

#test for new listing form pages
def test_get_new_listing_form(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/space/new")
    # We look at the <p> tag
    strong_tag = page.locator("p")
    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("Create a new listing")


    






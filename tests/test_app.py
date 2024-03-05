from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_home(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/home")
    # We look at the <p> tag
    strong_tag = page.locator("p")
    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")








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






#test for get all spaces
def test_get_spaces(db_connection, page, test_web_address):
    db_connection.seed("/seeds/database_connection.sql")

    # We visit the space page
    page.goto(f"http://{test_web_address}/space")
    # Click the link with the text 'Cozy Studio Apartment, New York, A small but comfortable studio in downtown., 100.00, 1'
    page.click("Cozy Studio Apartment, New York, A small but comfortable studio in downtown., 100.00, 1")
    
    # The virtual browser acts just like a normal browser and goes to the next
    # page without us having to tell it to.

    # Then we look for specific test classes that we have put into the HTML
    # as targets for our tests to look for. This one is called `t-title`.
    # You can see it in `templates/space/show.html`
    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("name: Cozy Studio Apartment")

    author_element = page.locator(".t-location")
    expect(author_element).to_have_text("location: New York")
    
    author_element = page.locator(".t-description")
    expect(author_element).to_have_text("description: A small but comfortable studio in downtown.")

    author_element = page.locator(".t-price")
    expect(author_element).to_have_text("price: 100.00")


    author_element = page.locator(".t-user_id")
    expect(author_element).to_have_text("user_id: 1")



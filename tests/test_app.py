from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."

    expect(tag).to_have_text("Welcome to MakersBnB")


def test_get_login(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/login")

    # We look at the <p> tag
    tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(tag).to_have_text("Log in to MakersBnB")    

def test_get_sign_up(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/sign_up")

    # We look at the <p> tag
    tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(tag).to_have_text("Sign up to MakersBnB")      

    expect(strong_tag).to_have_text("This is the homepage.")



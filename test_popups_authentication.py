from playwright.sync_api import sync_playwright, expect, Playwright, Page
import pytest

# TO handle authentication popup we have 2 ways

# Approach 1. direct - inject userlogin with url (not recommended)
# Ex - https://admin:admin@the-internet.herokuapp.com/basic_auth

# Approach 2. using context - we can pass user and password along with the context (recommended)
# Ex - https://the-internet.herokuapp.com/basic_auth


# Approach 1. direct - inject userlogin with url (not recommended)
# Ex - https://admin:admin@the-internet.herokuapp.com/basic_auth

def test_authpopup(page:Page):
   page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
   page.wait_for_load_state()
   expect(page.locator("text=Congratulations")).to_be_visible()


# Approach 2. using context - we can pass user and password along with the context (recommended)
# Ex - https://the-internet.herokuapp.com/basic_auth

def test_authpopup_context(playwright:Playwright):
   browser=playwright.chromium.launch(headless=False) # created browser
   context=(browser.new_context(http_credentials={"username":"admin","password":"admin"})) # created context + passed credentials
   page=context.new_page() # created new page

   page.goto("https://the-internet.herokuapp.com/basic_auth")
   page.wait_for_load_state()
   expect(page.locator("text=Congratulations")).to_be_visible()
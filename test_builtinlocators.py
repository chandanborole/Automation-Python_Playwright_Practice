from playwright.sync_api import Page , expect
def test_getbyalttext(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    playwright_logo = page.get_by_alt_text("logo image")
    expect(playwright_logo).to_be_visible()


from playwright.sync_api import Page , expect
def test_getbytext(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.wait_for_timeout(30000)
    text = page.get_by_text("important")
    expect(text).to_be_visible()


from playwright.sync_api import Page, expect
def test_getbyrole(page:Page):
     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
     page.wait_for_timeout(5000)
     page.get_by_role("link", name="Home").click()


from playwright.sync_api import Page , expect
def test_getbylabel(page:Page):
     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
     page.get_by_label("Email Address:").fill("automationqa@gmail.com")
     page.get_by_label("Password:").fill("automationqa@gmail.com")
     page.get_by_label("Your Age:").fill("21")


from playwright.sync_api import Page , expect
def test_getbyplaceholder(page:Page):
     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
     page.get_by_placeholder("Enter your full name").fill("automation")
     page.get_by_placeholder("Phone number(xxx - xxx - xxxx)").fill("1234567890")
     page.get_by_placeholder("Type your message here...").fill("qa")
     page.get_by_placeholder("Search products...").fill("python")


from playwright.sync_api import Page , expect
def test_getbytitle(page:Page):
     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
     title = page.get_by_title("Home page link")
     expect(title).to_have_text("Home")
     page.wait_for_timeout(10000)


from playwright.sync_api import Page , expect
def test_getbytestid(page:Page):
     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
     testid = page.get_by_test_id("edit-profile-btn")
     expect(testid).to_have_text("Edit Profile")

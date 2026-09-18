from playwright.sync_api import sync_playwright, expect, Page, Playwright

# Browser --> Context --> Page/s
# to create browser need to use Playwright fixture

def test_browsercontext(playwright: Playwright):

    # Insted of this you can use browser = playwright.chromium.launch(headless=False)
    # chromium = playwright.chromium
    # browser=chromium.launch()

    # created new own browser
    browser = playwright.chromium.launch(headless=False)

    # created own context
    context = browser.new_context()

    # you can create multiple context , PFB example
    # context1 = browser.new_context()
    # context2 = browser.new_context()

    page1 = context.new_page()  # created page1
    page2 = context.new_page()  # created page2 , you can create multiple pageobject , page refer to tab , popup , browser window

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")

# to create browser you can create any one statement
# check code below test_browsercontext function 

# 1.
# chromium=playwright.chromium
# browser=chromium.launch()

# or

# 2.
# browser=playwright.chromium.launch(headless=False) # created browser
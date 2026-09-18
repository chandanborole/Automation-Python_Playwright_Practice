from playwright.sync_api import sync_playwright, expect, Playwright

def test_hande_popups(playwright:Playwright):
   browser=playwright.chromium.launch(headless=False) # created browser
   context=browser.new_context() # created context
   page=context.new_page() # created page

   page.goto("https://testautomationpractice.blogspot.com/")

   # registration of event
   # we can use two ways for create registration of event
   # 1. create user define customised function
   # 2. use inbuit LAMBDA function

   # 1. create user define customised function (not recommended)
   # in bracket popup is event name we need to pass
   # wait_for_load_state method will wait till popup open
   # page.on is event listener

   # def handle_popup(popup): # this is registration of event
   #     popup.wait_for_load_state()
   #
   # page.on("popup",handle_popup) # page.on will handle popup , popup is event , handle_popup is function name

   # 2. use inbuit LAMBDA function (recommended)
   # page.on is event listener & will handle popup
   # LAMBDA is inbuilt function
   # popup is register event
   # popup.wait_for_load_state() method will wait till popup open

   page.on("popup",lambda popup:popup.wait_for_load_state())

   # click button
   page.locator("#PopUp").click()

   # capture all pageobject number
   all_pages_count=context.pages
   print("Total number of popups/pageobject:",len(all_pages_count))

   # capture all popup pageobject urls
   for popup in all_pages_count:
       print("Popup/Page URL- ", popup.url)
       title=popup.title()
       if "Playwright" in title:
           popup.locator(".getStarted_Sjon").click()
           expect(popup).to_have_title("Installation | Playwright")
           popup.close() # it will close the playwright popup/window

   context.close()
   browser.close()
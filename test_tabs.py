from playwright.sync_api import sync_playwright, expect, Playwright

# handle 2 tabs from 1 browser

def test_handle_tabs(playwright:Playwright):
   browser=playwright.chromium.launch(headless=False) # created browser
   context=browser.new_context() # created context
   parentpage=context.new_page() # created page

   parentpage.goto("https://testautomationpractice.blogspot.com/")

   # register an event for handle tab
   # parentpage.on is event listener & will handle tab
   # LAMBDA is inbuilt function
   # page is register event
   # page.wait_for_load_state() method

   parentpage.on("page",lambda page:page.wait_for_load_state())

   parentpage.locator("button:has-text('New Tab')").click()

   # capture page number
   all_pages=context.pages
   print("Number of tabs/pageobject:====>",len(all_pages))

   print("Title of parent page:",all_pages[0].title())
   print("Title of child page/tab:", all_pages[1].title())

   childpage=all_pages[1]

   print("URL of the child page- ",childpage.url)

   context.close()
   browser.close()
from playwright.sync_api import Playwright, sync_playwright, expect

def test_capture_trace(playwright:Playwright):
   browser=playwright.chromium.launch(headless=False) # created browser
   context=browser.new_context() # created context

   # starting the trace
   context.tracing.start(screenshots=True,snapshots=True)

   # created page
   page=context.new_page()

   page.goto('https://www.demoblaze.com/index.html')
   page.locator('#login2').click()
   page.locator('#loginusername').fill('automation')
   page.locator('#loginpassword').fill('test@123')
   page.locator("button:has-text('Log in')").click()

   expect(page.locator("#logout2")).to_be_visible()
   expect(page.locator('#nameofuser')).to_contain_text('Welcome automation')

   # stopping the trace
   # it will create zip file. we can open this file using command prompt or using website to oprn file just drag n drop it ll automatically open zip file
   # cmd for open file - playwright show-trace FILENAME
   context.tracing.stop(path="trace.zip")

   context.close()
   browser.close()
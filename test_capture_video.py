from playwright.sync_api import Playwright, sync_playwright, expect

def test_capture_video(playwright:Playwright):
   browser=playwright.chromium.launch(headless=False) # created browser
   context=browser.new_context(
          record_video_dir="videos/",
          record_video_size={"width":1024,"height":768}
   ) # created context + passed record_video_dir & record_video_size information
   page=context.new_page() # created page

   page.goto('https://www.demoblaze.com/index.html')
   page.locator('#login2').click()
   page.locator('#loginusername').fill('automation')
   page.locator('#loginpassword').fill('test@123')
   page.locator("button:has-text('Log in')").click()

   expect(page.locator("#logout2")).to_be_visible()
   expect(page.locator('#nameofuser')).to_contain_text('Welcome automation')

   context.close()
   browser.close()
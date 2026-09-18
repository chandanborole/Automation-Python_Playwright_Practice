from playwright.sync_api import sync_playwright, expect, Page
import time
import datetime

def test_capture_screenshot(page:Page):
   page.goto("https://demowebshop.tricentis.com/")

   # you can use any statement from a or b

   # a. capture screenshot in not understandable format (ex - homepage.png12345678)
   timestamp=str(int(time.time()))

   # b. capture screenshot in understandable format (ex - homepage.png2026813142525)
   timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

   # 1. capture page screenshot (partially/visible page)
   page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

   # 2. capture full page screenshot
   page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page=True)

   # 3. capture element/specific section of the page screenshot
   logo=page.locator("img[alt='Tricentis Demo Web Shop']")
   logo.screenshot(path=f"screenshots/logo_{timestamp}.png")

   # 4. capture specific section
   featuredproducts=page.locator(".product-grid.home-page-product-grid")
   featuredproducts.screenshot(path=f"screenshots/featuredproducts_{timestamp}.png")
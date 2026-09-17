import pytest
from playwright.sync_api import sync_playwright, expect,Page

# mouse_hover
def test_mouse_hover(page:Page):
   page.goto("https://testautomationpractice.blogspot.com/")

   # pointme is hovering on element and hover is method in PR
   pointme_button=page.locator(".dropbtn")
   pointme_button.hover()

   # capture element from pointme_button hower
   # you can use any 1 from below statement
   # laptops=page.locator('.dropdown-content a').nth(1)
   # or (here we capture child element from parent)
   laptops=page.locator('.dropdown-content a:nth-child(2)')
   laptops.hover()


# rightclick
def test_mouse_rightclick(page:Page):
   page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

   # capture element - right click button
   button=page.locator(".context-menu-one")
   button.click(button = "right") # button = "right" performs right click action - right , left , middle (left is default)


# doubleclick
def test_mouse_doubleclick(page:Page):
   page.goto("https://testautomationpractice.blogspot.com/")

   # capture element - double click
   copytext_button=page.locator("button[ondblclick='myFunction1()']")
   copytext_button.dblclick() # dblclick performs double click action

   # 2nd field validation for same text copied or not
   field2=page.locator("#field2")
   expect(field2).to_have_value("Hello World!")


# draganddrop
def test_mouse_draganddrop(page:Page):
   page.goto("https://testautomationpractice.blogspot.com/")

   source_element=page.locator("#draggable")
   target_element=page.locator("#droppable")

   # approach 1 : manual drag using hover()
   # source.hover()
   # page.mouse.down()
   # target.hover()
   # page.mouse.up()

   # approach 2 (recommended) : drag_to()
   # drag_to() is method
   source_element.drag_to(target_element)
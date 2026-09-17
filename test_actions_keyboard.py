import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_keyboardactions(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Capture element
    input1 = page.locator("#input1")

    # 1. focus on input1
    # focus = receives keyboard focus and can accept keyboard input
    input1.focus()

    # 2. provide the text in input1
    # insert_text is similar to fill method
    page.keyboard.insert_text("welcome")

    # 3. Control+A
    # press is method to press keys
    page.keyboard.press("Control+A")

    # 4. Control+C
    # press is method to press keys
    page.keyboard.press("Control+C")

    # 5. press Tab key 2 times to navigate/focus on input2
    # press is method to press keys
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 6. Control+V - paste the text inside the 2nd inputbox - input2
    page.keyboard.press("Control+V")

    # 7. press Tab key 2 times to navigate/focus on input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 8. Control+V - Paste the text inside the 3rd inputbox - input3
    page.keyboard.press("Control+V")

    # capture 2nd and 3rd input box
    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    # assertion
    expect(input2).to_have_value("welcome")
    expect(input3).to_have_value("welcome")

    page.wait_for_timeout(5000)

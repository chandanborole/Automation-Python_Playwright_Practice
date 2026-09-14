from playwright.sync_api import Page , expect

def test_tagandid(page:Page):
    # tag and id
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("mobiles")
    page.wait_for_timeout(5000)


def test_tagandclass(page: Page):
    # tag and class
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text").fill("mobiles")
    page.wait_for_timeout(5000)


def test_tagandattribute(page:Page):
    # tag and attribute
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[name=q]").fill("mobiles")
    page.wait_for_timeout(5000)


def test_tagclassandattribute(page:Page):
    # tag , class and attribute
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text[name=q]").fill("mobiles")
    page.wait_for_timeout(5000)

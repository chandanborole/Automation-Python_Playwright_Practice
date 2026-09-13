from playwright.sync_api import Page , expect

def test_singleselect_dropdown(page:Page):
  page.goto("https://testautomationpractice.blogspot.com/")

  # 3 ways to select option from the dropdown
  # select_option is a built-in method used to interact with and select one or more options inside standard HTML <select> dropdown elements

  # 1. by label
  page.locator("#country").select_option("India")
  # OR
  page.locator("#country").select_option(label="India")

  # 2. by value
  page.locator("#country").select_option("germany")
  # OR
  page.locator("#country").select_option(value="germany")

  # 3. by index (starts from 0) (in single_select_dropdown we have to explicitly provide index keyword)
  page.locator("#country").select_option(index=3)

  page.wait_for_timeout(5000)


def test_multiselect_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 1. by label
    page.locator("#colors").select_option(["Red", "Blue", "Green"])

    # 2. by value (in multi_select_dropdown we have to explicitly provide value keyword)
    page.locator("#colors").select_option(value=["red", "white", "green"])

    # 3. by index (starts from 0) (in multi_select_dropdown we have to explicitly provide index keyword)
    page.locator("#colors").select_option(index=[4, 2])
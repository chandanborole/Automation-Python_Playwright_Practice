from playwright.sync_api import Page , expect

def test_static_webtable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Locating table
    static_table = page.locator("table[name='BookTable'] tbody")
    expect(static_table).to_be_visible()

    # Count number of rows in table
    rowcount = page.locator("table[name='BookTable'] tbody tr")
    expect(rowcount).to_have_count(7)

    # Count total number of column/header in table
    headercount = page.locator("table[name='BookTable'] tbody tr th")
    expect(headercount).to_have_rows(4)

    # Print column count
    header_count = headercount.count()
    print("Header_Count-->" , header_count)

    # Read data from a second row of table
    # assertion on value is not available for python playwright so we can validate text , refer expect line
    second_row_data = page.locator("table[name='BookTable'] tbody tr td").nth(1)
    second_row_texts = second_row_data.all_inner_texts()
    print("Second_Row_Data" , second_row_texts)
    expect(second_row_data).to_have_text(["JAVA" , "ONLINE" , "5000"])

    # Print data individually using loop
    for text in second_row_texts:
        print(text)
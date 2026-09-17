import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_fileupload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Capture single - choose file element
    page.locator("#singleFileInput").set_input_files("FILE UPLOAD . PATH OF LOCAL MACHINE")

    # Click on Upload Single File button
    page.locator("button:has-text('Upload Single File')").click()

    # Capture Upload Single File locator
    upload_single_file = page.locator("#singleFileStatus")

    # Validation message after upload file
    expect(upload_single_file).to_contain_text("Single file selected: Screenshot 2026-07-27 144307.jpg, Size: 78426 bytes, Type: image/jpeg")


def test_multiplefileupload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Capture files to upload in LIST collection
    files = ["file/test1.txt" , "file/test2.txt"]

    # Capture multiple - choose file element
    page.locator("#multipleFilesInput").set_input_files(files)

    # Click on Upload Multiple Files button
    page.locator("button:has-text('Upload Multiple Files')").click()

    # Capture Upload Single File locator
    upload_multiple_files = page.locator("#multipleFilesInput")

    # Validation message after upload file
    expect(upload_multiple_files).to_contain_text("test1.txt")
    expect(upload_multiple_files).to_contain_text("test2.txt")
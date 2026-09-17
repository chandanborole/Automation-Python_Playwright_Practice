import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_filedownload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Capture enter text element
    page.locator("inputText").fill("HI")

    # Click Generate and Download Text File button (this will generate lonk to download)
    page.locator("generateTxt").click()

    # # Approach 1 - to create user define function (not recommended)
    # # Before download need to register event
    # # in bracket download is event name
    # def handle_download(download):
    #     download.save_as("downloads/test.txt")
    # page.on("download", handle_download)

    # Approach 1 - LAMBDA function (recommended)
    # statement explanation as below - "download" , lambda download: download.save_as("downloads/test.txt"))
    # download is register event , lambda is function ,
    # download.save_as("downloads/test.txt" - dowload is event , save_as is method used to save a downloaded file
    # ("downloads/test.txt")) - filepath (save_as(path) copies that temporary file to a specific folder and name you choose)
    page.on("download" , lambda download: download.save_as("downloads/test.txt"))

    # Click Download Text File link
    page.locator("txtDownloadLink").click()
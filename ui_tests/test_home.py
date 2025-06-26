import pytest
from playwright.sync_api import sync_playwright
from time import sleep
import os

def test_homepage_shows_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        assert "Hello Uzziel!" in page.content()

        sleep(2)

        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/test_homepage.png")

        browser.close()
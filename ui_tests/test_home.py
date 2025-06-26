import pytest
from playwright.sync_api import sync_playwright
from time import sleep
import os

def test_homepage_shows_username():
    test_name = "🧪 Test: Homepage displays greeting for user"
    print(f"\n{test_name}\n{'-' * len(test_name)}")

    with sync_playwright() as p:
        is_ci = os.getenv("CI") == "true"
        browser = p.chromium.launch(headless=is_ci)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        try:
            assert "Hello Uzziel!" in page.content(), \
                "❌ Text 'Hello Uzziel!' not found on the page"
            print("✅ Status: PASSED")
        except AssertionError as e:
            print("❌ Status: FAILED")
            raise e
        finally:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path="screenshots/test_homepage.png")
            browser.close()
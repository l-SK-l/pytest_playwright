from pages.login_page import LoginPage
from playwright.sync_api import Page
puth_screenshots = "test-results/screenshots/check_login_page/"

def test_check_login_page(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.load()
    login_page.check_title()
    login_page.screenshot()

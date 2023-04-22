from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_check_login_page(
    page: Page,
    login_page: LoginPage) -> None:
    login_page.load()
    login_page.check_title()

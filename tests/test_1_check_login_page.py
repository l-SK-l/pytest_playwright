import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_check_login_page(
        page: Page,
        login_page: LoginPage) -> None:
    """
    Check that the login page is available and displayed
    """
    login_page.load()
    # Checking for title availability
    login_page.check_title()

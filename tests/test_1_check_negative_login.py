import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_check_login_page(
        page: Page,
        login_page: LoginPage) -> None:
    """
    Check that a user with an invalid password cannot login
    """
    login_page.load()
    # Аuthorization with an invalid password, under the user "Obama"
    login_page.login_obama()

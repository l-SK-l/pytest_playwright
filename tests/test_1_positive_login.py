import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_positive_login(
        page: Page,
        login_page: LoginPage) -> None:
    """
    Check that the administrator can login and logout
    """
    login_page.load()
    # Login as Admin
    login_page.login_admin()
    # Logout
    login_page.logout()

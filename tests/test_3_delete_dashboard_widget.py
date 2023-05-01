import pytest
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from playwright.sync_api import Page


def test_delete_dashboard_widget(
        page: Page,
        login_page: LoginPage,
        dashboard_page: DashboardPage) -> None:
    """
    Check if the widget can be deleted
    """
    # Login
    login_page.login_admin()
    # Open Main dashboard page
    dashboard_page.load()
    # Edit dashboard
    dashboard_page.edit_dashboard()
    # Delete Network security log dashboard
    dashboard_page.del_network_security_dashboard()
    dashboard_page.save_dashboard_page()
    # Check a deleted widget
    dashboard_page.word_is_not_on_page('Network security log')
    # Logout
    dashboard_page.logout()

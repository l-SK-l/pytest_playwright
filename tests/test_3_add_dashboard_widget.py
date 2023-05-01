import pytest
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from playwright.sync_api import Page


@pytest.mark.skip('Unstable Date')
def test_dashboard_widget(
        page: Page,
        login_page: LoginPage,
        dashboard_page: DashboardPage) -> None:
    """
    Check that you can create a new widget on the main page and on an additional page
    """
    # Login
    login_page.login_admin()
    # Open Main dashboard page
    dashboard_page.load()
    # Create a new dashboard
    dashboard_page.add_new_dashboard()
    # Open dashboard
    dashboard_page.open_custom_dashboard()
    # Edit dashboard
    dashboard_page.edit_dashboard()
    # Edit a new widget
    # dashboard_page.edit_default_widget()
    dashboard_page.save_dashboard_page()
    # Logout
    dashboard_page.logout()

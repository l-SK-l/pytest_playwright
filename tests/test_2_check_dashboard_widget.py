import pytest
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from playwright.sync_api import Page


def test_check_dashboard_widget(
        page: Page,
        login_page: LoginPage,
        dashboard_page: DashboardPage) -> None:
    """
    Checking that the default widgets are displayed and working
    """
    # Login
    login_page.login_admin()
    # Open Main dashboard page
    dashboard_page.load()
    # Check Access server widget
    dashboard_page.check_widget_access_server_available()
    dashboard_page.check_widget_access_server_has_0_connections()
    dashboard_page.open_widget_access_server()
    dashboard_page.check_widget_access_server_has_0_connections_inside()
    # Check VPN widget
    dashboard_page.check_widget_vpn_available()
    # Check Network ifaces widget
    dashboard_page.check_widget_Network_ifaces_available()
    # Chect Network security widget
    dashboard_page.check_widget_Network_security_available()
    # Create events + check
    # Logout
    dashboard_page.logout()

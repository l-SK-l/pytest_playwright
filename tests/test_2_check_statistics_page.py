import pytest
from pages.login_page import LoginPage
from pages.statistics import StatisticsPage
from playwright.sync_api import Page


# @pytest.mark.skip('Not Ready')
def test_check_statistics_page(
        page: Page,
        login_page: LoginPage,
        statistics_page: StatisticsPage) -> None:
    """
    Checking the Statistics page
    """
    # Login
    login_page.login_admin()
    # Open Statistics page
    statistics_page.load()
    # Check Top15 widget
    statistics_page.check_widget_top15_available()
    # Duplicate dashboard
    statistics_page.duplicate_dashboard()
    statistics_page.open_duplicate_dashboard()
    statistics_page.check_widget_top15_available()
    # Add new dashboard
    statistics_page.add_new_dashboard()
    statistics_page.open_new_dashboard()
    statistics_page.check_empty_widget()
    # Create events + check
    # Logout
    statistics_page.logout()

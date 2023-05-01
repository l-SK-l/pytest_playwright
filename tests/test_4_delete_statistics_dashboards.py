import pytest
from pages.login_page import LoginPage
from pages.statistics import StatisticsPage
from playwright.sync_api import Page


# @pytest.mark.skip('Not Ready')
def test_detele_statistics_dashboards(
        page: Page,
        login_page: LoginPage,
        statistics_page: StatisticsPage) -> None:
    """
    Checking the removal of dashboards to the Statistics page
    """
    # Login
    login_page.login_admin()
    # Open Statistics page
    statistics_page.load()
    # Delete "new_dashboard"
    statistics_page.delete_new_dashboard()
    statistics_page.word_is_not_on_page('new_dashboard')
    # Delete "duplicate_dashboard"
    statistics_page.delete_duplicate_dashboard()
    statistics_page.word_is_not_on_page('duplicate_dashboard')
    # Logout
    statistics_page.logout()

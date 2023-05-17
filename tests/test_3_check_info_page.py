import pytest
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from playwright.sync_api import Page
# from tests.conftest import current_version


def test_check_info_page(
        current_year,
        current_version,
        page: Page,
        login_page: LoginPage,
        dashboard_page: DashboardPage) -> None:
    """
    Checking the operation of the information window with the version and dates
    """
    # Login
    login_page.login_admin()
    # Checking the version
    dashboard_page.open_about()
    print(f"Current Year: {current_year}, Current Version: {current_version}" )
    dashboard_page.page.get_by_role("button", name=f"SC logo Dashboard and audit \"Continent 4\" Version {current_version} Our contacts support@securitycode.ru Site www.securitycode.net © 1995-{current_year} Security Code").get_by_role("button",
        name=f"SC logo Dashboard and audit \"Continent 4\" Version {current_version} Our contacts support@securitycode.ru Site www.securitycode.net © 1995-{current_year} Security Code", exact=True).filter(has_text=f"Dashboard and audit \"Continent 4\"Version{current_version}Our contactssupport@securityco").locator("button").click()
    # Logout
    dashboard_page.logout()

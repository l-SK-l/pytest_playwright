from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from playwright.sync_api import Page
from tests.conftest import corrent_version, corrent_year


def test_check_info_page(
    page: Page,
    login_page: LoginPage,
    dashboard_page: DashboardPage) -> None:
    # Login
    login_page.login_admin()
    # Checking the version
    dashboard_page.open_about()
    dashboard_page.page.get_by_role("button", name=f"SC logo Dashboard and audit \"Continent 4\" Version {corrent_version} Our contacts support@securitycode.ru Site www.securitycode.net © 1995-2022 Security Code").get_by_role("button",
        name=f"SC logo Dashboard and audit \"Continent 4\" Version {corrent_version} Our contacts support@securitycode.ru Site www.securitycode.net © 1995-{corrent_year} Security Code", exact=True).filter(has_text=f"Dashboard and audit \"Continent 4\"Version{corrent_version}Our contactssupport@securityco").locator("button").click()
    # Logout
    dashboard_page.logout()

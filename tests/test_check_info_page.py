import pytest
import re
from playwright.sync_api import Page, expect
from conftest import corrent_version, corrent_year
puth_screenshots = "test-results/screenshots/check_that_monitoring_work/"


def test_check_info_page(page: Page, ) -> None:
    page.goto("https://mon-aes/login-page")
    # Login as admin
    page.get_by_role("button", name="Войти").click()
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("admin")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("Test123!")
    page.get_by_role("button", name="Войти").click()
    # Checking the version
    page.get_by_role("button", name="About").click()
    page.screenshot(path=f"{puth_screenshots}version_logo.png")
    page.get_by_role("button", name=f"SC logo Dashboard and audit \"Continent 4\" Version {corrent_version} Our contacts support@securitycode.ru Site www.securitycode.net © 1995-2022 Security Code").get_by_role("button",
        name=f"SC logo Dashboard and audit \"Continent 4\" Version {corrent_version} Our contacts support@securitycode.ru Site www.securitycode.net © 1995-{corrent_year} Security Code", exact=True).filter(has_text=f"Dashboard and audit \"Continent 4\"Version{corrent_version}Our contactssupport@securityco").locator("button").click()
    # Exit
    page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
    page.get_by_role("button", name="Exit").get_by_role(
        "button", name="Exit", exact=True).filter(has_text="Exit").click()
    page.get_by_role("button", name="Proceed", exact=True).click()

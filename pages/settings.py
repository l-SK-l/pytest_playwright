from playwright.sync_api import Page, expect
import re
import pytest


class SettingsPage:

    URL = 'https://mon-aes/settings/mailserver'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def edit_settings_page(self) -> None:
        self.page.get_by_role("button", name="Edit").click()

    def enable_smtp(self) -> None:
        self.page.locator("#switch_enabled").get_by_role("button").click()

    def enable_whois(self) -> None:
        self.page.locator("label").click()

    def fill_smtp_fields(self) -> None:
        self.page.locator("input[name=\"host\"]").click()
        self.page.locator("input[name=\"host\"]").fill("smtp_server")
        self.page.locator("input[name=\"port\"]").click()
        self.page.locator("input[name=\"port\"]").fill("587")
        self.page.locator("input[name=\"username\"]").click()
        self.page.locator("input[name=\"username\"]").fill("test_user")
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill("test_password")
        self.page.locator("input[name=\"sender\"]").click()
        self.page.locator("input[name=\"sender\"]").fill("test_user@test.com")

    def fill_whois_field(self) -> None:
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("178.237.222.123")

    def enable_tls(self) -> None:
        self.page.locator("#smtpSecurity").get_by_role("button").click()

    def save_sittings_page(self) -> None:
        self.page.get_by_role("button", name="Save").click()

    def open_smtp_page(self) -> None:
        self.page.get_by_role("button", name="SMTP", exact=True).click()

    def open_whois_page(self) -> None:
        self.page.get_by_role("button", name="WhoIs", exact=True).click()

    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role(
            "button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

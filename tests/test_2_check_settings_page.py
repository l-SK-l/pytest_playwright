import pytest
from pages.login_page import LoginPage
from pages.settings import SettingsPage
from playwright.sync_api import Page


def test_check_statistics_page(
        page: Page,
        login_page: LoginPage,
        settings_page: SettingsPage) -> None:
    """
    Checking the Settings page: SMTP and WhoIs
    """
    # Login
    login_page.login_admin()
    # Open Statistics page
    settings_page.load()
    # Enable SMTP
    settings_page.open_smtp_page()
    settings_page.edit_settings_page()
    settings_page.enable_smtp()
    settings_page.fill_smtp_fields()
    settings_page.save_sittings_page()
    settings_page.edit_settings_page()
    # Enable WhoIs
    settings_page.open_whois_page()
    settings_page.edit_settings_page()
    settings_page.enable_whois()
    settings_page.fill_whois_field()
    settings_page.save_sittings_page()
    settings_page.edit_settings_page()
    # Logout
    settings_page.logout()

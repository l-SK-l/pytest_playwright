import pytest
from pages.login_page import LoginPage
from pages.journals import JournalsPage
from playwright.sync_api import Page


def test_check_download_logs(
        page: Page,
        login_page: LoginPage,
        journals_page: JournalsPage) -> None:
    """
    Check the ability to export logs in CSV format. Validating the CSV format
    """
    # Login as Admin
    login_page.login_admin()
    # Open System journals
    journals_page.load()
    # Open logs
    journals_page.open_system_section()
    # Select all visible rows with logs
    journals_page.select_all_visible_rows_system()
    # Export CSV Logs
    journals_page.export_csv_logs()
    # Start waiting for the download
    journals_page.wait_and_confirm('test-results/logs.csv')
    # Logout
    journals_page.logout()
    # Check logs
    journals_page.validate_csv_log('test-results/logs.csv')

import pytest
from pages.login_page import LoginPage
from pages.journals import JournalsPage
from playwright.sync_api import Page


def test_check_download_logs(
        page: Page,
        login_page: LoginPage,
        journals: JournalsPage) -> None:
    """
    Check the ability to export logs in CSV format. Validating the CSV format
    """
    # Login as Admin
    login_page.login_admin()
    # Open System journals
    journals.load()
    # Open logs
    journals.open_system_section()
    # Select all visible rows with logs
    journals.select_all_visible_rows_system()
    # Export CSV Logs
    journals.export_csv_logs()
    # Start waiting for the download
    journals.wait_and_confirm('test-results/logs.csv')
    # Logout
    journals.logout()
    # Check logs
    journals.validate_csv_log('test-results/logs.csv')

import csv
from datetime import datetime
import pytest
from playwright.sync_api import Page, expect


def test_download_logs(page: Page) -> None:
    page.goto("https://mon-aes/login-page")
    # Login as admin
    page.locator("input[name=\"username\"]").fill("admin")
    page.locator("input[name=\"password\"]").fill("Test123!")
    page.get_by_role("button", name="Войти").click()
    # Open logs
    page.get_by_role("button", name="Journals").click()
    page.get_by_role("row", name="Date Security node Device ID Facility Messages Category Severity Severity weight").get_by_role("button").click()
    page.locator(".control-group-control-group_element > .tooltip-tooltip_inline > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").first.click()
    # Start waiting for the download
    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.get_by_role("button", name="Export CSV logs").first.click()
    # Wait for the download to start
    download = download_info.value
    # Wait for the download process to complete
    print(download.path())
    # Save downloaded file somewhere
    download.save_as("test-results/logs.csv")


@pytest.fixture(scope='session')
def logs_file_path():
    return 'test-results/logs.csv'

def test_logs_file_contains_date(logs_file_path):
    with open(logs_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                try:
                    date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                    return
                except ValueError:
                    pass
    pytest.fail('No date in yyyy-mm-dd hh:mm:ss format found in the logs file.')
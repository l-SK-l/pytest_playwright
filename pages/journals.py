from playwright.sync_api import Page, expect
from datetime import datetime
# from tests.conftest import logs_file_path
import re
import csv
import pytest


class JournalsPage:

    URL = 'https://mon-aes/journals/syslog'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role(
            "button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

    def open_system_section(self) -> None:
        self.page.get_by_role("button", name="Journals").click(timeout=60000)
        self.page.get_by_role("button", name="System",
                              exact=True).click(timeout=60000)
        self.page.locator("#btnStatusRefresh").get_by_role("button")
        self.page.wait_for_timeout(5000)

    def open_ids_section(self) -> None:
        self.page.get_by_role("button", name="Journals").click(timeout=60000)
        self.page.get_by_role("button", name="IDS",
                              exact=True).click(timeout=60000)
        self.page.locator("#btnStatusRefresh").get_by_role("button")
        self.page.wait_for_timeout(5000)

    def open_management_section(self) -> None:
        self.page.get_by_role("button", name="Journals").click(timeout=60000)
        self.page.get_by_role("button", name="Management",
                              exact=True).click(timeout=60000)
        self.page.locator("#btnStatusRefresh").get_by_role("button")
        self.page.wait_for_timeout(5000)

    def select_all_visible_rows_system(self) -> None:
        self.page.get_by_role(
            "row", name="Date Security node Device ID Facility Messages Category Severity Severity weight").get_by_role("button").click()

    def select_all_visible_rows_ids(self) -> None:
        self.page.get_by_role(
            "row", name="Date Action Security node Source address Source country Destination address Destination country Destination domain Protocol Destination port Signature").get_by_role("button").click()

    def select_all_visible_rows_management(self) -> None:
        self.page.get_by_role(
            "row", name="Date Security node Device ID Subject Message Category Severity Severity weight").get_by_role("button").click()

    def open_filters(self) -> None:
        self.page.locator("#btnFilter").get_by_role(
            "button").click(timeout=60000)

    def select_filter_message(self, field) -> None:
        self.page.locator(f"input[name=\"{field}\"]").click()

    def fill_text(self, field, word: str) -> None:
        self.page.locator(f"input[name=\"{field}\"]").fill(word)
        self.page.wait_for_timeout(500)
        self.page.locator(f"input[name=\"{field}\"]").press("Enter")
        self.page.wait_for_timeout(1000)

    def clear_all(self) -> None:
        self.page.locator("div:nth-child(11) > .tooltip-tooltip_inline > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Clear all").get_by_role(
            "button", name="Clear all", exact=True).filter(has_text="Clear all").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

    def word_is_on_page(self, word: str) -> None:
        self.page.locator("#btnStatusRefresh").get_by_role("button")
        self.page.wait_for_timeout(1000)
        expect(self.page.locator(".content-block-content-block_root")
               ).to_have_text(re.compile(rf"\b{word}\b", re.IGNORECASE))

    def word_is_not_on_page(self, word: str) -> None:
        self.page.locator("#btnStatusRefresh").get_by_role("button")
        self.page.wait_for_timeout(1000)
        expect(self.page.get_by_text(re.compile(
            rf"\b{word}\b", re.IGNORECASE))).not_to_be_visible()

    def export_csv_logs(self) -> None:
        self.page.locator(".control-group-control-group_element > .tooltip-tooltip_inline > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").first.click()

    def wait_and_confirm(self, path: str) -> None:
        with self.page.expect_download() as download_info:
            # Perform the action that initiates download
            self.page.get_by_role(
                "button", name="Export CSV logs").first.click(timeout=300000)
        # Wait for the download to start
        download = download_info.value
        # Wait for the download process to complete
        print(download.path())
        # Save downloaded file
        download.save_as(path)

    def validate_csv_log(self, logs_file_path: str) -> None:
        with open(logs_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for value in row:
                    try:
                        date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                        return
                    except ValueError:
                        pass
        pytest.fail(
            'No date in yyyy-mm-dd hh:mm:ss format found in the logs file.')

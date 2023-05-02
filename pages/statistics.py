from playwright.sync_api import Page, expect
import re
import pytest


class StatisticsPage:

    URL = 'https://mon-aes/statistics/predefined_statistics'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def check_widget_top15_available(self) -> None:
        self.page.wait_for_timeout(3000)
        self.page.get_by_text("Top 15 faulty nodes")

    def check_empty_widget(self) -> None:
        self.page.get_by_text("Widget title")

    def add_new_dashboard(self) -> None:
        self.page.get_by_role("button", name="Добавить").click()
        self.page.get_by_placeholder("Widgets set name").fill("new_dashboard")
        self.page.get_by_role("button", name="Apply", exact=True).click()

    def duplicate_dashboard(self) -> None:
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("button", name="Duplicate").click()
        self.page.get_by_placeholder("Widgets set name").click()
        self.page.get_by_placeholder(
            "Widgets set name").fill("duplicate_dashboard")
        self.page.get_by_role("button", name="Apply", exact=True).click()
        self.page.get_by_role(
            "button", name="duplicate_dashboard", exact=True).click()

    def open_new_dashboard(self) -> None:
        self.page.get_by_role("button", name=(
            "new_dashboard"), exact=True).click()

    def open_duplicate_dashboard(self) -> None:
        self.page.get_by_role("button", name=(
            "duplicate_dashboard"), exact=True).click()

    def delete_new_dashboard(self) -> None:
        self.page.get_by_role("button", name="new_dashboard", exact=True).get_by_role(
            "button").nth(1).click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

    def delete_duplicate_dashboard(self) -> None:
        self.page.get_by_role("button", name="duplicate_dashboard",
            exact=True).get_by_role("button").nth(1).click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

    def word_is_not_on_page(self, word: str) -> None:
        expect(self.page.get_by_text(re.compile(
            rf"\b{word}\b", re.IGNORECASE))).not_to_be_visible()

    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role(
            "button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

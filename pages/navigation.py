from playwright.sync_api import Page, expect
import re
import pytest


class NavigationPage:

    URL = 'https://mon-aes/navigation/common/templates'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def search_node(self) -> None:
        self.page.get_by_placeholder("Searching for nodes...").click()
        self.page.get_by_placeholder("Searching for nodes...").fill("node-1")
        self.page.get_by_placeholder("Searching for nodes...").press("Enter")

    def open_node(self, node_name: str) -> None:
        self.page.get_by_text(re.compile(
            rf"\b{node_name}\b", re.IGNORECASE)).click()

    def check_cpu_and_memory_widgets(self) -> None:
        self.page.get_by_text("ram").click()
        self.page.get_by_text("buffers", exact=True).click()
        self.page.get_by_text("cache", exact=True).click()
        self.page.get_by_text("swap").click()
        self.page.get_by_text("Total").nth(1).click()
        self.page.get_by_text("CPU", exact=True).click()
        self.page.get_by_text("load per 1/5/15 minutes").click()
        self.page.get_by_text("idle per 1/5/15 minutes").click()
        self.page.get_by_text("temperature").click()
        self.page.get_by_text("sda per 1/5/15 minutes").click()

    def check_subsystems_widgets(self) -> None:
        self.page.get_by_text("Firewall").click()
        self.page.get_by_text("connections per 1/5/15 minutes").click()
        self.page.get_by_text("log", exact=True).click()
        self.page.get_by_text("used").nth(3).click()
        self.page.get_by_text("syslog").click()
        self.page.get_by_text("state").nth(2).click()

    def check_hard_disk_widgets(self) -> None:
        self.page.get_by_text("sda", exact=True).click()
        self.page.get_by_text("SMART", exact=True).click()

    def check_hard_disks_widgets(self) -> None:
        self.page.get_by_text("Boot").click()
        self.page.get_by_text("usage (free / used / Total)").click()
        self.page.get_by_text("Data").click()
        self.page.get_by_text("usage (free / used / Total)").nth(1).click()
        self.page.get_by_text("System", exact=True).click()
        self.page.get_by_text("usage (free / used / Total)").nth(2).click()
        self.page.get_by_text("Temporary").click()
        self.page.get_by_text("usage (free / used / Total)").nth(3).click()

    def check_net_interface_widget(self) -> None:
        self.page.get_by_role("heading", name="Network interfaces").click()
        self.page.get_by_text("ge-0-0").click()

    def word_is_on_page(self, word: str) -> None:
        expect(self.page.get_by_text(re.compile(
            rf"\b{word}\b", re.IGNORECASE))).to_be_visible()

    def word_is_not_on_page(self, word: str) -> None:
        expect(self.page.get_by_text(re.compile(
            rf"\b{word}\b", re.IGNORECASE))).not_to_be_visible()

    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role(
            "button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

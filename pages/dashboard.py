from playwright.sync_api import Page, expect
import re
import pytest

class DashboardPage:

    URL = 'https://mon-aes/dashboard/predefined_dashboard'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def chech_widget_access_server_available(self) -> None:
        self.page.get_by_text("Access server")

    def check_widget_access_server_has_0_connections(self) -> None:
        self.page.get_by_role("columnheader", name="Connected 0").get_by_text("0")

    def open_widget_access_server(self) -> None:
        self.page.get_by_role("button", name="User sessions").click()

    def check_widget_access_server_has_0_connections_inside(self) -> None:
        self.page.get_by_text("Total 0").nth(1).click()
        self.page.locator(".panel-panel_icon").click()

    def chech_widget_vpn_available(self) -> None:
        self.page.get_by_text("VPN")
        self.page.get_by_text("Tunnel 00")
        self.page.get_by_text("Download speed")
        self.page.get_by_text("Upload speed")

    def chech_widget_Network_ifaces_available(self) -> None:
        self.page.get_by_text("Network Ifaces")
        self.page.get_by_text("Security gateway")
        self.page.get_by_text("node-1")
        self.page.get_by_text("Interface")
        self.page.get_by_text("State")

    def chech_widget_Network_security_available(self) -> None:
        self.page.get_by_text("Network security log")
        self.page.get_by_text("Severity")

    def edit_dashboard(self) -> None:
        self.page.get_by_role("button", name="Edit").click()

    def add_new_dashboard(self) -> None:
        self.page.get_by_role("button", name="Добавить").click()
        self.page.get_by_placeholder("Widgets set name").click()
        self.page.get_by_placeholder("Widgets set name").fill("new_dashboard")
        self.page.get_by_role("button", name="Apply", exact=True).click()

    def open_custom_dashboard(self) -> None:
        self.page.get_by_role("button", name=("new_dashboard"), exact=True).click()

    def edit_default_widget(self) -> None:
        self.page.locator("button:nth-child(2)").click()
        self.page.get_by_role("textbox").fill("new_widget")
        self.page.locator("#widgetTypeChoices div").nth(4).click()
        self.page.locator("#react-select-8-option-2").click() # unstable data
        self.page.locator("#infotTypeChoices div").nth(4).click()
        self.page.get_by_text("State", exact=True).click()
        self.page.locator("#infoSourceChoices div").nth(4).click()
        self.page.get_by_text("Monitoring", exact=True).click()
        self.page.locator("#btnSave").click()
        self.page.get_by_text("domain-1")

    def save_dashboard_page(self) -> None:
        self.page.get_by_role("button", name="Save").click()

    def del_network_security_dashboard(self) -> None:
        self.page.locator("div").filter(has_text=re.compile(r"^Network security log$")).get_by_role("button").first.click()

    def word_is_not_on_page(self, word: str) -> None:
        expect(self.page.get_by_text(re.compile(rf"\b{word}\b", re.IGNORECASE))).not_to_be_visible()
    
    def open_about(self) -> None:
        self.page.get_by_role("button", name="About").click()

    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role(
            "button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

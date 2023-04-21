from playwright.sync_api import Page, expect
puth_screenshots = "test-results/screenshots/check_that_monitoring_work/"

class DashboardPage:

    URL = 'https://mon-aes/dashboard/predefined_dashboard'
    
    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def open_about(self) -> None:
        self.page.get_by_role("button", name="About").click()
    
    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role("button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()

    def screenshot(self) -> None:
        self.page.screenshot(path=f"{puth_screenshots}version_logo.png")
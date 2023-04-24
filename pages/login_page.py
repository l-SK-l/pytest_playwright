import re
from playwright.sync_api import Page, expect


class LoginPage:

    URL = 'https://mon-aes/login-page'
    
    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    def check_title(self) -> None:
        expect(self.page).to_have_title("Мониторинг - Авторизация")

    def login_admin(self) -> None:
        self.page.goto(self.URL)
        self.page.locator("input[name=\"username\"]").click()
        self.page.locator("input[name=\"username\"]").fill("admin")
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill("Test123!")
        self.page.get_by_role("button", name="Войти").click()
        self.page.wait_for_timeout(1000)

    def login_obama(self) -> None:
        self.page.goto(self.URL)
        self.page.locator("input[name=\"username\"]").click()
        self.page.locator("input[name=\"username\"]").fill("obama")
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill("Test123!")
        self.page.get_by_role("button", name="Войти").click()
        expect(self.page.locator('//*[@id="root"]/div/div/div[2]/div/div[2]/form/div/div[5]')).to_have_text("Неверное имя пользователя или пароль")

    def logout(self) -> None:
        self.page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
        self.page.get_by_role("button", name="Exit").get_by_role(
            "button", name="Exit", exact=True).filter(has_text="Exit").click()
        self.page.get_by_role("button", name="Proceed", exact=True).click()
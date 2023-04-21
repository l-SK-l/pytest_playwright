from playwright.sync_api import Page, expect
puth_screenshots = "test-results/screenshots/check_login_page/"

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

    def screenshot(self) -> None:
        self.page.screenshot(path=f"{puth_screenshots}1_login_page.png")
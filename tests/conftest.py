import pytest
from playwright.sync_api import Playwright, Page, expect
# page.pause()

# @pytest.fixture(scope="function", autouse=True)
# def before_each_after_each(page: Page):
#     print("beforeEach")
#     # Go to the starting url before each test.
#     page.goto("https://playwright.dev/")
#     yield
#     print("afterEach")

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "ignore_https_errors": True
#     }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1366,
            "height": 768,
        }
    }

class JornalsPage:
    def __init__(self, page):
        self.page = page
        # self.search_term_input = page.locator('[aria-label="Enter your search term"]')

    def login(self):
        self.page.goto("https://mon-aes/login-page")
    # Login as admin
        self.page.get_by_role("button", name="Войти").click()
        self.page.locator("input[name=\"username\"]").click()
        self.page.locator("input[name=\"username\"]").fill("admin")
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill("Test123!")
        self.page.get_by_role("button", name="Войти").click()
    # Open the management logs
        self.page.get_by_text("MANAGEMENT:").click()
        self.page.get_by_role("button", name="Journals").click()
    # def search(self, text):
    #     self.search_term_input.fill(text)
    #     self.search_term_input.press("Enter")

# @pytest.fixture(scope="function")
# def authenticated_page(playwright: Playwright) -> Page:
#     with playwright.chromium.launch() as browser:
#         with browser.new_context() as context:
#             page = context.new_page()
#             page.goto("https://mon-aes/login-page")
#             # Read login and password from .auth file
#             with open("tests/.auth") as f:
#                 username, password = f.read().strip().split("\n")
#             page.fill('input[name="username"]', username)
#             page.fill('input[name="password"]', password)
#             page.get_by_role("button", name="Войти").click()
#             yield page

# def test_main_navigation(page: Page):
#     # Assertions use the expect API.
#     expect(page).to_have_url("https://playwright.dev/")
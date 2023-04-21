import pytest
from playwright.sync_api import Playwright, Page, expect
# page.pause()
corrent_version = "4.1.5.2475"
corrent_year = "2022"

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
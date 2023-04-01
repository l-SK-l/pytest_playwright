import pytest
from playwright.sync_api import Page, expect


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

def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")
import pytest
from playwright.sync_api import Playwright, Page, expect
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from pages.journals import JournalsPage
# page.pause()

# Variables
current_version = "4.1.5.2475"
current_year = "2022"
screen_width_resolution = 1366
screen_height_resolution = 768


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": screen_width_resolution,
            "height": screen_height_resolution,
        }
    }


def pytest_addoption(parser):
    parser.addoption("--screen_width", action="store",
                     default=None, help="Screen width resolution")
    parser.addoption("--screen_height", action="store",
                     default=None, help="Screen height resolution")


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def journals(page: Page) -> JournalsPage:
    return JournalsPage(page)

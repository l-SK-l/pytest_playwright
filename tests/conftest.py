import pytest
from playwright.sync_api import Playwright, Page, expect
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from pages.journals import JournalsPage
from pages.statistics import StatisticsPage
from pages.settings import SettingsPage
from pages.navigation import NavigationPage
# page.pause()

# Variables
screen_width_resolution = 1366
screen_height_resolution = 768


# Additional parameters
def pytest_addoption(parser):
    parser.addoption(
        "--fw_year",
        action="store",
        default="2023",
        help="Current year in web monitoring"
    )
    parser.addoption(
        "--fw_version",
        action="store",
        default="4.1.7.1325",
        help="Current version firewall"
    )


@pytest.fixture
def current_year(request):
    return request.config.getoption("--fw_year")


@pytest.fixture
def current_version(request):
    return request.config.getoption("--fw_version")


# Screen resolution, transmitted to all tests
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


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def journals_page(page: Page) -> JournalsPage:
    return JournalsPage(page)


@pytest.fixture
def statistics_page(page: Page) -> StatisticsPage:
    return StatisticsPage(page)


@pytest.fixture
def settings_page(page: Page) -> SettingsPage:
    return SettingsPage(page)


@pytest.fixture
def navigation_page(page: Page) -> NavigationPage:
    return NavigationPage(page)

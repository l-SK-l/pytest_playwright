import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"viewport": {"width":1366,"height":768}}


def test_chack_that_monitoring_work(page: Page) -> None:
    page.goto("https://mon-aes/login-page")
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Неверное имя пользователя или пароль").click()
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("admin")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("Cont-4.X")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="About").click()
    page.get_by_role("button", name="SC logo Dashboard and audit \"Continent 4\" Version 4.1.5.2475 Our contacts support@securitycode.ru Site www.securitycode.net © 1995-2022 Security Code").get_by_role("button", name="SC logo Dashboard and audit \"Continent 4\" Version 4.1.5.2475 Our contacts support@securitycode.ru Site www.securitycode.net © 1995-2022 Security Code", exact=True).filter(has_text="Dashboard and audit \"Continent 4\"Version4.1.5.2475Our contactssupport@securityco").locator("button").click()
    page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
    page.get_by_role("button", name="Exit").get_by_role("button", name="Exit", exact=True).filter(has_text="Exit").click()
    page.get_by_role("button", name="Proceed", exact=True).click()


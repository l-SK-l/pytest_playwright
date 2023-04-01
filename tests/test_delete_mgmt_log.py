import pytest
import re
from playwright.sync_api import Page, expect
# breakpoint()

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


def test_delete_mgmt_log(page: Page) -> None:
    page.goto("https://mon-aes/login-page")
    # Login with wrong username
    page.fill('input[name="username"]', 'obama')
    page.get_by_role("button", name="Войти").click()
    # Check for error message
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div[2]/form/div/div[5]')).to_have_text("Неверное имя пользователя или пароль")
    # Login as admin
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'Cont-4.X')
    page.get_by_role("button", name="Войти").click()
    # Open the management logs
    page.get_by_text("MANAGEMENT:").click()
    page.get_by_role("button", name="Journals").click()
    page.get_by_role("button", name="Management", exact=True).click()
    # Looking for the right log
    page.locator("#btnFilter").get_by_role("button").click()
    page.wait_for_timeout(500)
    page.locator("input[name=\"action\"]").click()
    page.wait_for_timeout(500)
    page.locator("input[name=\"action\"]").fill("obama")
    page.locator("input[name=\"action\"]").press("Enter")
    page.screenshot(path="screenshots/delete_mgmt_log/1_before_delete.png")
    # Deleting the log
    page.get_by_role("row", name="obama").get_by_role("button").click()
    page.locator("div:nth-child(11) > .tooltip-tooltip_inline > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
    page.get_by_role("button", name="Delete selected").get_by_role(
        "button", name="Delete selected", exact=True).filter(has_text="Delete selected").click()
    page.get_by_role("button", name="Proceed", exact=True).click()
    # Check that the log has been deleted
    expect(page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]')).not_to_have_text("obama")
    page.screenshot(path="screenshots/delete_mgmt_log/2_after_delete.png")
    # Log out of the website.
    page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
    page.get_by_role("button", name="Exit").get_by_role(
        "button", name="Exit", exact=True).filter(has_text="Exit").click()
    page.get_by_role("button", name="Proceed", exact=True).click()

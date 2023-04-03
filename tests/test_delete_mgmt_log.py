import pytest
import re
from conftest import JornalsPage
from playwright.sync_api import Page, expect
# breakpoint()
puth_screenshots = "test-results/screenshots/delete_mgmt_log/"


def test_delete_mgmt_log(page: Page) -> None:
    page.goto("https://mon-aes/login-page")
    # Login with wrong username
    page.fill('input[name="username"]', 'obama')
    page.get_by_role("button", name="Войти").click()
    # Check for error message
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div[2]/form/div/div[5]')).to_have_text("Неверное имя пользователя или пароль")
    # Login as admin
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'Test123!')
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
    page.screenshot(path=f"{puth_screenshots}1_before_delete.png")
    # Deleting the log
    page.get_by_role("row", name="obama").get_by_role("button").click()
    page.locator("div:nth-child(11) > .tooltip-tooltip_inline > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
    page.get_by_role("button", name="Delete selected").get_by_role(
        "button", name="Delete selected", exact=True).filter(has_text="Delete selected").click()
    page.get_by_role("button", name="Proceed", exact=True).click()
    # Check that the log has been deleted
    # page.pause()
    expect(page.locator(".content-block-content-block_root")).not_to_have_text("obama")
    page.screenshot(path=f"{puth_screenshots}2_after_delete.png")
    # Log out of the website.
    page.locator("div:nth-child(8) > .toolbar-dropdown_wrapper > .base-dropdown-dropdown_dropdown > .base-dropdown-dropdown_dropdownToggle > .toolbar-dropdown_root > .toolbar-button_wrapper > .toolbar-button_root").click()
    page.get_by_role("button", name="Exit").get_by_role(
        "button", name="Exit", exact=True).filter(has_text="Exit").click()
    page.get_by_role("button", name="Proceed", exact=True).click()

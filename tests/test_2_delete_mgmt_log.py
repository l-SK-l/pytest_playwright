import pytest
from pages.login_page import LoginPage
from pages.journals import JournalsPage
from playwright.sync_api import Page


def test_delete_mgmt_log(
        page: Page,
        login_page: LoginPage,
        journals_page: JournalsPage) -> None:
    """
    Checking the ability to search for and delete logs
    """
    # Аuthorization with an invalid password, under the user "Obama"
    login_page.login_obama()
    # Login as Admin
    login_page.login_admin()
    # Open Management journals
    journals_page.load()
    journals_page.open_management_section()
    # Find the word "Obama" in messages
    journals_page.open_filters()
    journals_page.select_filter_message('action')
    journals_page.fill_text('action', 'obama')
    # Deleting the found logs
    journals_page.word_is_on_page('obama')
    journals_page.select_all_visible_rows_management()
    journals_page.clear_all()
    # Check that the word "Obama" is not on the screen
    journals_page.word_is_not_on_page('obama')
    # Logout
    journals_page.logout()

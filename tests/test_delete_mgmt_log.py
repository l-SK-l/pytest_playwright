from pages.login_page import LoginPage
from pages.journals import JournalsPage
from playwright.sync_api import Page


def test_delete_mgmt_log(
    page: Page,
    login_page: LoginPage,
    journals: JournalsPage) -> None:
    # Аuthorization with an invalid password, under the user "Obama"
    login_page.login_obama()
    # Login as Admin
    login_page.login_admin()
    page.wait_for_timeout(1000)
    # Open Management journals
    journals.load()
    journals.open_management_section()
    # Find the word "Obama" in messages
    journals.open_filters()
    journals.select_filter_message('action')
    journals.fill_text('action', 'obama')
    # Deleting the found logs
    journals.word_is_on_page('obama')
    journals.select_all_visible_rows()
    journals.clear_all()
    # Check that the word "Obama" is not on the screen
    journals.word_is_not_on_page('obama')
    # Logout
    journals.logout()
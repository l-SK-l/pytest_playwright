from playwright.sync_api import Page, expect
import re
import pytest

class SettingsPage:

    URL = 'https://mon-aes/settings/mailserver'

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)

    
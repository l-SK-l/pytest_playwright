import pytest
from pages.login_page import LoginPage
from pages.navigation import NavigationPage
from playwright.sync_api import Page


def test_check_structure_node_information(
        page: Page,
        login_page: LoginPage,
        navigation_page: NavigationPage) -> None:
    """
    Checking the navigation page with nodes and data availability from a node
    """
    # Login
    login_page.login_admin()
    # Open navigation page
    navigation_page.load()
    # Node 1 available
    navigation_page.word_is_on_page('node-1')
    # Node 1 is available in the search
    navigation_page.search_node()
    navigation_page.word_is_on_page('node-1')
    # Open Node
    navigation_page.open_node('node-1')
    navigation_page.word_is_on_page('Node: node-1')
    # Check widgets
    navigation_page.check_cpu_and_memory_widgets()
    navigation_page.check_subsystems_widgets()
    navigation_page.check_hard_disk_widgets()
    navigation_page.check_hard_disks_widgets()
    navigation_page.check_net_interface_widget()
    # Logout
    navigation_page.logout()
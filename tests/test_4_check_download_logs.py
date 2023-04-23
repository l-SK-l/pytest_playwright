from pages.login_page import LoginPage
from pages.journals import JournalsPage
from playwright.sync_api import Page


def test_check_download_logs(
    page: Page,
    login_page: LoginPage,
    journals: JournalsPage) -> None:
    # Login as Admin
    login_page.login_admin()
    # Open System journals
    journals.load()
    # Open logs
    journals.open_system_section()
    # Select all visible rows with logs
    journals.select_all_visible_rows_system()
    # Export CSV Logs
    journals.export_csv_logs()
    # Start waiting for the download
    journals.wait_and_confirm('test-results/logs.csv')
    # Check logs
    journals.validate_csv_log('test-results/logs.csv')


# @pytest.fixture(scope='session')
# def logs_file_path():
#     return 'test-results/logs.csv'

# def test_logs_file_contains_date(logs_file_path):
#     with open(logs_file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             for value in row:
#                 try:
#                     date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
#                     return
#                 except ValueError:
#                     pass
#     pytest.fail('No date in yyyy-mm-dd hh:mm:ss format found in the logs file.')
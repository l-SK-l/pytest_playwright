from playwright.sync_api import Page, expect
puth_screenshots = "test-results/screenshots/check_login_page/"

def test_check_login_page(page: Page) -> None:
    page.goto("https://mon-aes/")
    # expect(page.locator('//*[@id="root"]/div/div/div[2]/button/div')).to_have_text("Войти")
    # Wait for a loading event
    page.wait_for_load_state("networkidle")
    expect(page).to_have_title("Мониторинг - Авторизация")
    page.screenshot(path=f"{puth_screenshots}1_login_page.png")

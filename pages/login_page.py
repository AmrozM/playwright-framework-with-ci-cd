# pages/login_page.py

from playwright.sync_api import Page, expect
from config.config import BASE_URL, DEFAULT_TIMEOUT
from utils.logger import get_logger


class LoginPage:
    def __init__(self,page: Page):
        self.page = page
        self.log = get_logger("LoginPage")
        self.username_input = self.page.locator('input[name="username"]')
        self.password_input = self.page.locator('input[name="password"]')
        # button locator specific to the OrangeHRM demo login
        self.sign_in_button = self.page.locator('button[type="submit"]')
        self.dashboard_button = self.page.locator('a:has-text("Dashboard")')
        self.error_message = self.page.locator('.oxd-alert-content-text')

    def open(self, url: str):
        # iF you use context base_url, you can call self.page.goto("/") too.
        self.log.info("Opening login page")
        self.page.goto(url, wait_until="domcontentloaded")
        expect(self.username_input).to_be_visible(timeout=DEFAULT_TIMEOUT)
        self.log.info("Login page loaded successfully")

    def login(self, username: str, password: str):
        self.log.info("Entering username and password")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.log.info("Clicking login button")
        self.sign_in_button.click()
        # tests should wait for their expected destination URL
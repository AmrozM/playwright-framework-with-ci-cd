from playwright.sync_api import Page, expect
from config.constants import DEFAULT_TIMEOUT
from utils.logger import get_logger

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.log = get_logger("MISLoginPage")
        self.school_id_input = self.page.locator('input#SchoolIDTextBox')
        self.username_input = self.page.locator('input#UsernameTextBox')
        self.password_input = self.page.locator('input#PasswordTextBox')
        self.sign_in_button = self.page.locator('button#LoginButton')

    def open(self, url: str):
        self.log.info("Opening MIS Login page")
        self.page.goto(url, wait_until="domcontentloaded")
        expect(self.username_input).to_be_visible(timeout=DEFAULT_TIMEOUT)
        self.log.info("MIS Login page loaded successfully")

    def login(self, school_id: str, username: str, password: str):
        self.school_id_input.fill(school_id)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.log.info(f"Logging in with School ID: {school_id}")
        self.sign_in_button.click()
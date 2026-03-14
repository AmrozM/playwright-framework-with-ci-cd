#/pages.Vision_login.py
from playwright.sync_api import Page, expect
from config.constants import DEFAULT_TIMEOUT
from utils.logger import get_logger

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.log = get_logger("VisionLoginPage")
        self.customer_code_input = self.page.locator('input#CustomerCode')
        self.username_input = self.page.locator('input#Username')
        self.password_input = self.page.locator('input#Password')
        self.sign_in_button = self.page.locator('input#btnSignin')

    def open(self, url: str):
        self.log.info("Opening MAT Vision Login page")
        self.page.goto(url, wait_until="domcontentloaded")
        expect(self.username_input).to_be_visible(timeout=DEFAULT_TIMEOUT)
        self.log.info("MAT VIsion Login page loaded successfully")

    def login(self, customer_code: str, username: str, password: str):
        self.customer_code_input.fill(customer_code)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.log.info(f"Logging in with Customer code: {customer_code}")
        self.sign_in_button.click()

    
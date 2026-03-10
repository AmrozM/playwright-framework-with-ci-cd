import re
import json
from playwright.sync_api import expect
from pages.login_page import LoginPage

with open("test_data/orangehrm_login_data.json") as f:
    test_data = json.load(f)

valid_username = test_data["valid_user"]["username"]
valid_password = test_data["valid_user"]["password"]

def test_orangehrm_login(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(valid_username, valid_password)
    expect(login.dashboard_button).to_be_visible(timeout=30000)
    assert re.search(r"/dashboard", page.url, re.IGNORECASE), "Dashboard page did not load check url"
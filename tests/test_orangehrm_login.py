import re
import json
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from config.config import BASE_URL

with open("test_data/orangehrm_login_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("username, password, expected", [
    (test_data["valid_user"]["username"], test_data["valid_user"]["password"], "valid"),
    (test_data["invalid_user"]["username"], test_data["invalid_user"]["password"], "invalid")
])

def test_orangehrm_login(page, username, password, expected):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(username, password)
    if expected == "valid":
        expect(login.dashboard_button).to_be_visible(timeout=30000)
        assert re.search(r"/dashboard", page.url, re.IGNORECASE), "Dashboard page did not load check url"
    else:
        expect(login.error_message).to_be_visible()
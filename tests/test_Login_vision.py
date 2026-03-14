#test_login_vision.py
from playwright.sync_api import expect
from pages.Vision_login import LoginPage
from pages.vision_navigate_to_studentlist import vision_navigation_class
from config.config import VISION_URL, CUSTOMER_CODE, VISION_USERNAME, VISION_PASSWORD
from utils.logger import get_logger

def test_login_vision(page):
    log = get_logger("TestLogin")
    log.info("Starting Mat Vision login test")
    login = LoginPage(page)
    login.open(VISION_URL)
    login.login(CUSTOMER_CODE, VISION_USERNAME, VISION_PASSWORD)
    navigator = vision_navigation_class(page)
    navigator.goto_vision_studentlist()
    expect(navigator.studentlist_pagename).to_be_visible()
    page.wait_for_timeout(1000)
    assert f"{VISION_URL}Students/StudentList" in page.url, "Url seems to be different" # use following if page opens in new tab assert "url" in new_tab.url
    log.info("MAT Vision Login test completed successfully")
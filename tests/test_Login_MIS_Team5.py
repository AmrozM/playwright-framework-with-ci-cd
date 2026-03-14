#test_login_MIS_Team5.py
from playwright.sync_api import expect
from pages.MIS_login_Team5 import LoginPage
from pages.navigateToStudents import goToStudents
from config.config import MIS_URL, SCHOOL_ID, MIS_USERNAME, MIS_PASSWORD
from utils.logger import get_logger

def test_Login_MIS_Team5(page):
    log = get_logger("TestLogin")
    log.info("Starting MIS login test")
    login = LoginPage(page)
    login.open(MIS_URL)
    login.login(SCHOOL_ID, MIS_USERNAME, MIS_PASSWORD)
    navigator = goToStudents(page)
    expect(navigator.student_module).to_be_attached()
    navigator.go_to_student_module()
    navigator.select_student()
    navigator.click_view_button()
    page.wait_for_timeout(10000)
    new_tab = navigator.click_view_button() #use this when checking on new_tab
    assert f"{MIS_URL}Nucleus/UI/Areas/People/StudentList.aspx" in page.url, "Url seems to be different" # use following if page opens in new tab assert "url" in new_tab.url
    log.info("MIS Login test completed successfully")
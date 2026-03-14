#pages/vision_navigate_to_studentlist
from playwright.sync_api import Page, expect
class vision_navigation_class:
    def __init__(self, page: Page):
        self.page = page
        self.vision_list = self.page.locator('li:has(i.fa-list-alt)')
        self.vision_student_list = self.page.locator('#verticalmenu-Student:has-text("Students")')
        self.studentlist_pagename = self.page.locator('#StudentListContent')
        self.studentlist_aggrid_checkbox = self.page.locator('.ag-row').nth(1)

    def goto_vision_studentlist(self):
        expect(self.vision_list).to_be_attached()
        self.vision_list.click()
        expect(self.vision_student_list).to_be_visible(timeout=10000)
        self.vision_student_list.click()
        expect(self.studentlist_pagename).to_be_visible()
        expect(self.page.locator('.ag-row').nth(1)).to_be_attached(timeout=15000)
        self.page.locator('.ag-row').nth(0).dispatch_event('click')
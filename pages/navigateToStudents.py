from playwright.sync_api import Page, expect
class goToStudents:
    def __init__(self, page: Page):
        self.page = page
        self.student_module = self.page.locator("a:has(span.grid-display:has-text('Students'))")
        self.select_student_row = self.page.locator("table.k-selectable tbody tr").nth(1)
        self.view_btn = self.page.get_by_role("button", name="View")

    def go_to_student_module(self):
        # wait for the link to appear
        expect(self.student_module).to_be_visible()
        self.student_module.click()
        
    def select_student(self):
        self.select_student_row.click()

    def click_view_button(self):
            with self.page.expect_popup() as new_page_info:
                self.view_btn.click()
            return new_page_info.value
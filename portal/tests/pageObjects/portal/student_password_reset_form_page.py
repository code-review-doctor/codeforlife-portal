from __future__ import absolute_import

from .base_page import BasePage
from .home_page import HomePage


class StudentPasswordResetFormPage(BasePage):
    def __init__(self, browser):
        super(StudentPasswordResetFormPage, self).__init__(browser)

        assert self.on_correct_page("reset_password_student_page")

    def cancel(self):
        self.browser.find_element_by_id("cancel_button").click()

        return HomePage(self.browser)

    def reset_username_submit(self, username):
        self.browser.find_element_by_id("id_username").send_keys(username)

        self.browser.find_element_by_id("reset_button").click()

        return self

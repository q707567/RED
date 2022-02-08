import time
from Project.Pay.Login.login_page import Login
from Project.common_els import Common
from playwright.sync_api import sync_playwright
from Common.common import path_file


class LoginOperation(Login, Common):
    def login_pw_check(self, tel, pw):
        self.input_tel(tel)
        self.input_pw(pw)
        self.submit()

    def login_pw_submit(self, tel, pw):
        self.input_tel(tel)
        self.input_pw(pw)
        self.submit()
        self.yzm()

    def login_yzm_check(self, tel, yzm):
        self.go_yzm()
        self.input_tel(tel)
        self.input_yzm(yzm)
        self.submit()

    def login_yzm_submit(self, tel, yzm):
        self.go_yzm()
        self.input_tel(tel)
        self.input_yzm(yzm)
        self.yzm_button()
        self.yzm()
        self.submit()

#
# if __name__ == '__main__':
#     path_images = path_file(pro='RED') + '/Images'
#     with sync_playwright() as browser_window:
#         obj = LoginOperation()
#         obj.sync_run(browser_window, 'chrome')
#         obj.get_url('https://www.cargonpay.com/back/#/login')
#         obj.login_pw_submit('13910000000', 'Aa123456')
#         obj.page.screenshot(path=path_images + '/111.png')
#         print('33333333333333')
#         obj.browser.close()



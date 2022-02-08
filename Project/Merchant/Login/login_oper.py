import time
from Project.Merchant.Login.login_page import Login
from Project.common_els import Common


class LoginOperation(Login, Common):
    def login_pw_check(self, tel, pw):
        self.input_tel(tel)
        self.input_pw(pw)
        self.submit()

    def login_pw_submit(self, tel, pw):
        self.input_tel(tel)
        self.input_pw(pw)
        self.submit()
        time.sleep(1)
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
        time.sleep(1)
        self.yzm()
        self.submit()
import time
from Project.Merchant.Regist.regist_page import Register
from Project.common_els import Common


class RegisterOperation(Register, Common):
    def register_submit(self, tel, yzm, pw):
        self.input_tel(tel)
        self.yzm_button()
        time.sleep(1)
        self.yzm()
        self.input_yzm(yzm)
        self.input_pw(pw)
        time.sleep(1)
        self.submit()
        time.sleep(1)

    def register_check(self, tel, yzm, pw):
        self.input_tel(tel)
        self.input_yzm(yzm)
        self.input_pw(pw)
        time.sleep(1)
        self.yzm_button()
        time.sleep(1)




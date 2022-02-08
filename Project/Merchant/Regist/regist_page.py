# coding=utf-8
from selenium.webdriver.common.keys import Keys
from Common.webkeys import WebKeys


class Register(WebKeys):
    def register_url(self):
        self.driver.get('https://www.cargonpay.com/merchant/#/register')

    def input_tel(self, value):
        self.element_location('xpath', '//input[@placeholder="请输入手机号码"]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[@placeholder="请输入手机号码"]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[@placeholder="请输入手机号码"]').send_keys(value)

    def input_yzm(self, value):
        self.element_location('xpath', '//input[@placeholder="请输入验证码"]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[@placeholder="请输入验证码"]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[@placeholder="请输入验证码"]').send_keys(value)

    def input_pw(self, value):
        self.element_location('xpath', '//input[@placeholder="请输入8-20位含数字、大小写字母组合密码"]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[@placeholder="请输入8-20位含数字、大小写字母组合密码"]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[@placeholder="请输入8-20位含数字、大小写字母组合密码"]').send_keys(value)

    def submit(self):
        button = self.element_location('xpath', '//button[@class="ivu-btn ivu-btn-primary ivu-btn-long"]')
        flag = button.get_property('disabled')
        if flag is False:
            button.click()
        else:
            print("不可点击")

    def yzm_button(self):
        self.element_location('xpath', '//span[text()="获取验证码"]').click()






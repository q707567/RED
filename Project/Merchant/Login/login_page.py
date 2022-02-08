# coding=utf-8
from selenium.webdriver.common.keys import Keys
from Common.webkeys import WebKeys


class Login(WebKeys):

    def input_tel(self, value):
        self.element_location('xpath', '//input[@placeholder="请输入手机号码"]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[@placeholder="请输入手机号码"]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[@placeholder="请输入手机号码"]').send_keys(value)

    def input_pw(self, value):
        self.element_location('xpath', '//input[@placeholder="请输入密码"]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[@placeholder="请输入密码"]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[@placeholder="请输入密码"]').send_keys(value)

    def input_yzm(self, value):
        self.element_location('xpath', '//input[@placeholder="请输入验证码"]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[@placeholder="请输入验证码"]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[@placeholder="请输入验证码"]').send_keys(value)

    def yzm_button(self):
        self.element_location('xpath', '//span[text()="获取验证码"]').click()

    def submit(self):
        self.element_location('xpath', '//button[@class="ivu-btn ivu-btn-primary ivu-btn-long"]').click()

    def go_yzm(self):
        self.element_location('xpath', '//a[text()="验证登录"]').click()

    def go_pw(self):
        self.element_location('xpath', '//a[text()="密码登录"]').click()

# coding=utf-8
from Common.open_browser import RunBrowser


class Login(RunBrowser):

    def get_url(self, url):
        self.page.goto(url)

    def input_tel(self, value):
        self.page.fill('//input[@placeholder="请输入手机号码"]', value)

    def input_pw(self, value):
        self.page.fill('//input[@placeholder="请输入密码"]', value)

    def input_yzm(self, value):
        self.page.fill('//input[@placeholder="请输入验证码"]', value)

    def yzm_button(self):
        self.page.click('//span[text()="获取验证码"]')

    def submit(self):
        self.page.click('//button[@class="ivu-btn ivu-btn-primary ivu-btn-long"]')

    def go_yzm(self):
        self.page.click('//a[text()="验证登录"]')

    def go_pw(self):
        self.page.click('//a[text()="密码登录"]')

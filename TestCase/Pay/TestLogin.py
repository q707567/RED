import os
import sys
import time
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page,Browser
import pytest
from Common.common import read_excel_file, xstr, list_tuple, path_file, get_times
import allure
from Project.Pay.Login.login_oper import LoginOperation
sys.path.append(os.getcwd())
file = read_excel_file('/TestData/case.xlsx', 'pay_login')
file = list_tuple(file)


@allure.suite('登录测试')
@allure.feature('登录测试用例')
class TestLoginCase(object):

    def setup_class(self):
        path = path_file()
        get_time = get_times()
        self.path_images = path + '/Images/login_images' + get_time
        os.mkdir(self.path_images)
        self.operation = LoginOperation()

    @allure.story('{title}')
    def login_pw_null(self, **kwargs):
        self.operation.login_pw_check(kwargs.get('tel'), kwargs.get('pw'))
        time.sleep(1)
        self.screenshot()

    @allure.story('{title}')
    def login_pw_success(self, **kwargs):
        self.operation.login_pw_submit(kwargs.get('tel'), kwargs.get('pw'))
        time.sleep(1)
        self.screenshot()

    def login_yzm_null(self, **kwargs):
        self.operation.login_yzm_check(kwargs.get('tel'), kwargs.get('yzm'))
        time.sleep(1)
        self.screenshot()

    def login_yzm_success(self, **kwargs):
        self.operation.login_yzm_submit(kwargs.get('tel'), kwargs.get('yzm'))
        time.sleep(1)
        self.screenshot()

    def screenshot(self):
        path_image = self.path_images + '/image' + get_times() + '.png'
        self.operation.page.screenshot(path=path_image)
        with open(path_image, mode='rb') as f:
            picture = f.read()
            allure.attach(picture, '截图', allure.attachment_type.PNG)

    @allure.title('{title}')
    @pytest.mark.parametrize('data,title', file)
    def test_login(self, data, title):
        obj = TestLoginCase()
        func = getattr(obj, data.get('method'))
        data_dict = data.get('data')
        for key in data_dict:
            data_dict[key] = xstr(data_dict[key])
        with sync_playwright() as browser_window:
            self.operation.sync_run(browser_window, 'chrome')
            self.operation.get_url('https://www.cargonpay.com/back/#/login')
            func(**data_dict)


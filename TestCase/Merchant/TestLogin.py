import os
import sys
import time

import pytest
from Common.common import read_excel_file, xstr, list_tuple, path_file, get_times
import allure
from Project.Merchant.Login.login_oper import LoginOperation
sys.path.append(os.getcwd())
file = read_excel_file('/TestData/case.xlsx', 'merchant_login')
file = list_tuple(file)


@allure.suite('登录测试')
@allure.feature('登录测试用例')
class TestLoginCase(object):

    def setup_class(self):
        self.operation = LoginOperation()
        self.operation.open_browser('windows', '91')
        self.operation.get_url()
        path = path_file()
        get_time = get_times()
        self.path_images = path + '/Images/login_images' + get_time
        os.mkdir(self.path_images)

    def teardown_class(self):
        self.operation.driver.quit()

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
        self.operation.driver.save_screenshot(path_image)
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
        func(**data_dict)

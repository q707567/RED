import os
import sys
import pytest
from Common.common import read_excel_file, xstr, list_tuple, path_file, get_times
from Common.mysql import Mysql
import allure
from Project.Merchant.Regist.regist_oper import RegisterOperation
sys.path.append(os.getcwd())
file = read_excel_file('/TestData/case.xlsx', 'merchant_regist')
file = list_tuple(file)


@allure.suite('注册测试')
@allure.feature('注册测试用例')
class TestRegisterCase(object):

    def setup_class(self):
        conn_mysql = Mysql('172.16.10.72', 3306, 'root', '123456', 'rongetong_sso')
        sel_sql = conn_mysql.select_sql('sso_login', 'pin', mobile='15910000000', is_deleted='0')
        if len(sel_sql) > 0:
            conn_mysql.update_sql('sso_login', 'is_deleted', '1', mobile='15910000000')
            conn_mysql.update_sql('sso_user_detail', 'is_deleted', '1', mobile='15910000000')
            conn_mysql.update_sql('sso_user_info', 'is_deleted', '1', pin=sel_sql[0][0])
        else:
            print('没有数据')
        conn_mysql.close_database()
        self.operation = RegisterOperation()
        self.operation.open_browser('windows', '91')
        self.operation.register_url()
        path = path_file()
        get_time = get_times()
        self.path_images = path + '/Images/register_images' + get_time
        os.mkdir(self.path_images)

    def teardown_class(self):
        self.operation.driver.quit()

    @allure.story('{title}')
    def register_null(self, **kwargs):
        self.operation.register_check(kwargs.get('tel'), kwargs.get('yzm'), kwargs.get('pw'))
        self.screenshot()

    def register_success(self, **kwargs):
        self.operation.register_submit(kwargs.get('tel'), kwargs.get('yzm'), kwargs.get('pw'))
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
        obj = TestRegisterCase()
        func = getattr(obj, data.get('method'))
        data_dict = data.get('data')
        for key in data_dict:
            data_dict[key] = xstr(data_dict[key])
        func(**data_dict)

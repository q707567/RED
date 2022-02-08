# coding=utf-8
import pytest
import time
from Common.common import path_file
import os


get_time = time.localtime()
get_time = time.strftime("%Y%m%d%H%M%S", get_time)
path = path_file()
path_json = path + '/Reports/Json' + get_time
path_html = path + '/Reports/Html' + get_time
file_path = '/TestCase/Pay/TestLogin.py'
pytest.main(['-s', path + file_path, '--alluredir', path_json])
allure = 'allure ' + 'generate ' + path_json + ' -o ' + path_html + ' --clean'
os.system(allure)

# coding=utf-8
import json
import time
import pandas as pd
import yaml
import os
from pykeyboard import PyKeyboard


def path_file(pro='RED'):
    """
    获取项目所在路径
    """

    path = os.getcwd()
    while 1:
        path = os.path.abspath(os.path.join(path, '..'))
        if os.path.split(path)[-1] == pro:
            break
    return path


def read_yaml_file(file_path):
    """
    读取yaml文件数据
    """
    path = path_file()
    path = path + file_path
    with open(path, 'r', encoding='utf8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        return res


def read_excel_file(file_path, *args):
    if len(args) > 0:
        path = path_file()
        path = path + file_path
        res = []
        df = pd.read_excel(path)
        for i in range(len(df)):
            dic1 = {}
            dic2 = {}
            lst1 = []
            if df['run'][i] == 1 and df['moudle'][i] in args:
                dic1['method'] = df['method'][i]
                dic1['data'] = json.loads(df['data'][i].replace('\n', ''))
                lst1.append(dic1)
                dic2['title'] = df['title'][i]
                lst1.append(dic2)
                res.append(lst1)
        return res
    else:
        path = path_file()
        path = path + file_path
        res = []
        df = pd.read_excel(path)
        for i in range(len(df)):
            dic1 = {}
            dic2 = {}
            lst1 = []
            if df['run'] == 1:
                dic1['method'] = df['method'][i]
                dic1['data'] = json.loads(df['data'][i].replace('\n', ''))
                lst1.append(dic1)
                dic2['title'] = df['title'][i]
                lst1.append(dic2)
                res.append(lst1)
        return res


def reflect(class_name, method):
    func = getattr(class_name, method)
    return func()


def xstr(s):
    """
    none和其他类型转换为字符串
    """

    if s is None:
        return ''
    return str(s)


def case_data_analysis(res):
    """
    主要用于数据中None转为空字符串后再生成新的元组
    参数必须为列表
    """

    lst_keys = []
    lst_values = []
    for i in range(len(res)):
        tup_list_keys = []
        tup_list_values = []
        dic = res[i]
        lst1_keys = list(dic.keys())
        lst1_values = list(dic.values())
        for k in range(len(lst1_keys)):
            lst2 = xstr(lst1_keys[k])
            tup_list_keys.append(lst2)
        for v in range(len(lst1_values)):
            lst2 = xstr(lst1_values[v])
            tup_list_values.append(lst2)
        tup_keys = tuple(tup_list_keys)
        lst_keys.append(tup_keys)
        tup_values = tuple(tup_list_values)
        lst_values.append(tup_values)
    lst_keys = list(set(lst_keys))
    lst_values = list(set(lst_values))
    return lst_keys, lst_values


def dir_file(value, dirs='/TestData/CaseData'):
    """
    获取路径下的文件,根据value查找指定文件
    默认获取 /TestData/CaseData/
    """
    path = path_file()
    path = path + dirs
    file_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            continue
        else:
            file_list.append(file)
    file_list = list(filter(lambda x: x.find(value) >= 0, file_list))
    return file_list


def cut_str(layout, file_list):
    """
    分割列表中的元素并去除空字符串后重新组成列表
    """

    lst = []
    for i in range(len(file_list)):
        b = file_list[i].split(layout)
        if b[0] == '':
            c = b[1]
        else:
            c = b[0]
        lst.append(c)
    return lst


def list_tuple(data):
    """
    把测试用例的yaml文件修改为可执行列表
    """
    lst = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].get('title') is not None:
                c = data[i][j].get('title')
                data[i].remove(data[i][j])
                data[i].append(c)
        a = tuple(data[i])
        lst.append(a)
    return lst


def get_times():
    """
    获取当前时间，生成时间字符串
    """
    get_time = time.localtime()
    get_time = time.strftime("%Y%m%d%H%M%S", get_time)
    return get_time


def upload_file(path):
    """
    上传文件
    """
    k = PyKeyboard()
    time.sleep(1)
    k.type_string(path)
    time.sleep(1)
    k.tap_key(k.enter_key)
    time.sleep(1)


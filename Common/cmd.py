# coding=utf-8

import os
import time


def cmd(stop_container, start_container):

    """
    关闭启动docker容器，防止连接数过多卡死
    """
    if isinstance(stop_container, str):
        os.system("docker stop " + stop_container)
    elif isinstance(stop_container, list):
        for i in range(len(stop_container)):
            os.system("docker stop " + stop_container[i])
    else:
        print('数据类型错误')
    time.sleep(1)
    if isinstance(start_container, str):
        os.system("docker stop " + start_container)
    elif isinstance(start_container, list):
        for i in range(len(start_container)):
            os.system("docker stop " + start_container[i])
    else:
        print('数据类型错误')
    time.sleep(5)



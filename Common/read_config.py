# coding=utf-8

from Common.common import read_yaml_file
import yaml


class ReadConfig(object):

    """
    __init__：获取config.yml路径并读取
    read_ip：获取ip部分的数据信息
    read_docker：获取连接docker的数据信息
    read_url：获取被测地址url的数据信息
    """

    def __init__(self):
        self.res = read_yaml_file('/Source/config.yml')

    def read_ip(self):
        if 'ip' in self.res.keys():
            ip_value = self.res['ip']
            return ip_value
        else:
            print("ip配置信息不存在")

    def read_docker(self):
        if 'docker' in ReadConfig().read_ip():
            docker_value = ReadConfig().read_ip()['docker']
            return docker_value
        else:
            print("docker配置信息不存在")

    def read_url(self):
        if 'url' in ReadConfig().read_ip():
            url_value = ReadConfig().read_ip()['url']
            return url_value







import pymysql


class Mysql(object):

    def __init__(self, host, port, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            port=port,  # 端口
            user=user,  # 用户
            password=password,  # 密码
            database=database,  # 数据库
            charset='utf8',  # 设置编码，此处不能写utf-8
            autocommit=True  # 自动提交
        )
        self.cursor = self.conn.cursor()

    def close_database(self):
        self.conn.close()

    def select_sql(self, table, *args, **kwargs):
        var_str = ''
        var_dic = ''
        for i in args:
            var_str = var_str + i + ','
        var_str = var_str.rstrip(',')
        for k, w in kwargs.items():
            if isinstance(w, str):
                var_dic = var_dic + k + ' = ' + w + ' and '
            if isinstance(w, int):
                var_dic = var_dic + k + ' = ' + str(w) + ' and '
            if isinstance(w, list):
                var_dic = var_dic + k + ' in ' + str(tuple(w)) + ' and '
        var_dic = var_dic.rstrip(' and ')
        if len(args) == 0 and len(kwargs) == 0:
            sql = f'select * from {table}'
        elif len(args) == 0 and len(kwargs) != 0:
            sql = f'select * from {table} where {var_dic}'
        elif len(args) != 0 and len(kwargs) == 0:
            sql = f'select {var_str} from {table}'
        elif len(args) != 0 and len(kwargs) != 0:
            sql = f'select {var_str} from {table} where {var_dic}'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def update_sql(self, table, *args, **kwargs):
        var_str = ''
        var_dic = ''
        for i in range(len(args)):
            if i % 2 == 0:
                var_str = var_str + args[i] + ' = ' + args[i+1] + ','
            else:
                continue
        var_str = var_str.rstrip(',')
        for k, w in kwargs.items():
            if isinstance(w, str):
                var_dic = var_dic + k + ' = ' + w + ' and '
            if isinstance(w, int):
                var_dic = var_dic + k + ' = ' + str(w) + ' and '
            if isinstance(w, list):
                var_dic = var_dic + k + ' in ' + str(tuple(w)) + ' and '
        var_dic = var_dic.rstrip(' and ')
        if len(args) == 0:
            print('没有set值')
        elif len(args) % 2 == 0 and len(kwargs) == 0:
            sql = f'update {table} set {var_str}'
        elif len(args) % 2 == 0 and len(kwargs) != 0:
            sql = f'update {table} set {var_str} where {var_dic}'
        else:
            print('set值参数错误')
        self.cursor.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    a = Mysql('172.16.10.72', 3306, 'root', '123456', 'rongetong_sso')

    b = a.select_sql('sso_login',  mobile='15910000000', is_deleted='1')
    print(b)
    print(b[0][0])
    a.close_database()







import pymysql
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def get_sql_connection():
    """
    生成数据库链接
    :return:
    """
    connection = pymysql.connect(host='rr-m5e0e5azcxvei8lz4524.mysql.rds.aliyuncs.com',
                                 user='hckj1070_58pic',
                                 password='X5SF58@2020#$',
                                 db='db_58pic',
                                 port=3306,
                                 charset='utf8')

    return connection


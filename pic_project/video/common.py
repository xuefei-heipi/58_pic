# -*- coding: utf-8 -*-
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests


def get_sql_connection():
    """
    生成数据库链接
    :return:
    """
    connection = pymysql.connect(host='rm-uf6uj41l039guiek9vo.mysql.rds.aliyuncs.com',
                                 user='hckj1070_58pic',
                                 password='X5SF58@2020#$',
                                 db='db_58pic',
                                 port=3306,
                                 charset='utf8')

    return connection


def is_pic_exist(pic_id, cursor):
    """
    判断素材是否爬取过
    :param pic_id:
    :param competitive_web:
    :param cursor:
    :return:
    """
    sql_search = "select `id` from vjshi_pic_info where `pic_id` = %s limit 1"
    # sql_search = "select pic_id from 58pic_competitor_pic where `c_id` = %s AND `act` = %s"
    if cursor.execute(sql_search, pic_id):
        return True
    return False

def insert_pic(pic_info, cursor):
    """

    :param pic_info:
    :param cursor:
    :return:
    """
    try:
        sql_insert = "insert into vjshi_pic_info (" \
                        "pic_id," \
                        "pic_detail_url," \
                        "pic_title," \
                        "pic_dl_num," \
                        "pic_upload_time," \
                        "pic_price," \
                        "pic_size," \
                        "page_num) values " \
                        "(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_insert, [
            pic_info['pic_id'],
            pic_info['pic_detail_url'],
            pic_info['pic_title'],
            pic_info['pic_dl_num'],
            pic_info['pic_upload_time'],
            pic_info['pic_price'],
            pic_info['pic_size'],
            pic_info['page_num'],
        ])
        cursor.connection.commit()
    except Exception as E:
        print(E)


def lxml_to_dict(lxml_):
    """
    lxml 转 dict
    :param lxml_:
    :return:
    """
    dict_ = ''
    for item in lxml_:
        dict_ += item

    return eval(dict_)

def get_elements_by_xpath(driver, xpath):
    """
    获取组元素
    :param driver:
    :param xpath:
    :return:
    """
    try:
        elements = driver.find_elements(By.XPATH, xpath)
        return elements
    except:
        return []


def browser():
    """
    浏览器驱动生成
    :return:
    """
    # ip = '123.163.118.203:9999'
    chrome_options = Options()
    # ip代理
    # chrome_options.add_argument('--proxy-server=' + ip)
    # chrome_options.add_extension('D:/chajian/vimm_chrome_proxyauth_plugin.zip')


    chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument("--user-data-dir=C:/Users/Dell/AppData/Local/Google/Chrome/User Data")    #使用当前chrome插件
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-plugins')
    # chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示   已经不支持了

    chrome_options.add_experimental_option("excludeSwitches",
                                           ['enable-automation', 'enable-logging'])  # 禁用浏览器正在被自动化程序控制的提示
    chrome_options.add_experimental_option('w3c', False)
    chrome_options.add_argument('--enable-audio-focus=true')

    # chrome_options.add_argument('--no-sandbox')  # 浏览器插件奔溃
    # chrome_options.add_argument('--window-size=2062,1126')  # 设置浏览器分辨率（窗口大小）
    # chrome_options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    # chrome_options.add_argument('--blink-sett=imagesEnabled=false')  # 不加载图片, 提升速度已经不支持了
    # 不加载图片, 提升速度
    prefs = {"profile.managed_default_content_settings.images": 2,}

    # 不加载图片, 提升速度  js  css  弹框
    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'images': 2,
    #         'javascript': 2,
    #         'notifications': 2,
    #     },
    #     'permissions.default.stylesheet': 2
    # }
    #
    chrome_options.add_experimental_option('prefs', prefs)

    # chrome_options.add_argument('headless') #无头浏览
    # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # chrome_options.add_argument('--disable-javascript')  # 禁用javascript
    # chrome_options.add_argument('–disable-software-rasterizer')
    # chrome_options.add_argument('--disable-extensions')

    # chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 9.0; Win64; x64) AppleWebKit/537.36 '
    #                             '(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')   #设置user-agent

    # 允许flash自动运行
    # prefs = {
    #     "profile.managed_default_content_settings.images": 1,
    #     "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    #     "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    # }
    # chrome_options.add_experimental_option('prefs', prefs)

    # chrome_driver_path = os.getcwd() + '\chromedriver.exe'
    # d = DesiredCapabilities.CHROME
    # d['loggingPrefs'] = { 'performance':'ALL' }

    # chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

    driver = webdriver.Chrome(chrome_options=chrome_options)

    # chrome_driver_path = 'C:/Users/Dell/AppData/Local/Google/Chrome/Application/chrome.exe'
    # driver = webdriver.Chrome(executable_path=chrome_driver_path,)

    return driver


def dl_jpg(url, jpg_name):
    try:

        r = requests.get(url, timeout=5, stream=True)
        if r.status_code != 200:
            return

        with open(jpg_name, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        import os
        for  files in os.walk(r'D:\envato'):
            res = files[2]



        sql_update = "SELECT * FROM `58pic_envato_info` ORDER BY pic_dl_num desc LIMIT 500;"
        cursor.execute(sql_update)
        rows = cursor.fetchall()
        for row in rows:
            pic_id = row['pic_id']
            pic_img_url = row['pic_img_url']
            pic_path = r'D:\envato\%s.jpg' % str(pic_id)
            key = True
            for x in res:
                if str(pic_id) in x:
                    key = False
            # dl_jpg(pic_img_url, pic_path)
            if key:
                print(pic_id)
                dl_jpg(pic_img_url, pic_path)

    finally:
        cursor.close()
        connection.close()



import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pymysql
# coding=utf-8
import csv
import json
import re

import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver



def browser(driver_type=1):
    """
    浏览器驱动生成
    :param driver_type: 类别
    :return:
    """

    if driver_type == 1:

        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')

        # chrome_options.add_argument("load-extension=C:/Users/Dell/Desktop/chajian/1.3.11_0");    #使用当前chrome插件
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-plugins')
        # chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示   已经不支持了

        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])  # 禁用浏览器正在被自动化程序控制的提示
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

    elif type == 2:
        driver = webdriver.Firefox()

    elif type == 3:
        driver = webdriver.Ie()

    # 设置执行js代码转换模式
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })

    return driver

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
    sql_search = "select `id` from `58pic_envato_element`  where `pic_id` = %s limit 1"
    # sql_search = "select pic_id from 58pic_competitor_pic where `c_id` = %s AND `act` = %s"
    if cursor.execute(sql_search, [pic_id]):
        return True
    return False

def insert_pic(pic_id, pic_detail_url, pic_title, cursor):
    """

    :param pic_id:
    :param pic_detail_url:
    :param pic_title:
    :param cursor:
    :return:
    """
    try:
        sql_insert = "insert into `58pic_envato_element`(" \
                        "pic_id," \
                        "pic_detail_url," \
                        "pic_title) values " \
                        "(%s, %s, %s)"
        cursor.execute(sql_insert, [
            pic_id,
            pic_detail_url,
            pic_title
        ])
        cursor.connection.commit()
    except Exception as E:
        print(E)

def update_pic(cursor, id, pic_img_url, pic_mp4_url, first_category, second_category, application_supported,
               length, resolution, file_size, tags):
    """

    :param cursor:
    :param id:
    :param pic_img_url:
    :param pic_mp4_url:
    :param first_category:
    :param second_category:
    :param application_supported:
    :param length:
    :param resolution:
    :param file_size:
    :param tags:
    :return:
    """
    try:
        sql_update = "update `58pic_envato_element` set " \
                        "`pic_img_url` = %s," \
                        "`pic_mp4_url` = %s," \
                        "`first_category` = %s," \
                        "`second_category` = %s," \
                        "`application_supported` = %s," \
                        "`length` = %s," \
                        "`resolution` = %s," \
                        "`file_size` = %s," \
                        "`tags` = %s where `id` = %s limit 1"

        cursor.execute(sql_update, [
            pic_img_url,
            pic_mp4_url,
            first_category,
            second_category,
            application_supported,
            length,
            resolution,
            file_size,
            tags,
            id
        ])
        cursor.connection.commit()
    except Exception as E:
        print(E)


def find_by_xpath(html, xpath, num):
    try:
        return  html.xpath(xpath)[num]
    except:
        return ''

def dl_jpg(pic_local_path, img_url):
    try:
        r = requests.get(url=img_url, timeout=5)
        with open(pic_local_path, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
    except Exception as E:
        print(E)
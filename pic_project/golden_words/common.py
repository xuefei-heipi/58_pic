# -*- coding: utf-8 -*-
import logging
import time
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from golden_words.qiniu_upload import qiniu_upload
from golden_words.youpai import YouPai
from lxml import etree
from requests.exceptions import ConnectTimeout
from golden_words.daili import get_plugin



def write_log():
    """
    记录日志
    :return:
    """
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # log_path = os.path.dirname(os.getcwd()) + '/golden_words/'
    log_path = r'D:/logger/'
    logfile = log_path + rq + 'search.log'
    print(logfile)
    # print(logfile)
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)

    return logger
    # 日志
    # logger.debug('this is a logger debug message')
    # logger.info('this is a logger info message')
    # logger.warning('this is a logger warning message')
    # logger.error('this is a logger error message')
    # logger.critical('this is a logger critical message')

def processing_data(data):
    """
    处理爬取的数据
    :param data:
    :return:
    """
    try:
        # print(data)
        #判断是否为list
        if isinstance(data, list):
            #判断list 是否为空
            if len(data) > 0:
                #去除str 中的换行 和 前后的空格(srtip)
                data = data[0].replace('\r\n', '').replace('\n', '').strip()

            else:
                return ''
        #判断是否为str
        elif isinstance(data, str):
            #去除 str 中的空格和换行
            data = data.replace('\r\n', '').replace(' ', '').replace('\n', '')
    except:
        data = ''
    return data

def processing_str(data, type=1):
    """
    处理字符串
    :param data:
    :param type:
    :return:
    """
    # 判断是否是字符串
    if isinstance(data, str):
        # 如果type = 1的话 删除所有换行 回车 空格
        if type == 1:
            return data.replace('\r\n', '').replace(' ', '').replace('\n', '')
        # 如果type = 1的话 删除所有换行 回车  首末的空格
        elif type == 2:
            return data.replace('\r\n', '').replace('\n', '').strip()
        # 如果type = 3的话 先将多个空格和平成一个 删除所有换行 回车  首末的空格
        elif type == 3:
            return ' '.join(data.split()).strip().replace('\r\n', '').replace('\n', '')
    return data


def processing_list(list):
    """
    处理昵图特殊的list
    :param list:
    :return:
    """
    try:
        list_ = []
        for x in range(len(list)):
            if '\n' not in list[x]:
                list_.append(list[x])

        return list_
    except:
        return []

def get_sql_connection():
    """
    生成数据库链接
    :return:
    """
    connection = pymysql.connect(
                                 # host='rm-uf6uj41l039guiek9vo.mysql.rds.aliyuncs.com',
                                 # user='hckj1070_58pic',
                                 # password='X5SF58@2020#$',
                                 # db='db_58pic',
                                 host='localhost',
                                 user='root',
                                 password='',
                                 db='autotest',
                                 port=3306,
                                 charset='utf8')


    return connection

def is_pic_exist(pic_url, cursor):
    """
    判断素材是否爬取过
    :param pic_id:
    :param competitive_web:
    :param cursor:
    :return:
    """
    sql_search = "select `id` from 58pic_competitive_info where `pic_url` = %s limit 1"
    # sql_search = "select pic_id from 58pic_competitor_pic where `c_id` = %s AND `act` = %s"
    if cursor.execute(sql_search, pic_url):
        return True
    return False

def insert_pic(pic_info, cursor, logger):
    """

    :param pic_info:
    :param cursor:
    :param logger:
    :return:
    """
    try:
        isert_sql = "insert into 58pic_competitive_info (" \
                    "pic_id," \
                    "competitive_web," \
                    "pic_title," \
                    "pic_url," \
                    "img_url," \
                    "pic_authorization," \
                    "create_time," \
                    "upload_time," \
                    "pic_volume," \
                    "pic_dpi," \
                    "pic_size," \
                    "pic_format," \
                    "pic_color_mode," \
                    "pic_price," \
                    "pic_key_word," \
                    "qn_img_url," \
                    "search_word," \
                    "search_word_id) values " \
                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(isert_sql, [
            pic_info['pic_id'],
            pic_info['competitive_web'],
            pic_info['pic_title'],
            pic_info['pic_url'],
            pic_info['img_url'],
            pic_info['pic_authorization'],
            pic_info['create_time'],
            pic_info['upload_time'],
            pic_info['pic_volume'],
            pic_info['pic_dpi'],
            pic_info['pic_size'],
            pic_info['pic_format'],
            pic_info['pic_color_mode'],
            pic_info['pic_price'],
            pic_info['pic_key_word'],
            pic_info['qn_img_url'],
            pic_info['search_word'],
            pic_info['search_word_id']
        ])
        cursor.connection.commit()
    except Exception as E:
        logger.warning(E)


def browser(ip):
    """
    浏览器驱动生成
    :return:
    """
    print('browser %s' %ip)
    # ip = '123.163.118.203:9999'
    chrome_options = Options()
    # ip代理
    chrome_options.add_argument('--proxy-server=' + ip)
    # chrome_options.add_extension('D:/QTproject/Python_script/golden_words/chajian/vimm_chrome_proxyauth_plugin.zip')
    chrome_options.add_extension('D:/chajian/vimm_chrome_proxyauth_plugin.zip')


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
    driver.set_page_load_timeout(5)
    return driver

def proxies_ip(ip_port):
    """
    获取代理认证
    :param ip_port:
    :return:
    """
    proxies_ip_https = 'https://422477075:rqxomyv9@%s' % ip_port
    proxies_ip_http = 'http://422477075:rqxomyv9@%s' % ip_port
    proxies = {}
    proxies["https"] = proxies_ip_https
    proxies["http"] = proxies_ip_http
    return proxies


def check_ip(ip_port):
    #获取当前访问使用的IP地址网站
    # url="https://www.ipip.net/"
    url="https://www.baidu.com/"
    #设置代理，从西刺免费代理网站上找出一个可用的代理IP
    # proxies = pro_ip #此处也可以通过列表形式，设置多个代理IP，后面通过random.choice()随机选取一个进行使用
    # print(proxies)
    # ip_check = ip_port.split(':')[0]
    proxies = proxies_ip(ip_port)
    print(proxies)
    #使用代理IP进行访问
    try:
        # headers = {
        #     'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'zh-CN,zh;q=0.9',
        #     'Connection': 'keep-alive',
        #     'Cookie': 'LOVEAPP_SESSID=fb628f22e5823ef1f0e01e0cad229127ab6cda6c; __jsluid_s=ac61cd9260b2a4495334921c1fbac9ae; _ga=GA1.2.1633830342.1602678714; _gid=GA1.2.1662338466.1602678714; Hm_lvt_6b4a9140aed51e46402f36e099e37baf=1602678714; Hm_lpvt_6b4a9140aed51e46402f36e099e37baf=1602678714',
        #     'Sec - Fetch - Mode': 'navigate',
        #     'Sec - Fetch - Site': 'none',
        #     'Host': 'www.ipip.net',
        #     'Sec - Fetch - User': '?1',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        # }
        res = requests.get(url, proxies=proxies, timeout=5)
        if res.status_code == 200: # 状态码
        # content=res.text
        # html=etree.HTML(content)
        # ip = html.xpath('//ul[@class="inner"]/li[1]/a/text()')[0]
            print(ip_port)
            return True
    except:
        print('超时了')
        return False


def read_pro_ip():
    """
    去读ip.txt 文件中的 ip地址
    :return:
    """
    with open('ip.txt', 'r', encoding='utf-8') as f:
        pro_ip = f.read()

    print("old_ip 为 : %s" % pro_ip)
    return pro_ip

def write_pro_ip(pro_ip):
    """
    将接口请求回来的ip地址写到文件中
    :return:
    """

    with open('ip.txt', 'w', encoding='utf-8') as f:
        # f.write('{"https": "https://10.10.1.10:1081"}')
        f.write(pro_ip)




def get_content_by_xpath(driver, xpath, type=1):
    """
    获取 textContent
    :param driver:
    :param xpath:
    :param type:如果type = 1的话 删除所有换行 回车 空格    如果type = 2 的话 删除所有换行 回车 首末的空格
    :return:
    """
    try:
        res = driver.find_element(By.XPATH, xpath).get_attribute('textContent')
        res = processing_str(res, type)
        return res
    except:
        return ''

def get_dom_src(driver, xpath, src, type=1):
    """
    获取 dom 中 src的信息
    :param driver:
    :param xpath:
    :param src:
    :param type: 如果type = 1的话 删除所有换行 回车 空格    如果type = 2 的话 删除所有换行 回车 首末的空格
    :return:
    """
    try:
        res = driver.find_element(By.XPATH, xpath).get_attribute(src)
        res = processing_str(res, type)
        return res
    except Exception as E:
        print(E)
        return ''

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

def remove_img(path):

    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception as E:
        print(E)



def upload_pic(pic_id, img_url):

    try:
        # 图片本地保存的地址
        pic_local_path = r'D:/competitive_img/%s.jpg' % str(pic_id)
        print('图片本地地址： %s' % pic_local_path)
        # 下载图片
        num = 0
        requests_error = False
        requests_res = True
        while requests_res:
            try:
                ip_port = read_pro_ip()
                proxies = proxies_ip(ip_port)
                r = requests.get(url=img_url, proxies=proxies, timeout=5)
                requests_res = False
            except Exception as E:
                print(E)
                # if create_daili_browser(1):
                #     pass
                if num < 20:
                    time.sleep(5)
                    num += 1
                else:
                    requests_error = True
                    requests_res = False
        if requests_error:
            raise ValueError("ip使用连续失败10次不能运行")

        if r.status_code == 200:
            with open(pic_local_path, 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
        print('下载图片完成')

        key_time = int(round(time.time()))
        # 作品 在七牛的地址
        key = 'images/competitive/%s_%s.jpg' % (str(key_time), str(pic_id))
        localfile = pic_local_path
        # 写入数据库的字段  奇葩的七牛上传的时候不能带 /
        insert_key = '/' + key
        # 上传七牛
        qiniu_upload(key, localfile)
        print('上传七牛图片完成')
        # 上传 又拍
        YouPai().yp_up_load(pic_local_path, insert_key)
        print('上传又拍图片完成')
        # 删除本地图片
        remove_img(pic_local_path)
        print('删除本地图片完成')
        upload_pic_info = {
            'upload_img_url': insert_key,  # 七牛保存的图片地址
            'upload_time': key_time  # 上传七牛的时间
        }
        print(upload_pic_info)
        return upload_pic_info
    except Exception as E:
        print(E)
        return False

def dai_ip():
    """
    通过第三方代理 获取ip
    :return:
    """
    response = requests.get(
        url='https://dps.kdlapi.com/api/getdps/?orderid=920369295632173&num=1&pt=1&format=json&sep=1')
    ip = response.json()["data"]['proxy_list'][0]
    print('获取了一次代理ip')
    print('代理ip是：%s' % ip)
    return ip

def create_daili_browser(type=1):
    """
    检测当前ip，以及生成新的ip
    :param type: type == 1 不需要生成browser  type == 2 需要生成browser
    :return:
    """
    # 如果连续失败10次 就不在试了 一个月才1000个ip
    with open('ip_max.txt', 'r') as f:
        num = int(f.read())
    if num > 10:
        return False
    # 获取当前文件ip
    old_ip = read_pro_ip()
    # 判断当前文件ip 是否有效
    check_result = check_ip(old_ip)
    if check_result:
        # 当前ip可用，不需要重新生成 但是需要 重新生成一下插件
        # 生成新插件
        ip = old_ip.split(':')[0]
        port = old_ip.split(':')[1]
        # 成功了 以后 将次数改为0
        with open('ip_max.txt', 'w') as f:
            f.write('0')
        if type == 2:
            get_plugin(ip, port)
            driver = browser(old_ip)
            return driver
        return old_ip
    # 获取一次代理ip + 1
    new_ip = dai_ip()
    num += 1
    with open('ip_max.txt', 'w') as f:
        f.write(str(num))
    write_pro_ip(new_ip)
    return create_daili_browser(type)



def requests_daili(url, headers, requests_res):
    """
    使用代理请求
    :param url:
    :param headers:
    :param requests_res:
    :return:
    """
    num = 0
    while requests_res:
        try:
            ip_port = read_pro_ip()
            proxies = proxies_ip(ip_port)
            response = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)
            return  response
        except Exception as E:
            print(E)
            if num > 20:
                # requests_error = True
                # requests_res = False
                return False
            time.sleep(5)
            num += 1



if __name__ == '__main__':

    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM `58pic_gaoding` where id >368'
    cursor.execute(sql)
    rows = cursor.fetchall()
    try:

        for row in rows:
            try:
                url = row['img_url'].split('?x-oss-process=image')[0]
                print(row['pic_id'])
                pic_local_path = 'D:/gaoding/%s.jpg' % str(row['pic_id'])
                # print(row['pic_id'], row['img_url'])
                r = requests.get(url)
                with open(pic_local_path, 'wb') as fd:
                    for chunk in r.iter_content():
                        fd.write(chunk)
                time.sleep(1)
            except:
                pass
    finally:
        cursor.close()
        connection.close()

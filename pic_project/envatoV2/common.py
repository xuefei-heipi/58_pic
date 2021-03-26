import pymysql
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
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
    sql_search = "select `id` from `58pic_envatov2`  where `pic_id` = %s limit 1"
    # sql_search = "select pic_id from 58pic_competitor_pic where `c_id` = %s AND `act` = %s"
    if cursor.execute(sql_search, pic_id):
        print('这个id爬过:%d' % pic_id)
        return True
    return False

def insert_pic(pic_id, pic_detail_url, pic_sales, pic_stars, cursor):
    """

    :param pic_id:
    :param pic_detail_url:
    :param pic_title:
    :param cursor:
    :return:
    """
    try:
        sql_insert = "insert into `58pic_envatov2` (" \
                        "pic_id," \
                        "pic_detail_url," \
                        "pic_sales," \
                        "pic_stars) values " \
                        "(%s, %s, %s, %s)"
        cursor.execute(sql_insert, [
            pic_id,
            pic_detail_url,
            pic_sales,
            pic_stars
        ])
        cursor.connection.commit()
    except Exception as E:
        print(E)


def find_by_xpath(html, dom_xpath, num):
    try:
        return  html.xpath(dom_xpath)[num]
    except:
        return ''

def update_pic(pic_id, pic_infos, cursor):
    """

    :param cursor:
    :param id:
    :param pic_infos:
    :return:
    """
    try:
        sql_update = "update `58pic_envatov2` set " \
                        "`pic_title` = %s," \
                        "`pic_img_url` = %s," \
                        "`pic_mp4_url` = %s," \
                        "`pic_price` = %s," \
                        "`first_category` = %s," \
                        "`second_category` = %s," \
                        "`third_category` = %s," \
                        "`fourth_category` = %s," \
                        "`comments` = %s," \
                        "`last_update` = %s," \
                        "`created` = %s," \
                        "`alpha_channel` = %s," \
                        "`looped_video` = %s," \
                        "`frame_rate` = %s," \
                        "`resolution` = %s," \
                        "`video_encoding` = %s," \
                        "`file_size` = %s," \
                        "`number_of_clips` = %s," \
                        "`total_clip_length` = %s," \
                        "`individual_clip_lengths` = %s," \
                        "`tags` = %s where `pic_id` = %s limit 1"

        cursor.execute(sql_update, [
            pic_infos['pic_title'],
            pic_infos['pic_img_url'],
            pic_infos['pic_mp4_url'],
            pic_infos['pic_price'],
            pic_infos['first_category'],
            pic_infos['second_category'],
            pic_infos['third_category'],
            pic_infos['fourth_category'],
            pic_infos['comments'],
            pic_infos['last_update'],
            pic_infos['created'],
            pic_infos['alpha_channel'],
            pic_infos['looped_video'],
            pic_infos['frame_rate'],
            pic_infos['resolution'],
            pic_infos['video_encoding'],
            pic_infos['file_size'],
            pic_infos['number_of_clips'],
            pic_infos['total_clip_length'],
            pic_infos['individual_clip_lengths'],
            pic_infos['tags'],
            pic_id
        ])
        cursor.connection.commit()
    except Exception as E:
        print(E)



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


def dl_jpg(pic_local_path, img_url):

    try:
        r = requests.get(url=img_url, timeout=5)
        with open(pic_local_path, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
    except Exception as E:
        print(E)

if __name__ == '__main__':

    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        with open('./pic6.json', 'w+') as file:
            sql_search = 'SELECT * FROM `58pic_envatov2` limit 15001, 18214'
            cursor.execute(sql_search)
            rows = cursor.fetchall()
            file.writelines('[' + '\n')
            for row in rows:
                pid = row['pic_id']
                purl = row['pic_img_url']
                write = '{"pid":"%d","purl":"%s"},' % (pid, purl)
                file.writelines(write + '\n')
            file.writelines(']')

        # time.sleep(600)
    except Exception as E:
        print(E)

    finally:
        cursor.close()
        connection.close()


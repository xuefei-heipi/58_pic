from concurrent.futures import ThreadPoolExecutor
from time import ctime, sleep
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Product.spbackstage.qt_backstage import QTBackstage
from django.conf import settings
# settings.configure()

def browser():
    '''
    浏览器驱动生成
    :return: 
    '''
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 禁用浏览器正在被自动化程序控制的提示
    chrome_options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    return driver

def add_cookies(driver, user_cookie, user_referer, user_id, type):

    # 添加localstorage记录

    #格式化时间戳为标准格式
    #time.strftime('%Y.%m.%d', time.localtime(time.time()))
    time_day = time.strftime('%d', time.localtime(time.time()))
    # time_month = time.strftime('%m', time.localtime(time.time()))

    driver.get('https://www.58pic.com/index.php?m=HelpCenter')

    #添加localStorge
    local_storge_data_JS = [
        'localStorage.setItem("is_show_guide", "1")',
        'localStorage.setItem("activBottom",%s)' %time_day,
        'localStorage.setItem("activRight", %s)' %time_day
    ]
    for JS in local_storge_data_JS:
        driver.execute_script(JS)

    expiry_time = 15488452170
    if type == 1:

        cookies = [
            {'domain': '.58pic.com', 'secure': True,
             'value': 'NDI2ODg1MzF8MTU0MDg5MDE3N3xmYjkwNWE2YzMwNjEyNDMzOGU2ODgyZTkyZjZmNDVhOA%3D%3D', 'httpOnly': True,
             'expiry': expiry_time, 'path': '/', 'name': '_auth_dl_'},
            {'domain': '.58pic.com', 'secure': False,
             'value': user_cookie, 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'auth_id'},
            {'domain': '.58pic.com', 'secure': False,
             'value': '%224ac7049f557063d01fbe2b259aeaac69%22', 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'qt_visitor_id'},
            {'domain': '.58pic.com', 'secure': False,
             'value': user_referer, 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'referer'}
        ]
    elif type == 2:
        cookies = [
            # {'domain': '.58pic.com', 'secure': True,
            #  'value': 'NDI2ODg1MzF8MTU0MDg5MDE3N3xmYjkwNWE2YzMwNjEyNDMzOGU2ODgyZTkyZjZmNDVhOA%3D%3D', 'httpOnly': True,
            #  'expiry': expiry_time, 'path': '/', 'name': '_auth_dl_'},
            {'domain': '.58pic.com', 'secure': False,
             'value': user_cookie, 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'auth_id'},    #控制登陆
            {'domain': '.58pic.com', 'secure': False,
             'value': '%224ac7049f557063d01fbe2b259aeaac69%22', 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'qt_visitor_id'},  #控制AB测试
            {'domain': '.58pic.com', 'secure': False,
             'value': 'patchOne%3A2%2CtimeOne%3A21%2CtimeEnd%3A6', 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'first-charge-' + str(user_id) + '_10'} #控制首次充弹框
        ]


    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://www.58pic.com/')
    driver.refresh()

def get_console(driver, url, error_list):
    '''
    获取控制台信息
    :param driver: 
    :param url: 
    :return: 
    '''
    error_num = 0
    driver.get(url[0])
    driver.refresh()
    sleep(1)
    driver.log_types
    error_log = []

    from Product.models import ConsoleErrorIgnore as ceignore
    ce_ignore = ceignore.objects.filter()
    #排除一次干扰的无用的报错数据
    for console_log in driver.get_log('browser'):
        # if 'goo.gl' in console_log['message'] \
        #         or 'api.share.baidu.com' in console_log['message'] \
        #         or 'WARNING' in console_log['level'] \
        #         or 'wx.qlogo.cn' in console_log['message']\
        #         or 'https://icon.58pic.com' in console_log['message']\
        #         or 'analytics.58pic.com/sa.gif' in console_log['message']\
        #         or 'bdimg.share.baidu.com' in console_log['message']:
        #     pass

        if 'WARNING' in console_log['level']:
            pass
        else:
            error = 1
            for ce_i in ce_ignore:
                if ce_i.errorContent in console_log['message']:
                    error = 0
                    break
            if error == 0:
                pass
            else:
                error_num += 1
                error_log.append(console_log)
    if error_num != 0:
        error_str = '%s 出错url：%s ======== %s' %(url[1], url[0], error_log)
        print(error_str)
        error_list.append(error_str)

def check_page(urls, user_cookie, user_referer, user_id, position_num, error_lsit):
    ''' 
    检测url报错
    :param urls: 
    :param user_cookie: 
    :param user_referer: 
    :param user_id: 
    :param position_num: 控制多线程时 浏览器窗口在左面的位置
    :return: 
    '''
    driver = browser()
    driver.set_window_size(1032, 564)
    if position_num == 0:
        driver.set_window_position(0,0)
    elif position_num == 1:
        driver.set_window_position(1032,0)
    elif position_num == 2:
        driver.set_window_size(2048, 564)
        driver.set_window_position(0, 564)
    elif position_num == 3:
        driver.set_window_position(1032, 564)
    # driver.maximize_window()
    # print(driver.get_window_size())
    driver.implicitly_wait(30)
    add_cookies(driver, user_cookie, user_referer, user_id, 2)
    # get_console(driver, urls[0])
    # add_cookies(driver, user_cookie, 1)
    end_num = len(urls)
    for x in range(1, end_num):
        get_console(driver, urls[x], error_lsit)

    driver.quit()

def get_user_cookies(username, password):
    '''
    获取账号登录的cookie
    :param username: 
    :param password: 
    :return: 
    '''
    login_by_passwd_new_request_url = 'https://www.58pic.com/index.php?m=userinfo&a=loginByPasswdNew'
    datas = {
        'username': username,
        'userpass': password
    }
    response = requests.post(url=login_by_passwd_new_request_url, data=datas)

    # 判断账号是否被封禁
    if response.cookies.get('auth_id') == None:
        print('账号被封禁，或账号不存在')
        return '账号被封禁，或账号不存在!'

    new_cookie = response.cookies.get('auth_id')
    uid = str(new_cookie).replace('%22', '').split('%')[0]
    referer = response.cookies.get('referer')

    return new_cookie, uid, referer

if __name__ == '__main__':
    start_time = ctime()
    username = 'ogcugctest13'
    password = '123456'
    user_cookies = get_user_cookies(username, password)
    user_cookie = user_cookies[0]
    user_id = user_cookies[1]

    user_referer = user_cookies[2]
    urls = [
        [
        ['https://www.58pic.com', '新主页'],
        ['https://www.58pic.com','新主页'],
        ['https://www.58pic.com/tupian/dongtian.html',  '普通搜索页'],
        ['https://www.58pic.com/tupian/shishidididaodao.html',  '搜索推荐页'],
        ['https://www.58pic.com/tupian/ip.html','ip搜索页'],
        ['https://www.58pic.com/u/'+user_id +'/', '个人主页'],
        ['https://www.58pic.com/u/'+user_id +'/c/create', '个人收藏页'],
        ['https://www.58pic.com/u/'+user_id +'/f/fans', '个人关注页'],
        ['https://www.58pic.com/u/'+user_id +'/edit', '个人主页编辑页'],
        ['https://www.58pic.com/u/'+user_id +'/upload', '个人上传页'],
        ['https://www.58pic.com/u/32606934/', '他人主页'],
        ['https://www.58pic.com/u/32606934/c/create', '他人收藏页'],
        ['https://www.58pic.com/u/33462937/c/favorites', '他人收藏页关注'],
        ['https://www.58pic.com/u/32606934/f/fans', '他人关注页'],
        ['https://www.58pic.com/u/32606934/f/atten', '他人关注的人'],
        ['https://www.58pic.com/u/'+user_id +'/mc', '管理中心-管理首页'],
        ['https://www.58pic.com/u/'+user_id +'/mc/upload/editing', '管理中心页-作品管理页'],
        ['https://www.58pic.com/u/'+user_id +'/mc/authentication', '管理中心页-认证管理页'],
        ['https://www.58pic.com/u/'+user_id +'/dw', '管理中心页-我的下载页'],
        ['https://www.58pic.com/u/'+user_id +'/resume', '云简历页'],
        ['https://www.58pic.com/u/'+user_id +'/vip', 'VIP中心页'],
        ['https://www.58pic.com/index.php?m=IntegralMall', '积分商城页']
    ],
   [
        ['https://www.58pic.com/piccate/2-0-0.html', '分类页-平面广告'],
        ['https://www.58pic.com/piccate/3-0-0.html', '分类页-电商淘宝'],
        ['https://www.58pic.com/piccate/4-0-0.html', '分类页-装饰装修'],
        ['https://www.58pic.com/piccate/5-0-0.html', '分类页-网页UI'],
        ['https://www.58pic.com/piccate/6-0-0.html', '分类页-视频'],
        ['https://www.58pic.com/piccate/6-133-0.html', '分类页-音效'],
        ['https://www.58pic.com/piccate/6-133-0-g1758_1774_1773.html', '分类页-视频音效/配乐音效'],
        ['https://www.58pic.com/piccate/7-0-0.html', '分类页-产品工业'],
        ['https://www.58pic.com/piccate/10-0-0.html', '分类页-背景'],
        ['https://www.58pic.com/piccate/11-0-0.html', '分类页-设计元素'],
        ['https://www.58pic.com/piccate/16-0-0.html', '分类页-手机用图'],
        ['https://www.58pic.com/piccate/17-0-0.html', '分类页-插画绘画'],
        ['https://www.58pic.com/piccate/40-0-0.html', '分类页-字库'],
        ['https://www.58pic.com/piccate/8-0-0.html', '分类页-PPT模板'],
        ['https://www.58pic.com/piccate/12-0-0.html', '分类页-Excel模板'],
        ['https://www.58pic.com/piccate/14-0-0.html', '分类页-简历模板'],
        ['https://www.58pic.com/piccate/15-0-0.html', '分类页-Word模板'],
        # ['https://www.58pic.com/piccate/35-0-0.html', '分类页-教育文档'],
        # ['https://www.58pic.com/piccate/36-0-0.html', '分类页-专业资料'],
        # ['https://www.58pic.com/piccate/38-0-0.html', '分类页-办公文档'],
        ['https://www.58pic.com/piccate/16-373-0.html', '分类页-表情包配图'],
        ['https://www.58pic.com/zuixin', '最新页-老页面没有入口']

    ],
    [
        ['https://www.58pic.com/newpic/33205448.html', '视频详情页'],
        ['https://www.58pic.com/newpic/34358147.html', '音频详情页'],
        ['https://www.58pic.com/newpic/32837867.html', '字库汉仪详情页'],
        ['https://www.58pic.com/newpic/32822151.html', '字库义启详情页'],
        ['https://www.58pic.com/newpic/32822244.html', '字库印品字库详情页'],
        ['https://www.58pic.com/newpic/32822064.html', '字库XFont详情页'],
        ['https://www.58pic.com/newpic/34221648.html', '字库仓耳字库详情页'],
        ['https://www.58pic.com/newpic/28772429.html', '普通详情页'],
        ['https://www.58pic.com/newpic/32512361.html', 'IP详情页'],
        ['https://www.58pic.com/index.php?m=convergePage', '创意趋势'],
        ['https://www.58pic.com/index.php?m=sponsor&a=indexnew&f=4&t=2&p_r=9',  '原创充值页'],
        ['https://www.58pic.com/index.php?m=sponsor&a=indexnew&f=4&t=3&p_r=9',  '共享充值页'],
        ['https://www.58pic.com/index.php?m=sponsor&a=officeVip&p_r=9', '办公充值页'],
        ['https://www.58pic.com/index.php?m=sponsor&a=indexnew&f=4&t=4&p_r=9',  '超级VIP充值页'],
        ['https://www.58pic.com/index.php?m=companyVip&p_r=9',  '企业VIP充值页'],
        ['https://www.58pic.com/index.php?m=FontLibrary&a=sponsorFont&font_vip_type=1',  '字体充值页49.9'],
        ['https://www.58pic.com/index.php?m=FontLibrary&a=sponsorFont&font_vip_type=2',  '字体充值页499'],
        ['https://www.58pic.com/index.php?m=FontLibrary&a=sponsorFont&font_vip_type=3',  '字体充值页999'],
        ['https://www.58pic.com/index.php?m=ogcintro', '特邀申请页'],
        ['https://ppt.58pic.com', 'ppt页面']
    ]
]

    error_list = []
    max_pools = 3
    pool = ThreadPoolExecutor(max_workers=max_pools)
    for x in range(max_pools):
        pool.submit(check_page, urls[x], user_cookie, user_referer, user_id, x, error_list)
    # future1 = pool.submit(check_page, urls[0], user_cookie, user_referer, user_id, 0,)
    # future2 = pool.submit(check_page, urls[1], user_cookie, user_referer, user_id, 1,)
    # future3 = pool.submit(check_page, urls[2], user_cookie, user_referer, user_id, 2,)

    pool.shutdown()



    print(error_list)
    end_time = ctime()


    qtbkstage = QTBackstage()
    qtbkstage.clear_browse_record(user_id)

    print(start_time)
    print(end_time)




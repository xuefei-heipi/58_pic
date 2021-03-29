# coding=utf-8
from Product.basefunction.basefun import BaseFunction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time,os,datetime
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

class CommonFunction(BaseFunction):
    def mouse_above(self, element_path):
        '''
        #鼠标悬浮
        :param element_path: 
        :return: 
        '''
        above = self.driver.find_element_by_xpath(element_path)
        ActionChains(self.driver).move_to_element(above).perform()


    def dominant_wait(self, element_path):
        '''
        #显性等待
        :param element_path: 
        :return: 
        '''
        locator = (By.XPATH, element_path)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))  # 显性等待5秒,等待元素出现
        # element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(element_path))  # 显性等待5秒,等待元素出现
        return element

    def find_element_by_Js(self, element_path):
        '''
        #通过滚动条滚动查找元素
        :param element_path:  
        :return: 
        '''
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        target = self.driver.find_element_by_xpath(element_path)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(0.5)

    def driver_execute_script01(self):
        '''
        当前滚动条向上移动500像素
        :return: 
        '''
        js1 = 'var q=document.documentElement.scrollTop=500'
        self.driver.execute_script(js1)


    def driver_execute_script02(self, num):
        '''
        当前滚动条位置向下移动num像素
        :return: 
        '''
        js2 = 'var location=document.documentElement.scrollTop;' \
              'var b=document.documentElement.scrollTop=(location+'+str(num)+')'

        self.driver.execute_script(js2)

    def new_window_open(self):
        '''
        新开首页
        :return: 
        '''
        #'https://www.58pic.com/'
        js = "window.open('https://www.58pic.com/')"
        self.driver.execute_script(js)
        time.sleep(1)
        self.switch_to_window_close()


    def switch_to_frame(self, frame_id):
        '''
        #跳进iframe
        :param frame_id: 
        :return: 
        '''
        self.driver.switch_to.frame(frame_id)

    def switch_to_window_open(self):
        '''
        跳进新句柄
        :return: 
        '''
        handles = self.driver.window_handles
        if len(handles) < 2:
            return False
        else:
            self.driver.switch_to_window(handles[len(handles) - 1])
            sleep(1)
            return True

    def switch_to_window_close(self):
        '''
        关闭原句柄跳进新句柄
        :return: 
        '''
        try:
            sleep(1)
            handles = self.driver.window_handles
            if len(handles) < 2:
                return False
            else:
                self.driver.close()
                self.driver.switch_to_window(handles[len(handles) - 1])
                sleep(1)
                return True
        except Exception as ES:
            return False

    def get_user_cookies(self, user_name, password):
        '''
        获取帐号cookies
        :param user_name: 
        :param password: 
        :return: 
        '''
        #获取cookie接口
        login_by_passwd_new_request_url = 'https://www.58pic.com/index.php?m=userinfo&a=loginByPasswdNew'

        user_data = {
            'username': user_name,
            'userpass': password
        }
        response = requests.post(url=login_by_passwd_new_request_url, data=user_data)
        # print(response.cookies)
        user_cookie = response.cookies.get('auth_id')
        user_uid = str(user_cookie).replace('%22', '').split('%')[0]
        user_referer = response.cookies.get('referer')

        return user_cookie, user_uid, user_referer

    def add_cookies(self, user_cookie, user_id, user_referer):
        '''
        添加用户cookie
        :param user_cookie: 
        :param user_referer: 
        :param user_id: 
        :param type: 
        :return: 
        '''

        self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
        # 添加localstorage记录
        time_day = time.strftime('%d ', time.localtime(time.time()))
        # self.driver.get('https://www.58pic.com/index.php?m=HelpCenter')
        local_storge_data_JS = [
            'localStorage.setItem("is_show_guide", "1")',
            'localStorage.setItem("activBottom",%s)' % time_day,
            'localStorage.setItem("activRight", %s)' % time_day,
            'localStorage.setItem("time2019618", "1558667818943")'
        ]
        for JS in local_storge_data_JS:
            self.driver.execute_script(JS)

        expiry_time = 15488452170

        now_time = datetime.datetime.now().day
        date = datetime.datetime.now().strftime('%Y%m%d')


        cookies = [
            {'domain': '.58pic.com', 'secure': True,
             'value': 'NDI2ODg1MzF8MTU0MDg5MDE3N3xmYjkwNWE2YzMwNjEyNDMzOGU2ODgyZTkyZjZmNDVhOA%3D%3D', 'httpOnly': True,
             'expiry': expiry_time, 'path': '/', 'name': '_auth_dl_'},
            {'domain': '.58pic.com', 'secure': False,
             'value': user_cookie, 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'auth_id'},
            {'domain': '.58pic.com', 'secure': False,
             'value': '%224ac7049f557063d01fbe2b259aeaac6a%22', 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'qt_visitor_id'},
            {'domain': '.58pic.com', 'secure': False,
             'value': user_referer, 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'referer'},
            {'domain': '.58pic.com', 'secure': False,
             'value': 'patchOne%3A1%2CtimeOne%3A'+str(now_time)+'%2CtimeEnd%3A0', 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'first-charge-'+str(user_id)+'_8'},
            {'domain': '.58pic.com', 'secure': False,
             'value': '1', 'httpOnly': False,
             'expiry': expiry_time, 'path': '/', 'name': 'checkQyActPopup_' + str(date)}
        ]

        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def user_login(self, user_name, password):
        '''
        登录
        :param user_name: 
        :param password: 
        :return: 
        '''
        user_info = self.get_user_cookies(user_name, password)
        # user_info[0]     auth_id 的 cookie值
        # user_info[1]     uid
        # user_info[2]     referer
        if not user_info:
            return False
        self.add_cookies(user_info[0], user_info[1], user_info[2])
        return user_info

    def catch_exception(origin_fun):
        '''
        出错装饰器
        :return: 
        '''
        def wrapper(*args, **kwargs):
            try:
                # print(u'进入装饰器'.encode(encoding='utf-8'))
                print('Enter decorator')
                return origin_fun(*args, **kwargs)
            except Exception as ES:
                # print('出错了'.encode(encoding='utf-8'))
                print(ES)
                return False
        return wrapper

    def change_user_vip_num_times(self, user_id, downloaded_times, vip_type='all'):
        '''
        修改用户vip剩余次数
        :param user_id: 用户id
        :param downloaded_times: 已下载的次数 
        :param vip_type: VIP类型  all——所有，yc——精选，sc——基础，bg——办公 ，qy499——主站企业499
        :return: 
        '''
        # 请求方法
        request_url = 'http://cron.58pic.com/index.php?c=QATools&a=setTodayDownloadNum&' + \
                      'uid=' + str(user_id) + '&' + \
                      'num=' + str(downloaded_times) + '&' + \
                      'type=' + str(vip_type)

        # 头部
        header = {
            'Authorization': 'Basic UUFUb29scy41OHBpYy5jb206NXIlI2xxWXAybFFU'
        }
        # 请求
        f = requests.get(request_url, headers=header).json()
        print(f)



if __name__ == '__main__':

    C = CommonFunction('brower')
    C.change_user_vip_num_times('63231380', '0', vip_type='sc')
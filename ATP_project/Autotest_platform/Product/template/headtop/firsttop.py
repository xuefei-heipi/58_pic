from Product.common.commonfun import CommonFunction
from Product.common.driver import browser
import time


class DLAutomatedTest(CommonFunction):

    @CommonFunction.catch_exception
    def drop_home_classification(self, num, num1):
        '''
        测试分类菜单一级菜单
        :param num: 分类下第几行   1:平面广告/电商淘宝 2:元素/背景/艺术字 3:插画/新媒体用图 4:PPT模板/Word模板 5:摄影图库/视频音频 6:装饰专修/3D模型 7:简历模板/Excel模板 8:GIF动图/卡通形象 9:字库/网页UI
        :param num1: 分类下某一行的第几个   如：第一行:平面广告/电商淘宝 下第一个 1:平面广告  第二个 2:电商淘宝   
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        # 悬浮到分类
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-main clearfix"]/div[1]')
        time.sleep(0.5)
        #定位到分类下菜单中的分类词
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-main clearfix"]/div[1]/div/dl/dd['+str(num)+']/div[1]/a[@stats-point="559:'+str(num)+'-'+str(num1)+'"]')
        name = elem.text
        print(name)
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title or '千图网'in self.driver.title:
            return True
        else:
            return False


    @CommonFunction.catch_exception
    def drop_home_classification_menu(self, num, num2, num3):
        '''
        测试公共分类菜单下三级菜单
        :param num: 分类下一级菜单第几行   1:平面广告/电商淘宝 2:元素/背景/艺术字 3:插画/新媒体用图 4:PPT模板/Word模板 5:摄影图库/视频音频 6:装饰专修/3D模型 7:简历模板/Excel模板 8:GIF动图/卡通形象 9:字库/网页UI       
        :param num2: 二级菜单 第几个  如：平面广告/电商淘宝 1:平面广告 2:电商淘宝     特例：元素/背景/艺术字   1:艺术字  2:元素  3:背景
        :param num3: 三级菜单 第几个  如：平面广告  1:节日海报 2:商业海报 3:促销海报 4:美食海报 5:招聘海报 ......
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #悬浮到分类
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[1]')
        time.sleep(0.5)
        #悬浮到分类菜单下一级菜单栏上
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[1]/div/dl/dd[' + str(num) + ']'
        )
        time.sleep(0.5)
        #定位到需要测试的三级菜单词分类词上
        elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
                '/div[@class="search-main clearfix"]/div[1]/div/dl/dd[' + str(num) + ']'
                '/div[@class="list-sec"]/div[' + str(num2) + ']/div/a[' + str(num3) + ']'
        )
        name = elem.text
        print(name)
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄

        if name in self.driver.title or '千图网' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_search_outside(self, num):
        '''
        测试公共搜索框外下面搜索词
        :param num: 对应的第几个搜索词 
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #定位搜索框外搜索词
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-hot"]/a['+str(num)+']'
        )
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title or '千图网' in self.driver.title:
            return True
        else:
            return False


    @CommonFunction.catch_exception
    def drop_home_within_search(self, num):
        '''
        测试公共搜索框内的搜索词
        :param num: 第几个搜索词
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #点击收搜框
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[@class="search-input"]/div[1]'
        ).click()
        time.sleep(1)
        #定位搜索框内搜索词
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[@class="search-input"]/div[2]/div/dl['+str(num)+']/dd[1]'
        )
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title or '千图网' in self.driver.title:
            return  True
        else:
            return False


    @CommonFunction.catch_exception
    def drop_home_upload(self):
        '''
        测试公共上传作品按钮
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #定位上传作品
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]/div[5]/a'
        )
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False


    @CommonFunction.catch_exception
    def drop_home_personal_vip(self):
        '''
        测试公共个人vip
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #定位个人vip
        elem = self.driver.find_element_by_xpath(
            '//*[@id="user-vip-header"]/div[1]'
            )
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_personalvip_suspension(self, num=None, num1=None):
        '''
        测试公共个人vip浮窗
        :param num:   199全站年vip：None    精选、基础：1  办公、字库：3
        :param num1:   精选：1  基础：2    办公：1  字卡：2
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #悬浮到个人vip
        self.mouse_above('//*[@id="user-vip-header"]/div[1]')
        # time.sleep(10)
        if num == None and num1 == None:
            #定位199全站年vip
            elem = self.driver.find_element_by_xpath(
                '//*[@id="user-vip-header"]/div[2]/a/div'
            )
        else:
            #定位vip查看特权按钮
            elem = self.driver.find_element_by_xpath(
                '//*[@id="user-vip-header"]/div[2]/div['+str(num)+']/div['+str(num1)+']/div/a'
            )
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_company_vip(self, num=None):
        '''
        测试公共企业vip
        :param num: 1：给公司用，正版作品  2：给公司用，正版字体  3：给客户用  4：给集团和子公司用
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #悬浮到企业vip上
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]'
            '/div[@class="head-vip header-right fr"]/a/em'
        )
        time.sleep(0.5)
        if num == None:
            #定位企业vip
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]'
                '/div[@class="head-vip header-right fr"]/a/em'
            )
        else:
            #定位企业vip下来框中对应标签
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]'
                '/div[@class="head-vip header-right fr"]/div/ul/li['+str(num)+']/a/div'
            )

        elem.click()
        self.switch_to_window_close() # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_message(self):
        '''
        测试消息
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #悬浮到消息上
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div[@class="header-row clearBoth"]'
            '/div[@class="header-row-login"]/div[@class="messageSystem header-right"]/ul'
        )
        #定位全部信息
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div[@class="header-row clearBoth"]'
            '/div[@class="header-row-login"]/div[@class="messageSystem header-right"]/span/span/li'
            '/a[@class="messageSystem-btn2"]'
        )
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_head_portrait(self, num=None, num1=None, num2=None):
        '''
        测试头像下拉框
        num、num1、num2为空时定位点击的是头像
        :param num: num=1：精选、基础、办公、字库 vip栏   num=2：作品、个人主页、收藏、主题领取 个人资料栏
        :param num1: vip栏：1 精选 2 基础 3 办公 4 字库    个人资料栏：1作品管理 2个人主页  3我的收藏 4主题领取
        :param num2: num2=2 企业vip栏
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        #悬浮到头像上
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div[@class="header-row clearBoth"]/'
            'div[@class="header-row-login"]/div[@class="header-user info header-right fr"]/'
            'div[@class="user-box"]/div[@class="user-img"]/a')
        time.sleep(1)
        if num != None and num1 != None:
            #定位下来框中个vip、作品管理、个人主页、收藏、主题领取
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/'
                'div/div[@class="header-row-login"]/div[@class="header-user info header-right fr"]/'
                'div[@class="header-drop"]/div[@class="user-info-row"]/ul['+str(num)+']/li['+str(num1)+']/a'#/p[1]/span'
            )
        elif num2 == 2:
            #定位企业主页
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]/'
                'div[@class="header-user info header-right fr"]/div[@class="header-drop"]/div[@class="user-info-row"]/'
                'div['+str(num2)+']/div[@class="company-row"]/a'
            )
        else:
            # 定位头像
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div[@class="header-row clearBoth"]/'
                'div[@class="header-row-login"]/div[@class="header-user info header-right fr"]/'
                'div[@class="user-box"]/div[@class="user-img"]/a'
            )

        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False


    @CommonFunction.catch_exception
    def drop_home_sidebar_collar_vip(self, num=None):
        '''
        测试侧边栏免费领取vip
        :param num: num=None：走去兑换  num=1：去分享  num=2：去下载  num=3：去领取
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="tally"]/a[1]'
        ).click()
        time.sleep(1)
        if num != None:
            #定位领vip页中去分享、去下载、去领取按钮，并点击跳转
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="inlet"]/div/div/div[@class="inletModel vip-lingqu"]/div[@class="vip-lingqu-main"]/'
                'div['+str(num)+']/a/div[@class="title"]/div'
            ).click()

        else:
            #定位领vip页去兑换按钮并点击跳转
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="inlet"]/div/div/div[@class="inletModel vip-lingqu"]/'
                'div[@class="vip-lingqu-head"]/a/div'
            ).click()

        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        #定位获取页面头部中千图网logo
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')
        if '千图网' in name:
            return True
        return False


    @CommonFunction.catch_exception
    def drop_home_sidebar_check_in(self, num):
        '''
        测试悬浮到签到上点击积分商城和积分
        :param num: 1：积分   2：积分商城
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        # 悬浮到侧边栏签到上
        self.mouse_above(
            '/html/body/div[@class="tally"]/a[@stats-point="512"]'
        )
        #点击积分商城、积分
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="tally"]/ul[@class="tally-ul1"]/a['+str(num)+']'
        ).click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        # 获取页面头部logo 千图网
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')

        if '千图网' in name:
            return True
        return False



    @CommonFunction.catch_exception
    def drop_home_sidebar_daily_activities(self, num=None, num1=None):
        '''
        测试日常活动栏
        num = None  num1 = None 是每日签到栏
        :param num: 2：设计大赛  3：积分活动
        :param num1: 1：设计大赛中第一个  2：设计大赛中第二个
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #悬浮到侧边栏签到上
        self.mouse_above(
            '/html/body/div[@class="tally"]/a[@stats-point="512"]'
        )
        #点击侧边栏签到按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="tally"]/a[@stats-point="512"]'
        ).click()
        time.sleep(1)
        if num == 2:
            #点击设计大赛
            self.driver.find_element_by_xpath(
                '//*[@id="richang"]/ul[@class="inletBtn"]/a['+str(num)+']'
            ).click()
            #点击大赛里的活动
            self.driver.find_element_by_xpath(
                '//*[@id="rw"]/li['+str(num1)+']'
            ).click()
            self.switch_to_window_close()  # 跳入新句柄关闭原句柄
            #获取页面头部logo 千图网
            name = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-header "]/div/a'
            ).get_attribute('title')
            print(name)

        elif num == 3:
            #点击积分活动
            self.driver.find_element_by_xpath(
                '//*[@id="richang"]/ul[@class="inletBtn"]/a['+str(num)+']'
            ).click()
            #点击活动
            self.driver.find_element_by_xpath(
                '//*[@id="zt"]/li'
            ).click()
            self.switch_to_window_close()  # 跳入新句柄关闭原句柄
            # 获取页面头部logo 千图网
            name = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-header "]/div/a'
            ).get_attribute('title')
            print(name)

        else:
            #获取签到页面名字
            elem = self.driver.find_element_by_xpath(
                 '//*[@id="qd"]/div/ul[@class="signInTitle"]/span'
            )
            name = elem.text
            print(name)
        if '签到' in name or '千图网' in name:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_theme_activity(self, num, num1=None):
        '''
         测试侧边栏弹窗主题活动页
        :param num: 1：创意教程  2：设计师招募
        :param num1: 第几个banner 
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        #悬浮到侧边栏签到上
        self.mouse_above(
            '/html/body/div[@class="tally"]/a[@stats-point="512"]'
        )
        #点击侧边栏签到按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="tally"]/a[@stats-point="512"]'
        ).click()
        time.sleep(1)
        #点击弹窗中主题活动
        self.driver.find_element_by_xpath(
            '//*[@id="nav-zhuti"]'
        ).click()
        #点击主题活动中的页签   1：创意教程  2：设计师招募
        self.driver.find_element_by_xpath(
            '//*[@id="zhuti"]/ul[@class="inletBtn"]/a['+str(num)+']'
        ).click()
        if num == 1:
            #点击第一栏创意教程 第一个banner
            self.driver.find_element_by_xpath(
             '//*[@id="zhuti"]/ul[@class="inletCon"]/li/a'
            ).click()

        else:
            #点击第二栏设计师招募 第num2个banner
            self.driver.find_element_by_xpath(
             '//*[@id="zhuti"]/ul[3]/li['+str(num1)+']/a'
            ).click()
        # 跳入新句柄关闭原句柄
        self.switch_to_window_close()
        # 获取页面头部logo 千图网
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')
        if '千图网' in name:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_sidebar_customer_service(self, num=None):
        '''
        测试侧边栏客服悬浮框
        :param num: 1：点击联系客服按钮      None：点击常见问题
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #悬浮到赚钱上
        self.mouse_above('/html/body/div[@class="tally"]/a[@class="tally-a3"]/i')
        # 悬浮到客服上
        self.mouse_above('/html/body/div[@class="tally"]/a[@class="tally-a2"]/i')
        if num == 1:
            #点击联系客服
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="tally"]/ul[@class="tally-ul2"]/p/a'
            ).click()
            # 跳入新句柄关闭原句柄
            self.switch_to_window_close()

        else:
            #点击常见问题
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="tally"]/ul[@class="tally-ul2"]/li/a'
            ).click()
            # 跳入新句柄关闭原句柄
            self.switch_to_window_close()
            # 获取页面头部logo 千图网
            name = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-header "]/div/a'
            ).get_attribute('title')
        if '客服热线' in self.driver.title or '千图网'in name:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_sidebar_make_money(self, num=None):
        '''
        测试侧边栏赚钱
        :param num: 1：点击赚钱按钮   None：点击点我赚钱按钮
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        #悬浮到赚钱上
        self.mouse_above('/html/body/div[@class="tally"]/a[@class="tally-a3"]/i')
        if num == 1:
            #点击赚钱
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="tally"]/a[@class="tally-a3"]/i'
            ).click()

        else:
            #点击点我赚钱按钮
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="tally"]/a[@class="tally-a3"]/li/p[2]'
            ).click()
        # 跳入新句柄关闭原句柄
        self.switch_to_window_close()
        # 获取页面头部logo 千图网
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')
        if '千图网'in name:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_feedback(self):
        '''
        测试侧边栏反馈按钮
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        self.mouse_above('/html/body/div[@class="tally"]/a[@class="tally-a4"]/i')
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="tally"]/a[@class="tally-a4"]/i'
        ).click()
        # 跳入新句柄关闭原句柄
        self.switch_to_window_close()
        # 获取页面头部logo 千图网
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')
        if '千图网' in name:
            return True
        return False


    @CommonFunction.catch_exception
    def drop_home_landing(self, user_name, password):
        '''
        测试登陆首页
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url = 'https://www.58pic.com/'
        self.driver.get(url)

        if "千图网" in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_pingmian(self):
        '''
        测试首页banner菜单平面广告
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #定位首页banner菜单平面广告位置
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@class="works-title"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()#跳入新句柄关闭原句柄
        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_dianshangtaobao(self):
        '''
        测试首页banner菜单电商淘宝
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位电商淘宝，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:2"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_shejiyuansu(self):
        '''
        测试首页banner菜单设计元素
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位设计元素，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:3"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_PPTmuban(self):
        '''
        测试首页banner菜单PPT模板
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位PPT模板，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:4"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_chahuahuihua(self):
        '''
        测试首页banner菜单插画绘画
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位插画绘画，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:5"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄

        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_shipingyinxiao(self):
        '''
         测试首页banner菜单视频音效
         :return: 
         '''
        self.driver.get('https://www.58pic.com/')
        # 定位视频音效，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:6"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄

        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_zhuangshizhuangxiu(self):
        '''
        测试首页推荐菜单 装饰装修
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位装饰装修，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:1"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄

        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_sheyingtuku(self):
        '''
        测试首页推荐菜单 摄影图库
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位摄影图库，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:2"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄

        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_wangyeUI(self):
        '''
        测试首页推荐菜单 网页UI
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位网页UI，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:4"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_meitiyongtu(self):
        '''
        测试首页推荐菜单 媒体用图
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #定位媒体用图，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:5"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄

        if name in  self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_GIFdongtu(self):
        '''
        测试首页推荐菜单 GIF动图
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #定位GIF动图，并点击跳转
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:3"]')
        elem.click
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return False
        else:
            return True

    @CommonFunction.catch_exception
    def drop_home_wordmuban(self):
        '''
        测试首页推荐菜单 word模板
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #悬浮到更多
        self.mouse_above('//*[@id="clearBox"]/div[@class="works-box-text fl"]/div[@class="more"]')
        #定位word模板获取名字并点击
        elem = self.driver.find_element_by_xpath('//div[@class="more-element"]/div[@class="more-works"]/a[3]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_teyaoshenqing(self):
        '''
        测试首页固定菜单 特邀申请
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位特邀申请页面位置并点击
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:2"]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return False
        else:
            return True

    @CommonFunction.catch_exception
    def drop_home_jifengshangcheng(self):
        '''
        测试首页固定菜单 积分商城
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位页面位置并点击
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:6"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_huodong(self):
        '''
        测试首页固定菜单 - 活动
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        # 定位活动页面位置并点击
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:4"]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return False
        else:
            return True

    @CommonFunction.catch_exception
    def drop_home_chuangyiqushi(self):
        '''
        测试首页固定菜单 - 创意趋势
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #定位创意趋势页面位置并点击
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:5"]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_qiantugongju(self,num):
        '''
        测试固定菜单 千图工具
        :param num: 1：千图box  2：千图样机  3：设计工具
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        #悬浮到千图工具
        self.mouse_above('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]')
        #定位获取名字并点击进入
        elem = self.driver.find_element_by_xpath(
            '//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]/div[@class="tool-element"]/a['+str(num)+']')
        #elem = self.driver.find_element_by_xpath(
        # '//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]/div[@class="tool-element"]/a[2]')
        #elem = self.driver.find_element_by_xpath(
        #'//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]/div[@class="tool-element"]/a[3]')
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图' in self.driver.title or name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_blog(self):
        '''
        测试首页博客
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #定位点击博客
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[5]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '官方Blog' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_floor_collection(self):
        '''
        测试首页精选收藏夹楼层
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #定位点击精选收藏夹
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-left"]/a')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '收藏夹' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_collection(self,above,num):
        '''
        测试精选收藏夹楼层下的收藏夹
        :param above: 收藏夹楼层下第几个标签  1:千图精选 2:插画风 3:优秀设计师 4:热门趋势
        :param num: 标签页下第个收藏夹
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)

        self.driver_execute_script02(300)  #鼠标向下移动300像素

        #悬浮到收藏夹楼层页签上
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above)+']')
        time.sleep(0.5)
        #点击收藏夹
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above)+']/div[@class="clearfix selected-topic w1200"]/div['+str(num)+']/a')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '收藏夹' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_collection_recommend(self,above):
        '''
        测试精选收藏夹楼层查看全部推荐
        :param above: 收藏夹楼层下第几个页签  1:千图精选 2:插画风 3:优秀设计师 4:热门趋势
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        # self.find_element_by_Js('/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-left"]/a')
        #悬浮到收藏夹楼层页签上
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above)+']')
        #点击查看全部推荐
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/a[@class="modelNav-leftLink"]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '收藏夹' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_designer(self,above,num):
        '''
        测试明星设计师推荐下的设计师卡片
        :param above: 页签  1:千图精选 2:特邀设计师 3:设计达人
        :param num: 当前页签下第几个设计师卡片  1至5
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #悬浮到页签
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/li[@class="modelNav-leftTxt start-active"]/a['+str(above)+']')
        time.sleep(0.5)
        #获取卡片中设计师名称
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-model"]/p[@class="introduce-title"]/a/span')
        name = elem.text
        elem.click()
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_designer_change(self,above,num):
        '''
        测试明星设计师推荐-换一批按钮
        :param above: 页签  1:千图精选 2:特邀设计师 3:设计达人
        :param num: 当前页签下第几个设计师卡片  1至5
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #悬浮点位到页签
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/li[@class="modelNav-leftTxt start-active"]/a['+str(above)+']')
        time.sleep(1)
        #获取卡片名字
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-model"]/p[@class="introduce-title"]/a/span'
        ).text
        print(name)
        #点击换一批按钮
        self.driver.find_element_by_xpath('/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/div').click()
        time.sleep(1)
        #获取最新卡片名字
        name2 = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-model"]/p[@class="introduce-title"]/a/span'
        ).text
        print(name2)
        if name != name2:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_designer_attention(self,above,num):
        '''
        测试明星设计师推荐-卡片关注
        :param above: 页签  1:千图精选 2:特邀设计师 3:设计达人
        :param num: 当前页签下第几个设计师卡片  1至5
        :return: 
        '''
        self.new_window_open()  #新开页面
        time.sleep(1)
        #悬浮定位到标签
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/li[@class="modelNav-leftTxt start-active"]/a['+str(above)+']')
        time.sleep(0.5)
        #悬浮到卡片关注
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]')
        #获取当前关注状态
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]/span'
        )
        name = elem.text
        print(name)
        elem.click()
        time.sleep(0.5)
        #悬浮到卡片关注
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]')
        #获取点击后卡片的关注状态
        name2 = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]/span'
        ).text
        print(name2)
        if name != name2:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_floorname(self,num):
        '''
        1:第一个楼层名称 
        2:第二个楼层名称 
        3:第三个楼层名称 
        4:第四个楼层名称 
        5:第五个楼层名称 
        6:第六个楼层名称
        :param num: 偏好楼层名称坑位
        :return: 
        '''
        self.new_window_open()  # 新开页面
        #self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(2)
        #定位楼层
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/li[@class="modelNav-left"]/a')
        name = elem.text
        print(name)
        elem.click()
        self.switch_to_window_close()# 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_floor_change(self,num):
        '''
        测试楼层换一批按钮   如：1：平面广告  2：电商淘宝  3：设计元素  4：PPT模板 ...
        :param num: 楼层换一批按钮坑位  1:第一个楼层换一批 2:第二个楼层换一批 3:第三个楼层换一批 4:第四个楼层换一批 ...
        :return: 
        '''

        self.new_window_open()  # 新开页面
        time.sleep(1)

        self.driver_execute_script02(300)  #鼠标向下移动300像素

        time.sleep(0.5)
        #获取千图精选下第一个卡片名字
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(num)+']/div[2]/div[1]/p[@class="card-title"]').text
        #点击换一批按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/div[@class="modelChange nextChange"]').click()
        time.sleep(1)
        #获取刷新后，千图精选下第一个卡片名字
        name2 = self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(num)+']/div[2]/div[1]/p[@class="card-title"]').text
        if name != name2:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_floor_card(self,above1,above2,num1):
        '''
        测试楼层卡片
        :param above1: 楼层  1:平面广告 2:电商淘宝 3:设计元素 4:插画绘画 ...
        :param above2: 在该楼层下第几个标签  1:千图精选 2:促销海报 3:商务名片 4:企业画册 5:化妆品包装
        :param num1: 所在楼层第几个标签下第几张卡片
        :return: 
        '''

        # self.driver.get('https://www.58pic.com')
        # time.sleep(1)
        self.new_window_open()  # 新开页面

        time.sleep(1)
        #获取卡片名称
        div = self.driver.find_element_by_xpath(
           '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-left"]/a'
        ).text
        print(div)
        time.sleep(0.5)

        if div == '视频音频':
            #鼠标悬浮到视频音频楼层
            self.mouse_above(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']'
            )
            time.sleep(0.2)
            #获取卡片名称
            name = self.driver.find_element_by_xpath(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div['+str(above2+1)+']/div[1]/div['+str(num1)+']/p[@class="card-title"]'
            ).text
            print(name)
            #点击卡片
            time.sleep(0.2)
            self.driver.find_element_by_xpath('//*[@class="ficheModel ficheModel-6-'+str(above2-1)+' masonry"]/div/div['+str(num1)+']/div').click()

        else:
            #定位楼层
            self.mouse_above(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']')
            time.sleep(0.5)
            #获取卡片名称
            name = self.driver.find_element_by_xpath(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div['+str(above2+1)+']/div['+str(num1)+']/p[@class="card-title"] '
            ).text
            print(name)
            #点击卡片
            self.driver.find_element_by_xpath(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div['+str(above2+1)+']/div['+str(num1)+']/div[@class="card-img"]/a'
            ).click()

        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(0.5)
        if name in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_home_floor_recommend(self,above1,above2):
        '''
        测试楼层查看全部推荐
        :param above1: 楼层  1:平面广告 2:电商淘宝 3:设计元素 4:插画绘画 ...
        :param above2: 在该楼层下第几个标签  2:促销海报 3:商务名片 4:企业画册 5:化妆品包装
        :return: 
        '''
        self.new_window_open()  # 新开页面
        time.sleep(1)
        #定位楼层
        self.mouse_above('/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']')
        time.sleep(0.5)

        self.driver_execute_script02(300)  #滚动条位置向下移动300像素

        #获取标签
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']'
        ).text
        print(name)
        time.sleep(1)
        #点击查看全部推荐按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/a[@class="modelNav-leftLink"]'
        ).click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        return False




if __name__ == '__main__':
    driver = browser()
    f = DLAutomatedTest(driver)
    print(f.drop_home_landing('ogcugctest28', '123456'))
    # print(f.drop_home_landing('cstest12', '123456'))
    # print(f.drop_message())
    num = None
    num1= None
    num2=2
    print(f.drop_head_portrait(num, num1,num2))
    # num = 1
    # print(f.drop_home_theme_activity(num))
    # num = 3
    # print(f.drop_home_sidebar_collar_vip(num))
    # num = 3
    # num1 = 1
    # print(f.drop_home_sidebar_check_in(num,num1))
    # num = 3
    # print(f.drop_home_sidebar_daily_activities(num,))
    # num = 1
    # print(f.drop_home_sidebar_customer_service(num))

    # print(f.drop_home_sidebar_make_money())
    # num = 1
    # print(f.drop_home_sidebar_make_money(num))
    # print(f.drop_home_jifengshangcheng())

    # above1 = 5
    # above2 = 3
    # num1 = 1
    # print(f.drop_home_floor_card(above1,above2,num1))

    # above = 2
    # num = 1
    # print(f.drop_home_designer_change(above,num))

    # num = 2
    # print(f.drop_home_floor_change( num))

    # num = 3
    # print(f.drop_home_floorname(num))
    # above1 = 1
    # above2 = 2
    # print(f.drop_home_floor_recommend(above1,above2))

    # above1 = 1
    # above2 = 3
    # print(f.drop_home_floor_recommend(above1,above2))
    # above1 = 1
    # above2 = 4
    # print(f.drop_home_floor_recommend(above1,above2))
    # above = 3
    # print(f.drop_home_collection_recommend(above))
    # above = 2
    # num = 5
    # print(f.drop_home_designer(above,num))
    # above = 3
    # num = 4
    # print(f.drop_home__designer_attention(above,num))
    # above = 1
    # num = 1
    # print(f.drop_home__designer_change(above,num))

    # num = 9
    # num2 = 2
    # num3 = 2
    # print(f.drop_classification_menu( num, num2, num3))
    # num = 8
    # num1 = 1
    # print(f.drop_classification( num, num1))

    # num = 1
    # print(f.drop_search_outside(num))
    # num = 10
    # print(f.drop_within_search(num))

    # print(f.drop_home_personalvip())
    # print(f.drop_home_personalvip_suspension())
    # num = 1
    # num1 = 1
    # print(f.drop_home_personalvip_suspension(num , num1))
    # num = 1
    # num1 = 2
    # print(f.drop_home_personalvip_suspension(num, num1))
    # num = 3
    # num1 = 1
    # print(f.drop_home_personalvip_suspension(num, num1))
    # num = 3
    # num1 = 2
    # print(f.drop_home_personalvip_suspension(num, num1))

    # print(f.drop_companyvip())
    # num = 1
    # print(f.drop_companyvip(num))

    print(f.drop_home_message())
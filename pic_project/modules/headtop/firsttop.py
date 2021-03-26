from pic_project.common.commonfun import CommonFunction
from pic_project.common.driver import browser
import time




class DLAutomatedTest(CommonFunction):

    @CommonFunction.catch_exception
    def drop_classification(self, num, num1):
        '''
        测试分类菜单一级菜单
        :param num: 分类下第几行   1:平面广告/电商淘宝 2:元素/背景/艺术字 3:插画/新媒体用图 4:PPT模板/Word模板 5:摄影图库/视频音频 6:装饰专修/3D模型 7:简历模板/Excel模板 8:GIF动图/卡通形象 9:字库/网页UI
        :param num1: 分类下某一行的第几个   如：第一行:平面广告/电商淘宝 下第一个 1:平面广告  第二个 2:电商淘宝   
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #鼠标悬浮再分类上
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[1]')

        time.sleep(0.5)
        #获取元素的位置，
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[1]/div/dl/dd['+str(num)+']/div[1]'
            '/a[@stats-point="559:'+str(num)+'-'+str(num1)+'"]')
        #需要点击的元素'文字'
        name = elem.text
        # print(name)
        elem.click()

        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title or '千图网'in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def drop_classification_menu(self, num, num2, num3):
        '''
        测试公共分类菜单下三级菜单
        :param num: 分类下一级菜单第几行   1:平面广告/电商淘宝 2:元素/背景/艺术字 3:插画/新媒体用图 4:PPT模板/Word模板 5:摄影图库/视频音频 6:装饰专修/3D模型 7:简历模板/Excel模板 8:GIF动图/卡通形象 9:字库/网页UI       
        :param num2: 二级菜单 第几个  如：平面广告/电商淘宝 1:平面广告 2:电商淘宝     特例：元素/背景/艺术字   1:艺术字  2:元素  3:背景
        :param num3: 三级菜单 第几个  如：平面广告  1:节日海报 2:商业海报 3:促销海报 4:美食海报 5:招聘海报 ......
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[1]')
        time.sleep(0.5)
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
            '/div[@class="search-main clearfix"]/div[1]/div/dl/dd[' + str(num) + ']')  # /div[1]/a[@stats-point="559:'+str(num)+'-'+str(num1)+'"]')
        time.sleep(0.5)
        elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]'
                '/div[@class="search-main clearfix"]/div[1]/div/dl/dd[' + str(num) + ']'
                '/div[@class="list-sec"]/div[' + str(num2) + ']/div/a[' + str(num3) + ']')
        name = elem.text
        print(name)
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(0.5)
        try:
            name2 = self.driver.find_element_by_xpath(
                    '/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em[3]').text
            print(name2)
        except :
            pass

        if name in self.driver.title or '千图网' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_search_outside(self, num):
        '''
        测试公共搜索框外下面搜索词
        :param num: 对应的第几个搜索词 
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-hot"]/a['+str(num)+']'
        )
        name = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title or '千图网' in self.driver.title:
            return True
        else:
            return False


    @CommonFunction.catch_exception
    def drop_within_search(self, num):
        '''
        测试公共搜索框内的搜索词
        :param num: 第几个搜索词
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-main clearfix"]/div[@class="search-input"]/div[1]'
        ).click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-main clearfix"]/div[@class="search-input"]/div[2]/div/dl['+str(num)+']/dd[1]'
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
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]/div[5]/a'
        )
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        else:
            return False


    @CommonFunction.catch_exception
    def drop_home_personalvip(self):
        '''
        测试公共个人vip
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
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
        :param num: 199全站年vip：None  精选、基础：1  办公、字库：3
        :param num1: 精选：1  基础：2    办公：1  字卡：2
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        self.mouse_above('//*[@id="user-vip-header"]/div[1]')
        # time.sleep(10)
        print(111)
        if num == None and num1 == None:
            elem = self.driver.find_element_by_xpath(
                '//*[@id="user-vip-header"]/div[2]/a/div'
            )
        else:
            elem = self.driver.find_element_by_xpath(
                '//*[@id="user-vip-header"]/div[2]/div['+str(num)+']/div['+str(num1)+']/div/a'
            )
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_companyvip(self, num=None):
        '''
        测试公共企业vip
        :param num: 
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        self.mouse_above(
            '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]/div[@class="head-vip header-right fr"]/a/em'
        )
        time.sleep(0.5)
        if num == None:
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]/div[@class="head-vip header-right fr"]/a/em'
            )
        else:
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-login"]/div[@class="head-vip header-right fr"]/div/ul/li['+str(num)+']/a/div'
            )

        elem.click()
        self.switch_to_window_close() # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        else:
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
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_pingmian(self):
        '''
        测试首页banner菜单平面广告
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        #定位首页banner菜单平面广告位置
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@class="works-title"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()#跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:2"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:3"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:4"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:5"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@stats-point="560:6"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:1"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:2"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:4"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:5"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-text fl"]/a[@stats-point="562:3"]')
        elem.click
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '404' in self.driver.title:
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
        self.mouse_above('//*[@id="clearBox"]/div[@class="works-box-text fl"]/div[@class="more"]')
        elem = self.driver.find_element_by_xpath('//div[@class="more-element"]/div[@class="more-works"]/a[3]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="adstyle-bgcolor"]/div[@class="classifyBanner"]/div[@class="classifyBanner-title"]/em').text
        if title in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:2"]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '404' in self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:6"]')
        tilte = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath('/html/body/div[@class="qt-header "]/div/em/a').text
        if tilte in title2 and self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:4"]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '404' in self.driver.title:
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
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/a[@stats-point="451:5"]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if title in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_honme_qiantugongju_qiantubox(self):
        '''
        测试首页固定菜单 千图工具—千图box
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        self.mouse_above('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]')
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]/div[@class="tool-element"]/a[1]')
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图box' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_qiantugongju_qiantuyangji(self):
        '''
        测试首页千图工具-千图样机
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        self.mouse_above('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]')
        #//*[@id="clearBox"]/div[2]/div/div/a[2]
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]/div[@class="tool-element"]/a[2]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if title in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_qiantugongju_shejigongju(self):
        '''
        测试首页千图工具- 设计工具
        :return: 
        '''
        self.driver.get('https://www.58pic.com/')
        self.mouse_above('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]')
        elem = self.driver.find_element_by_xpath('//*[@id="clearBox"]/div[@class="works-box-back fl"]/div[@class="tool"]/div[@class="tool-element"]/a[3]')
        title = elem.text
        elem.click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if title in self.driver.title:
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
        self.find_element_by_Js('/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-left"]/a')
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above)+']')
        time.sleep(0.5)
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
        :param above: 收藏夹楼层下第几个标签  1:千图精选 2:插画风 3:优秀设计师 4:热门趋势
        :return: 
        '''

        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        self.find_element_by_Js('/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-left"]/a')
        self.mouse_above('/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above)+']')
        #/html/body/div[7]/ul/a
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="modelMain modelPos slideModel"]/ul[@class="modelNav"]/a[@class="modelNav-leftLink"]')
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
        #self.find_element_by_Js('/html/body/div[9]/div[1]/li[2]/a')
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/li[@class="modelNav-leftTxt start-active"]/a['+str(above)+']')
        time.sleep(0.5)
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
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/li[@class="modelNav-leftTxt start-active"]/a['+str(above)+']')
        time.sleep(1)
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-model"]/p[@class="introduce-title"]/a/span'
        ).text
        print(name)
        self.driver.find_element_by_xpath('/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/div').click()
        time.sleep(1)
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
        self.driver.get('https://www.58pic.com/')
        time.sleep(1)
        #self.find_element_by_Js('/html/body/div[9]/div[1]/li[2]/a')
        self.mouse_above(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div[@class="modelNav"]/li[@class="modelNav-leftTxt start-active"]/a['+str(above)+']')
        time.sleep(0.5)
        self.mouse_above('/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]')
        elem = self.driver.find_element_by_xpath(
            '/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]/span'
        )
        name = elem.text
        print(name)
        elem.click()
        time.sleep(0.5)
        self.mouse_above('/html/body/div[@class="modelMain modelPos slideModel"]/div['+str(above+1)+']/div['+str(num)+']/li[@class="introduce-num"]')
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
        self.open_new_window()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/li[@class="modelNav-left"]/a')
        #self.find_element_by_Js('/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/li[@class="modelNav-left"]/a')
        js2 = 'var location=document.documentElement.scrollTop;' \
              'var b=document.documentElement.scrollTop=(location+100)'
        self.driver.execute_script(js2)

        title = elem.text
        print(title)
        elem.click()
        self.switch_to_window_close()# 跳入新句柄关闭原句柄
        if title in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_floor_change(self,num):
        '''
        测试楼层换一批按钮   如：1：平面广告  2：电商淘宝  3：设计元素  4：PPT模板 ...
        :param num: 楼层换一批按钮坑位  1:第一个楼层换一批 2:第二个楼层换一批 3:第三个楼层换一批 4:第四个楼层换一批 ...
        :return: 
        '''

        self.open_new_window()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(1)
        #self.mouse_above('/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a[1]')
        #self.find_element_by_Js('/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a[1]')
        self.driver_execute_script02()
        time.sleep(0.5)
        name = self.driver.find_element_by_xpath('/html/body/div[@class="index-main"]/div['+str(num)+']/div[2]/div[1]/p[@class="card-title"]').text
        self.driver.find_element_by_xpath('/html/body/div[@class="index-main"]/div['+str(num)+']/div[@class="modelNav"]/div[@class="modelChange nextChange"]').click()
        time.sleep(1)
        name2 = self.driver.find_element_by_xpath('/html/body/div[@class="index-main"]/div['+str(num)+']/div[2]/div[1]/p[@class="card-title"]').text
        if name != name2:
            return True
        else:
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
        self.open_new_window()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(1)
        #获取卡片名称
        div = self.driver.find_element_by_xpath(
           '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-left"]/a'
        ).text
        print(div)
        time.sleep(0.5)

        if div == '视频音频':
            self.mouse_above(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']'
            )
            time.sleep(0.2)
            #self.find_element_by_Js('/html/body/div[10]/div[6]/div[1]/li[2]/a')
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div['+str(above2+1)+']/div[1]/div['+str(num1)+']/p[@class="card-title"]'
            ).text
            print(elem)
            #self.find_element_by_Js('/html/body/div[10]/div[6]/div[1]/li[2]/a')
            time.sleep(0.2)
            self.driver.find_element_by_xpath('//*[@class="ficheModel ficheModel-6-'+str(above2-1)+' masonry"]/div/div['+str(num1)+']/div').click()

        else:
            self.mouse_above(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']')
            time.sleep(0.5)
            elem = self.driver.find_element_by_xpath(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div['+str(above2+1)+']/div['+str(num1)+']/p[@class="card-title"] '
            ).text
            print(elem)

            self.driver.find_element_by_xpath(
                '/html/body/div[@class="index-main"]/div['+str(above1)+']/div['+str(above2+1)+']/div['+str(num1)+']/div[@class="card-img"]/a'
            ).click()

        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(0.5)
        if elem in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_floor_recommend(self,above1,above2):
        '''
        测试楼层查看全部推荐
        :param above1: 楼层  1:平面广告 2:电商淘宝 3:设计元素 4:插画绘画 ...
        :param above2: 在该楼层下第几个标签  2:促销海报 3:商务名片 4:企业画册 5:化妆品包装
        :return: 
        '''
        # self.driver.get('https://www.58pic.com/')
        # time.sleep(1)
        # js = "window.open('https://www.58pic.com/')"
        # self.driver.execute_script(js)
        # time.sleep(1)
        self.open_new_window()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(1)
        #定位楼层标签
        self.mouse_above('/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']')
        time.sleep(0.5)
        self.driver_execute_script02()
        #time.sleep(0.5)
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/li[@class="modelNav-leftTxt"]/a['+str(above2)+']'
        ).text
        print(name)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[@class="index-main"]/div['+str(above1)+']/div[@class="modelNav"]/a[@class="modelNav-leftLink"]'
        ).click()
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if name in self.driver.title:
            return True
        else:
            return False




if __name__ == '__main__':
    driver = browser()
    f = DLAutomatedTest(driver)
    print(f.drop_home_landing('cstest12', '123456'))
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

    print(f.drop_companyvip())
    num = 1
    print(f.drop_companyvip(num))
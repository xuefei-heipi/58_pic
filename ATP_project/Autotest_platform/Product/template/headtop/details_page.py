from Product.common.commonfun import CommonFunction
from Product.common.driver import browser

from browsermobproxy import Server

import re
import time

public_positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                     'div[@class="material-info material-copyright clearfix"]/'
public_positioning1 ='/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/'

class DLAutomatedTest(CommonFunction):
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
    def details_current_position(self, id, num):
        '''
        测试当前位置
        :param id: 
        :param num: 1：首页  2：一级分类  3：二级分类  4：三级分类
        :return: 
        '''


        position = '/html/body/div[8]/div[@class="showDetail-header"]/div/div/' \
                   'div[@class="bread-crumbs"]/a['+str(num)+']'

        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/'+str(id)+'.html')
        self.driver.find_element_by_xpath(position).click()
        # 获取页面头部logo 千图网
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')
        if '千图网'in name:
            return True
        return False


    @CommonFunction.catch_exception
    def details_commercial_standard(self, id, num=None):
        '''
        测试详情页查看商标授权
        :param id: 素材uid
        :param num: 1：直接点击商标跳转  None：点击悬浮框上获取按钮
        :return: 
        '''
        position = '/html/body/div[8]/div[@class="showDetail-header"]/div/div/' \
                   'div[@class="detail-title fl"]/div[@class="pic-business fl"]/a'
        position1 = '/html/body/div[8]/div[@class="showDetail-header"]/div/div/' \
                    'div[@class="detail-title fl"]/div[@class="pic-business fl"]/span/a'
        head_position = '/html/body/div[@class="qt-header "]/div/a'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/'+str(id)+'.html')
        try:
            self.mouse_above(position) #移动到商用标上
            if num == 1:
                self.driver.find_element_by_xpath(position).click()#点击商用标
            else:
                self.driver.find_element_by_xpath(position1).click()#点击悬浮框上点击获取按钮
        except:
            self.mouse_above(position)# 当精选标和商用标共同存在时移动到商用标上
            if num == 1:
                self.driver.find_element_by_xpath(position).click()#点击商用标
            else:
                self.driver.find_element_by_xpath(position1).click()#点击悬浮框上点击获取按钮
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        #定位获取页面头部中千图网logo
        name = self.driver.find_element_by_xpath(head_position).get_attribute('title')
        if '千图网'in name:
            return True
        return False

    @CommonFunction.catch_exception
    def details_click_vip(self, id, num=None):
        '''
        测试详情页点击vip标、点击了解详细按钮
        :param id: 
        :param num: 
        :return: 
        '''

        position = '//*[@id="main-left"]/div[@class="mainLeft-title"]/a[@class="pic-type"]'
        position1 = '//*[@id="main-left"]/div[@class="mainLeft-title"]/a[2]'
        head_position = '/html/body/div[@class="qt-header "]/div/a'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/'+str(id)+'.html')
        if num == 1:
            self.driver.find_element_by_xpath(position1).click() #点击了解详细
        else:
            self.driver.find_element_by_xpath(position).click() #点击vip标签
        self.switch_to_window_close()  #跳入新句柄关闭原句柄
        #定位获取页面头部中千图网logo
        name = self.driver.find_element_by_xpath(head_position).get_attribute('title')
        if '千图网'in name:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_button(self, id, num=None):
        '''
        测试详情页下载按钮
        :param id: 
        :param num: 1：点击带jpg下载的源文件下载或者png下载  2：jpg下载  None：点击带png下载的源文件下载或免费下载
        :return: 
        '''



        position = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/'\
                   'div[@class="clearfix detail-down showDetail-header"]/a['+str(num)+']'
        position1= '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                   'div[@class="clearfix detail-down showDetail-header"]/div[1]'

        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        if num != None:
            self.driver.find_element_by_xpath(position).click() #点击带jpg下载的源文件下载/png下载/jpg下载
        else:
            self.driver.find_element_by_xpath(position1).click()  #点击带png下载的源文件下载/免费下载

        self.switch_to_window_close()  #跳入新句柄关闭原句柄
        if '千图网'in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_button_zk(self, id):
        '''
        测试字库免费下载按钮
        :param id: 
        :return: 
        '''

        position = '/html/body/div[@class="showDetail-container ZK-type"]/div[@class="showDetail-main w1200 clearfix"]'\
                   '/div[@class="main-right fr"]/div[@class="fr clearfix detail-down-Zk showDetail-header "]'\
                   '/div[@class="detailBtn-down-Zk download-page fl"]'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath(position).click() #点击下载
        self.switch_to_window_close()  #跳入新句柄关闭原句柄
        if '千图网'in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_button_ip(self, id):
        '''
        测试ip详情页免费下载按钮
        :param id: 
        :return: 
        '''

        position = '/html/body/div[@class="showDetail-container  YC-type"]/div[@class="showDetail-main w1200 clearfix"]' \
                   '/div[@class="main-right fr"]/div[@class="ipCode"]/ul[@class="ipCode-btnModel"]/div/' \
                   'div[@class="detailBtn-down download-page fl"]'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath(position).click()  # 点击下载
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_collection(self, id):
        '''
        测试详情页收藏按钮
        :param id: 
        :return: 
        '''



        position = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/'\
                   'div[@class="clearfix detail-down showDetail-header"]/div[@class="detailBtn-fav fl handle-fav"]'

        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath(position).click()  # 点击收藏
        title = self.driver.find_element_by_xpath(
            '//*[@id="favirite-all"]/div/div/div/div[1]'
        ).get_attribute("innerHTML") #获取div标签文本
        print(title)

        if '收藏夹' in title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_collection_zk(self, id):
        '''
        测试字库详情页收藏按钮
        :param id: 
        :return: 
        '''

        position = '/html/body/div[@class="showDetail-container ZK-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                   'div[@class="main-right fr"]/div[@class="fr clearfix detail-down-Zk showDetail-header "]/' \
                   'div[@class="detailBtn-fav-Zk fl handle-fav"]'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath(position).click()  # 点击下载
        title = self.driver.find_element_by_xpath(
            '//*[@id="favirite-all"]/div/div/div/div[1]'
        ).get_attribute("innerHTML") #获取div标签文本
        print(title)
        if '收藏夹' in title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_collection_ip(self, id):
        '''
        测试ip详情页收藏按钮
        :param id: 
        :return: 
        '''


        position = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                   'div[@class="ipCode"]/ul[@class="ipCode-btnModel"]/div[@class="fr clearfix detail-down showDetail-header"]/' \
                   'div[@class="detailBtn-fav fl handle-fav"]'

        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath(position).click()  # 点击下载
        title = self.driver.find_element_by_xpath(
            '//*[@id="favirite-all"]/div/div/div/div[1]'
        ).get_attribute("innerHTML") #获取div标签文本
        print(title)
        if '收藏夹' in title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_protocol(self, id):
        '''
        测试详情页授权方式
        :param id: 
        :return: 
        '''


        position = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                   'div[@class="material-info material-copyright clearfix"]/p[@class="authorization"]/a'

        position_zk = '/html/body/div[@class="showDetail-container ZK-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                      'div[@class="main-right fr"]/div[@class="material-info material-copyright clearfix fl"]/' \
                      'p[@class="authorization"]/a'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        try:
            self.driver.find_element_by_xpath( position ).click() #点击vrf协议
            self.switch_to_window_close()  # 跳入新句柄关闭原句柄
            if '千图网'in self.driver.title:
                return True
            return False
        except:
            title = self.driver.find_element_by_xpath(position_zk).get_attribute("href") #获取字体商用授权页面链接
            if 'pdf'in title:
                 return True
            return False

    @CommonFunction.catch_exception
    def details_download_purchase_authorization(self, id, num):
        '''
        测试ip形象购买授权弹窗
        :param id: 
        :param num: 1：基础版  2：专业版  3：旗舰版
        :return: 
        '''

        position_package = '/html/body/div[@class="showDetail-container  YC-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                           'div[@class="main-right fr"]/div[@class="wareStyle"]/ul[@class="wareStyle-toggle"]/li['+str(num)+']'
        position_buy = '/html/body/div[@class="showDetail-container  YC-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                       'div[@class="main-right fr"]/div[@class="wareStyle"]/a[@class="wareStyle-btn"]'
        position_price = '/html/body/div[@class="showDetail-container  YC-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                         'div[@class="main-right fr"]/div[@class="wareStyle"]/ul[@class="wareStyle-num"]/li[1]/i'
        position_price1 = '/html/body/div[@class="playMes"]/div/div[@class="playMesModel play-block"]/' \
                          'div[@class="playSum"]/li[@class="playSum-payment"]/i'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath( position_package ).click()   #点击选中基础版/专业版/旗舰版
        price = self.driver.find_element_by_xpath( position_price ).text #获取当前选中基础版/专业版/旗舰版的价格
        # print(price)
        self.driver.find_element_by_xpath(position_buy).click() #点击购买授权
        price1 = self.driver.find_element_by_xpath( position_price1 ).text #获取弹出窗上的选中价格
        # print(price1)

        if price1 in price:
            return True
        return False

    @CommonFunction.catch_exception
    def details_download_license_agreement(self,id):
        '''
        测试下载授权协议
        :param id: 
        :return: 
        '''


        download_agreement = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                             'div[@class="material-info material-copyright clearfix"]/p[3]/a'
        download_agreement_zk = '/html/body/div[@class="showDetail-container ZK-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                                'div[@class="main-right fr"]/div[@class="material-info material-copyright clearfix fl"]/p[3]/a'

        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        try:
            self.driver.find_element_by_xpath(download_agreement).click()  #点击下载授权协议
        except:
            self.driver.find_element_by_xpath(download_agreement_zk).click()  # 点击下载字库授权协议
        time.sleep(1)
        div = self.driver.find_element_by_xpath('//*[@id="model-enterVip"]').get_attribute("style")  #获取当前弹窗状态
        print(div)
        if 'block' in div: #不能下载授权
            btn = self.driver.find_element_by_xpath('//*[@id="alert-enter-vip-btn"]').text #获取弹窗中按钮文本

            if '立即加入企业VIP' in btn:  # 如果按钮文本是立即加入企业VIP
                self.driver.find_element_by_xpath('//*[@id="alert-enter-vip-btn"]').click() #点击按钮
                if '千图网' in self.driver.title:
                    return True
                return False
            else:
                if '我知道了' in btn:  #如果按钮文本是 我知道了
                    return True
                return False
        elif div == '':  #如果div是空的，可以下载授权
            return True
        return False

    @CommonFunction.catch_exception
    def details_obtain_authorization(self, id):
        '''
        测试获取企业商用授权按钮/了解字体商用授权按钮   必须是没有企业vip账号
        :param id: 
        :return: 
        '''


        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                      'div[@class="material-info material-copyright clearfix"]/p[4]/button[@class="down_cop1"]/a'

        positioning_zk = '/html/body/div[@class="showDetail-container ZK-type"]/div[@class="showDetail-main w1200 clearfix"]/' \
                         'div[@class="main-right fr"]/div[@class="material-info material-copyright clearfix fl"]/' \
                         'p[4]/button[@class="down_cop1"]/a'


        self.new_window_open()  # 新开页面

        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        try:
            self.driver.find_element_by_xpath(positioning).click() #点击获取企业商用授权
        except:
            self.driver.find_element_by_xpath(positioning_zk).click() #点击了解字体商用授权

        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '千图网' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_leaflet_resale(self, id):
        '''
        测试单张购买转售咨询/咨询客服
        :param id: 
        :return: 
        '''


        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                      'div[@class="material-info material-copyright clearfix"]/div[@class="mainRight-inform consultation"]/a'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath( positioning ).click()  #点击单张购买转售咨询
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if '客服热线' in self.driver.title or '千图网' in self.driver.title:

            return True
        return False

    @CommonFunction.catch_exception
    def details_photograph(self, id, num):
        '''
        测试详情页摄图网id
        :param id: 
        :param num: 摄图网id坑位
        :return: 
        '''


        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/' \
                      'div[@class="main-right fr"]/div[@class="toggle-main fr clearfix detail-down"]/' \
                      'p[@class="new-p-text"]/span[2]/span['+str(num)+']'
        positioning1 = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/' \
                       'div[@class="main-right fr"]/div[@class="toggle-main fr clearfix detail-down"]/' \
                       'p[@class="new-p-text"]/span[2]/a'


        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        name = self.driver.find_element_by_xpath(positioning1).text  #获取当前名字
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        title = re.sub(pattern, '', name) #去除非中文字符
        print(title)
        self.driver.find_element_by_xpath( positioning ).click()  #点击摄影图 id
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        time.sleep(2)
        if title in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_work_label(self, id, num):
        '''
        测试作品标签
        :param id: 
        :param num: 
        :return: 
        '''


        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/' \
                      'div[@class="main-right fr"]/div[@class="toggle-main fr clearfix works-dataTags"]/' \
                      'div[@class="clearfix mainRight-tagBox"]/a['+str(num)+']'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(400) #向下移动400像素

        name = self.driver.find_element_by_xpath(positioning)
        title = name.text  #获取作品标签名字
        print(title)
        name.click() #点击作品标签
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if title in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_author_avatar(self, id, num):
        '''
        测试点击作者头像跳转/查看主页按钮
        :param id: 
        :param num: 
        :return: 
        '''


        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                      '/div[@class="mainRight-user clearfix"]/div[@class="fl"]/div[@class="user-box fl"]/' \
                      'div[1]/a[@class="user-name"]'
        positioning1 = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                       '/div[@class="mainRight-user clearfix"]/div[@class="fl"]/div[@class="user-detail"]/' \
                       'div[@class="detail-btnGroup"]/a'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(400)  # 向下移动400像素

        self.mouse_above(positioning)
        name = self.driver.find_element_by_xpath(positioning)
        title = name.text
        print(title)
        if num == 1:
            name.click() #点击作者名字
        elif num ==2:
            self.driver.find_element_by_xpath(positioning1).click() #点击浮窗上查看主页按钮
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        if title in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_attention(self, id, num):
        '''
        测试作者旁关注按钮
        :param id: 
        :param num: 
        :return: 
        '''


        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                      '/div[@class="mainRight-user clearfix"]/div[@stats-point="105"]'
        positioning1 = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                       '/div[@class="mainRight-user clearfix"]/div[@stats-point="105"]/text()'
        positioning2 = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                       '/div[@class="mainRight-user clearfix"]/div[@class="fl"]/div[@class="user-detail"]/' \
                       'div[@class="detail-btnGroup"]/div[@stats-point="117"]'
        positioning3 = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                       '/div[@class="mainRight-user clearfix"]/div[@class="fl"]/div[@class="user-detail"]/' \
                       'div[@class="detail-btnGroup"]/div[@stats-point="117"]/text()'
        positioning4 = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                       '/div[@class="mainRight-user clearfix"]/div[@class="fl"]/div[@class="user-box fl"]/div[1]/a[@class="user-name"]'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(400)  # 向下移动400像素

        if num == 1:
            try:
                name = self.driver.find_element_by_xpath(positioning)
            except:
                name = self.driver.find_element_by_xpath(positioning1)
            title = name.text #获取关注按钮当前状态
            print(title)
            name.click()  #点击关注按钮
            time.sleep(1)

            try:
                name2 = self.driver.find_element_by_xpath(positioning1)
            except:
                name2 = self.driver.find_element_by_xpath(positioning)
            title2 = name2.text #获取最新关注按钮状态
            print(title2)
        elif num == 2:
            self.mouse_above(positioning4) #悬浮到头像上
            try:
                name = self.driver.find_element_by_xpath(positioning2)
            except:
                name = self.driver.find_element_by_xpath(positioning3)
            title = name.text #获取浮窗关注按钮当前状态
            print(title)
            name.click()
            time.sleep(1)
            try:
                name2 = self.driver.find_element_by_xpath(positioning3)
            except:
                name2 = self.driver.find_element_by_xpath(positioning2)
            title2 = name2.text  #获取浮窗上最新关注按钮状态
            print(title2)
        if title !=  title2:
            return True
        return False

    @CommonFunction.catch_exception
    def details_works_show(self, id, num):
        '''
        测试作品展示
        :param id: 
        :param num: 作者头像下，作品坑位
        :return: 
        '''

        positioning = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                      '/div[@class="toggle-main fr clearfix info-worksList"]/ul[@class="works-list"]/li['+str(num)+']/a'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(400)  # 向下移动400像素

        time.sleep(0.5)
        self.driver.find_element_by_xpath(positioning).click()
        time.sleep(0.5)
        name = self.driver.find_element_by_xpath(
            '/html/body/div[@class="qt-header "]/div/a'
        ).get_attribute('title')   # 获取页面头部logo 千图网
        if '千图网' in name:
            return True
        return False

    @CommonFunction.catch_exception
    def details_amplification_show(self, id):
        '''
        测试放大图片上下载按钮
        :param id: 
        :return: 
        '''

        positioning = '//div[@class="showDetail-header"]/div/div/div[2]/span[@class="pic-title fl"]'
        positioning1 = '/html/body/div[9]/div/div/div[@class="btn-group"]/p[1]/a'
        positioning2 = '/html/body/div[4]/div[@class="fl download-box"]/p[@class="title"]/a'
        positioning3 = '/html/body/div[4]/div[@class="limit-show-model"]/div/div[@class="limit-show-left"]/p'


        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        # js2 = 'var location=document.documentElement.scrollTop;' \
        #       'var b=document.documentElement.scrollTop=(location+1500)'
        # self.driver.execute_script(js2)

        self.driver_execute_script02(400)  # 向下移动400像素
        name = self.driver.find_element_by_xpath( positioning ).text #获取详情页图片名字
        print(name)
        try:
            self.driver.find_element_by_xpath('//*[@id="show-area-pic"]').click() #点击图片放大
        except:
            self.driver.find_element_by_xpath(
                '//*[@id="show-area-height"]/div[@class="gifWrap"]/img'
            ).click() #点击gif图片放大
        self.driver.find_element_by_xpath( positioning1 ).click() #点击放大后图片上的下载按钮
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        try:
            name2 = self.driver.find_element_by_xpath( positioning2 ).text #获取下载页文件名字
        except:
            name2 = self.driver.find_element_by_xpath( positioning3 ).text #获取下载页字库文件名

        # pattern = re.compile(r'[^\u4e00-\u9fa5]')
        # title = re.sub(pattern, '', name2)  # 去除非中文字符
        print(name2)
        if name in name2:
            return True
        return False



    @CommonFunction.catch_exception
    def details_recommended(self, id, num):
        '''
        测试详情页推荐作品下载
        :param id: 
        :param num: 
        :return: 
        '''

        positioning2 = '/html/body/div[4]/div[@class="fl download-box"]/p[@class="title"]/a'
        positioning3 = '/html/body/div[4]/div[@class="fl download-box isZK"]/p[@class="title"]/a'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(1500) #向下移动滚动条
        title = self.driver.find_element_by_xpath(
            '//*[@id="masonry"]/div['+str(num)+']/p/span[2]').text  #获取卡片的名字
        print(title)
        self.mouse_above('//*[@id="masonry"]/div['+str(num)+']/div/a')  #悬浮到卡片下
        self.driver.find_element_by_xpath(
            '//*[@id="masonry"]/div['+str(num)+']/div/a/div[3]/div[1]/span').click() #点击下载
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        try:
            title2 = self.driver.find_element_by_xpath( positioning2 ).text #获取下载页文件名字
        except:
            title2 = self.driver.find_element_by_xpath( positioning3 ).text #获取下载页字库文件名
        print(title2)
        if title in title2:
            return True
        return False

    @CommonFunction.catch_exception
    def details_recommended_2(self, id, num):
        '''
        测试详情页推荐卡片，点击卡片跳转到详情页
        :param id: 
        :param num: 第几个卡片 1~16
        :return: 
        '''

        positioning = '/html/body/div[8]/div[@class="showDetail-header"]/div/div/div[@class="detail-title fl"]/span[1]'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(1500)  #向下移动滚动条
        title = self.driver.find_element_by_xpath(
            '//*[@id="masonry"]/div['+str(num)+']/p/span[2]').text  #获取卡片的名字
        print(title)
        self.driver.find_element_by_xpath(
            '//*[@id="masonry"]/div['+str(num)+']/div/a').click() #点击下载
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath( positioning ).text #获取详情页素材名字
        print(title2)
        if title in title2:
            return True
        return False


    @CommonFunction.catch_exception
    def details_ip_figure_captions(self, id, num):
        '''
        测试ip详情页ip文章配图
        :param id: 
        :param num: 第几个文章配图
        :return: 
        '''

        positioning_title = '//*[@id="main-left"]/div[@class="series"]/div/div['+str(num)+']/p/span[@class="title-text"]'
        positioning_mouse = '//*[@id="main-left"]/div[@class="series"]/div/div['+str(num)+']/div'
        positioning_click =  '//*[@id="main-left"]/div[@class="series"]/div/div['+str(num)+']/div/a/div[@class="card-handle"]/div[1]/span'
        positioning_title2 = '/html/body/div[8]/div[@class="showDetail-header"]/div/div/div[@class="detail-title fl"]/span[1]'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver_execute_script02(1100)  #向下移动滚动条
        title = self.driver.find_element_by_xpath( positioning_title ).text  #获取卡片名字
        print(title)
        self.mouse_above(positioning_mouse) #悬浮到卡片上
        self.driver.find_element_by_xpath( positioning_click ).click() #点击查看详情按钮
        self.switch_to_window_close()  # 跳入新句柄关闭原句柄
        title2 = self.driver.find_element_by_xpath( positioning_title2 ).text #获取详情页名字
        print(title2)
        if title in title2:
            return True
        return False


    @CommonFunction.catch_exception
    def details_download_collection(self, id):
        '''
        测试下载按钮旁收藏按钮
        :param id: 
        :return: 
        '''
        positioning_click = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                            '/div[@class="clearfix detail-down showDetail-header"]/div[@class="detailBtn-fav fl handle-fav"]/i'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath( positioning_click ).click()  #点击搜藏按钮
        time.sleep(1)
        title = self.driver.find_element_by_xpath(
            '//*[@id="favirite-all"]/div/div/div/div[@class="model-title"]'
        ).text  #获取弹窗标题
        print(title)
        if '收藏夹' in title:
            return True
        return False


    @CommonFunction.catch_exception
    def details_ip_download_collection(self, id):
        '''
        测试ip形象下载按钮旁的收藏按钮
        :param id: 
        :return: 
        '''

        positioning_click = '/html/body/div[8]/div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]' \
                            '/div[@class="ipCode"]/ul[@class="ipCode-btnModel"]/div/div[@class="detailBtn-fav fl handle-fav"]/i'


        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath( positioning_click ).click() #点击搜藏按钮
        time.sleep(1)
        title = self.driver.find_element_by_xpath(
            '//*[@id="favirite-all"]/div/div/div/div[@class="model-title"]'
        ).text  #获取弹窗标题
        print(title)
        if '收藏夹' in title:
            return True
        return False

    @CommonFunction.catch_exception
    def details_zk_download_collection(self, id):
        '''
        测试字库详情页下载按钮旁的收搜按钮
        :param id: 
        :return: 
        '''

        positioning_click = '/html/body/div[@class="showDetail-container ZK-type"]/' \
                            'div[@class="showDetail-main w1200 clearfix"]/div[@class="main-right fr"]/' \
                            'div[@class="fr clearfix detail-down-Zk showDetail-header "]/' \
                            'div[@class="detailBtn-fav-Zk fl handle-fav"]/i'

        self.new_window_open()  # 新开页面
        self.driver.get('https://www.58pic.com/newpic/' + str(id) + '.html')
        self.driver.find_element_by_xpath( positioning_click ).click() #点击搜藏按钮
        time.sleep(1)
        title = self.driver.find_element_by_xpath(
            '//*[@id="favirite-all"]/div/div/div/div[@class="model-title"]'
        ).text  #获取弹窗标题
        print(title)
        if '收藏夹' in title:
            return True
        return False














if __name__ == '__main__':
    driver = browser()
    f = DLAutomatedTest(driver)
    print(f.drop_home_landing('cstest07', '123456'))

    id = 32822153
    # id = 32822058

    num = 1
    # print(f.details_current_position(id,num))
    # print(f.details_commercial_standard(id))
    # print(f.details_click_vip(id,num))
    # print(f.details_download_button(id))
    # print(f.details_download_button_zk(id))
    # print(f.details_download_collection(id))
    # print(f.details_download_collection_ip(id))
    # print(f.details_download_protocol(id))
    # print(f.details_download_purchase_authorization(id,num))
    # print(f.details_download_license_agreement(id))
    # print(f.details_obtain_authorization(id))
    # print(f.details_leaflet_resale(id))
    # print(f.details_photograph(id, num))
    # print(f.details_work_label(id, num))
    # print(f.details_attention(id, num))
    # print(f.details_works_show(id, num))

    # print(f.details_amplification_show(id))
    # print(f.details_recommended(id,num))
    # print(f.details_recommended_2(id, num))
    # print(f.details_ip_figure_captions(id))
    # print(f.details_ip_figure_captions(id, num))
    # print(f.details_download_collection(id))
    # print(f.details_ip_download_collection(id))
    print(f.details_zk_download_collection(id))





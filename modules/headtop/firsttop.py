from pic_project.common.commonfun import CommonFunction
from pic_project.common.driver import browser
import time

class DLAutomatedTest(CommonFunction):

    @CommonFunction.catch_exception
    def drop_down_box_pmgg(self, user_name, password):
        '''
        测试分类下拉框平面广告
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url ='https://www.58pic.com/'
        self.driver.get(url)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]')
        time.sleep(1)
        menu = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[1]/div[1]/a[1]')
        name = menu.text
        print(name)
        menu.click()
        self.switch_to_window_close()#关闭原页面进入新页面
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_down_box_dstb(self, user_name, password):
        '''
        测试分类下拉框电商淘宝
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url ='https://www.58pic.com/'
        self.driver.get(url)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]')
        time.sleep(1)
        menu = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[1]/div[1]/a[2]')
        name = menu.text
        print(name)
        menu.click()
        self.switch_to_window_close()#关闭原页面进入新页面
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_down_box_jrhb(self, user_name, password):
        '''
        测试分类下拉框平面广告下节日海报
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url ='https://www.58pic.com/'
        self.driver.get(url)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]')
        time.sleep(1)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[1]/div[1]/a[1]')
        menu = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[1]/div[2]/div[1]/div/a[1]')
        name = menu.text
        print(name)
        menu.click()
        self.switch_to_window_close()#关闭原页面进入新页面
        if name in self.driver.title:
            return True
        else:
            return False



    @CommonFunction.catch_exception
    def drop_down_box_symb(self, user_name, password):
        '''
        测试分类下拉框电商淘宝下首页模板
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url = 'https://www.58pic.com/'
        self.driver.get(url)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]')
        time.sleep(1)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[1]/div[1]/a[1]')
        menu = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[1]/div[2]/div[2]/div/a[2]')
        name = menu.text
        print(name)
        menu.click()
        self.switch_to_window_close()#关闭原页面进入新页面
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_down_box_ys(self, user_name, password):
        '''
        测试分类下拉框元素
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url = 'https://www.58pic.com/'
        self.driver.get(url)
        self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]')
        time.sleep(1)
        menu = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[2]/div[1]/a[1]')
        name = menu.text
        print(name)
        menu.click()
        self.switch_to_window_close()#关闭原页面进入新页面
        if name in self.driver.title:
            return True
        else:
            return False


    @CommonFunction.catch_exception
    def drop_down_box_zsta(self, user_name, password):
        '''
        测试分类下拉框元素分类下装饰图案
        :param user_name: 
        :param password: 
        :return: 
        '''
        self.user_login(user_name, password)
        url = 'https://www.58pic.com/'
        self.driver.get(url)
        #self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]')
        self.mouse_above('/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-main clearfix"]/div[@class="search-btn-classify"]')
        time.sleep(1)
        #self.mouse_above('/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[2]/div[1]/a[1]')
        self.mouse_above('/html/body/div[@class="qt-index-header"]/div/div[@class="header-row-search"]/div[@class="search-main clearfix"]/div[@class="search-btn-classify active"]/div[@class,"search-classify search-index-classify active"]/dl[@class="list-box"]/dd[@class="active"]/div[1]/a[1]')
        menu = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[1]/div[1]/div/dl/dd[2]/div[2]/div[2]/div/a[1]')
        name = menu.text
        print(name)
        menu.click()
        self.switch_to_window_close()#关闭原页面进入新页面
        if name in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def drop_home_landing(self, user_name, password):
        self.user_login(user_name, password)
        url = 'https://www.58pic.com/'
        self.driver.get(url)

    @CommonFunction.catch_exception
    def drop_home_pingmian(self,user_name, password):
        self.drop_home_landing(user_name, password)   #/html/body/div[5]/ul/li[1]/a[1]
        elem = self.driver.find_element_by_xpath('/html/body/div[@class="works-element"]/ul[@class="works-box clearBoth fl"]/li[@class="fl"]/a[@class="works-title"]')
        title = elem.text
        print(title)
        elem.click()
        time.sleep(2)
        self.switch_to_window_open()
        print(self.driver.title)
                                               #/html/body/div[5]/div[1]/div[3]/ul[1]/li[2]
        num = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/em').text
        print(num)





if __name__ == '__main__':
    driver = browser()
    f = DLAutomatedTest(driver)
    print(f.drop_home_pingmian('cstest06', '123456'))
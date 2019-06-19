from time import sleep

from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PIL import ImageGrab
import time,os
import csv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pic.baseView.baseView import BaseView


class Common(BaseView):

    def mouseAbove(self, request_element_path):   #鼠标悬浮
        above = self.driver.find_element_by_xpath(request_element_path)
        ActionChains(self.driver).move_to_element(above).perform()


    def dominantWait(self,request_element_path):    #显性等待
        locator = (By.XPATH, request_element_path)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))  # 显性等待5秒,等待元素出现

        return element

    def findElementByJs(self, request_element_path):    #通过滚动条滚动查找元素
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        target = self.driver.find_element_by_xpath(request_element_path)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def skipActivity(self):             #主页跳过活动

        if self.driver.name == "phantomjs":
            pass
        else:
            activity_element_path = "html/body/div[5]/div[4]/div[4]/div[3]/div[3]/div[3]/div[3]/div[4]/div[6]/a[1]"
            try:
                self.driver.find_element_by_xpath(activity_element_path).click()
            except NoSuchElementException:
                pass
            except ElementNotVisibleException:
                pass

    def skipSearchGuide(self):          #搜索页跳过
        first_guide = "/html/body/div[8]/ul[2]"
        second_guide = "/html/body/div[8]/ul[3]/li[2]"
        try:
            self.driver.find_element_by_xpath(first_guide).click()
            self.driver.find_element_by_xpath(second_guide).click()
            sleep(1)
        except:
            pass

    def checkLoginAlert(self,check_element_path=None, element_name=None):   #主页登录窗口的判断  (非真弹框)
        try:
            if self.driver.find_element_by_xpath(check_element_path):
                return True
            else:
                self.getScreenShot(element_name)  # 出错截屏
                return False
        except:
            self.getScreenShot(element_name)  # 出错截屏
            return False

    def checkImageLink(self,element_name):                  #主页图片链接的判断
        str_path = "/html/body/div[4]/div[1]/div/div/div[1]"
        c  # 获取所有句柄
        if len(all_h) < 2:  # 如果没有点击没有弹出新页面 本界面也可能获取
            self.getScreenShot(element_name)  # 出错截屏
            return False
        self.driver.switch_to_window(all_h[len(all_h) - 1])  # 跳入新句柄
        result = self.driver.find_element_by_xpath(str_path).text
        return  result.split('\n')[0]


    def checkSearchViewClickHasHandles(self, describe=None, check_element_path=None):
        try:
            if ">" in describe:         # 将字符串中的 > 除去
                describe = describe.replace(">","")

            all_h = self.driver.window_handles  # 获取所有句柄
            if len(all_h) < 2:  #如果没有点击没有弹出新页面 本界面也可能获取
                self.getScreenShot(describe)  # 出错截屏
                return  False
            self.driver.switch_to_window(all_h[len(all_h) - 1])  # 跳入新句柄
            try:
                if self.dominantWait("html/body/div[1]/div") != None:   #判断元素是否存在
                    if self.driver.find_element_by_xpath("html/body/div[1]/div").\
                            get_attribute("class") == "error": # 404界面是否存在
                        self.getScreenShot(describe)  # 出错截屏
                        return False
            except:
                pass
            self.driver.find_element_by_xpath(check_element_path)  # 判断元素是否存在
            return True
        except :
            self.getScreenShot(describe)  # 出错截屏
            return False

    def checkSearchViewClickNoHandles(self, describe=None, check_element_path=None):     #主页无句柄的判断
        try:
            if self.getAttribute("html/body/div[1]/div", "class") == "error":
                self.getScreenShot(describe)  # 出错截屏
                return False
            else:
                self.driver.find_element_by_xpath(check_element_path)  # 判断元素是否存在
                return True
        except:
            self.getScreenShot(describe)  # 出错截屏
            return False

    def checkFirstViewClickHasHandles(self, check_element_path=None, element_name=None):    #主页有句柄的判断
        try:
            if ">" in element_name:         # 将字符串中的 > 除去
                element_name = element_name.replace(">","")

            all_h = self.driver.window_handles  # 获取所有句柄
            if len(all_h) < 2:  #如果没有点击没有弹出新页面 本界面也可能获取
                self.getScreenShot(element_name)  # 出错截屏
                return  False
            self.driver.switch_to_window(all_h[len(all_h) - 1])  # 跳入新句柄
            try:
                if self.dominantWait("html/body/div[1]/div") != None:   #判断元素是否存在
                    if self.driver.find_element_by_xpath("html/body/div[1]/div").\
                            get_attribute("class") == "error": # 404界面是否存在
                        self.getScreenShot(element_name)  # 出错截屏
                        return False
            except:
                pass
            self.driver.find_element_by_xpath(check_element_path)  # 判断元素是否存在
            return True
        except :
            self.getScreenShot(element_name)  # 出错截屏
            return False

    def checkFirstViewClickNoHandles(self, check_element_path=None, element_name=None):     #主页无句柄的判断
        try:
            if self.driver.find_element_by_xpath("html/body/div[1]/div").get_attribute("class") == "error":
                self.getScreenShot(element_name)  # 出错截屏
                return False
            else:
                self.driver.find_element_by_xpath(check_element_path)  # 判断元素是否存在
                return True
        except:
            self.getScreenShot(element_name)  # 出错截屏
            return False

    def checkElementExist(self,element_path):
        try:
            if self.xpath_find(element_path):
                return True
            else:
                return False
        except:
            return False
    def getTagText(self,describe_path):
        describe = str(self.driver.find_element_by_xpath(describe_path).text)
        return describe

    def numReplace(self,str_num=None):
        if "," in str_num:
            str_num = int(str_num.replace(",", ""))
            return int(str_num)
        else:
            return int(str_num)

    def getAttribute(self, request_path, value):

        return self.xpath_find(request_path).get_attribute(value)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):         #异常截图
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        # logging.info('get %s sreenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
        # image = ImageGrab.grab()
        # image.save(image_file)


    def get_csv_data(self,csv_file, line):
        logging.info('============get_csv_data============')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

if __name__=='__main__':
    print()
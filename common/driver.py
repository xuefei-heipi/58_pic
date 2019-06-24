#!/usr/bin/env python3
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver
'''
初始化浏览器接口
'''

def browser():
    '''
        浏览器驱动生成
        :return: 
        '''
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('headless') #无头浏览
    chrome_driver_path = os.getcwd() + '/chromedriver.exe'
    chrome_driver_path = chrome_driver_path.split('pic_project')[0] + '/pic_project/common/chromedriver.exe'

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.set_window_size(2062, 1126)
    driver.set_window_position(0, 0)
    return driver




if __name__ == '__main__':
    # driver=browser()
    # if driver.name == "phantomjs":
    #     print(True)
    #
    # driver.get("http://www.baidu.com")
    # driver.get("http://www.58pic.com/piccate/1-0-0.html")
    #
    # des = driver.find_element_by_xpath("html/body/div[1]/div").get_attribute("class")

    # print(des)
    # sleep(2)
    # driver.quit()
    # for x in range(0,10000):
    #     print(x)
    driver = browser()
    driver.maximize_window()
    # driver.get("http://www.58pic.com")
    # driver.add_cookie({'name': 'auth_id', 'value': '%2242688531%7Cwsltest40%7C1540883167%7C1d0a115dd1207a72eae011dabc5e14b8%22'})
    # driver.add_cookie({'name': 'growth-time', 'value': '1'})
    # driver.refresh()
    user_name = ["xztest" + str(i)
                 for i in range(1,2)]
    driver.get("http://www.58pic.com/newpic/32279473.html")
    sleep(3)
    # driver.refresh()
    # sleep(3)
    # driver.refresh()
    for x in range(0,len(user_name)):
        # driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[@class="showDetail-container  YC-type OGC-type"]/div[2]/div[3]/div[1]/div[@data-id="32279473" and @sta-site="6"]').click()
        driver.find_element_by_xpath('/html/body/div[@class="qt-model-t login-model"]/div/div/div/div[3]/div[3]/p[1]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="account"]').send_keys(user_name[x])
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("123456")
        driver.find_element_by_xpath('/html/body/div[@class="qt-model-t login-model"]/div/div/div/div[3]/div[2]/div[2]/div/div[4]/a').click()
        sleep(3)
        for cookie in driver.get_cookies():
            if cookie['name'] == 'auth_id':
                print(user_name[x] +  "   " + cookie['value'])

        driver.delete_all_cookies()
        driver.refresh()


        # driver.delete_cookie('1490c6811c510539f99068d1b8b4e2ba')
        # driver.add_cookie({'name': '1490c6811c510539f99068d1b8b4e2ba', 'value': '%22101.88.237.234%22'})  # 添加cookie跳过新手礼包
        # for cookie in driver.get_cookies():
        #     print(cookie)
        # Common(driver).getScreenShot(str(x))
        # driver.quit()
    # data = driver.page_source
    # print(data)
    # print(driver.get_window_size())
    # driver.current_window_handle
    # driver.close()
    # driver.current_url
    # driver.implicitly_wait()
    # driver.switch_to.frame()
    # driver.refresh()
    # driver.switch_to.alert.dismiss()
    # driver.implicitly_wait(10)
    # image1 = driver.get_screenshot_as_base64()
    # sleep(4)
    # image2 = driver.get_screenshot_as_base64()
    # if image1 == image2:
    #     print(True)

    # for cookie in driver.get_cookies():
    #     print(cookie)
    #
    # print('----------------------------')
    # driver.find_element_by_class_name()
    # driver.delete_cookie('qt_createtime')
    # driver.add_cookie({'name': 'qt_createtime', 'value': '1533139205'})
    # for cookie in driver.get_cookies():
    #     print(cookie)
    # sleep(3)
    # driver.quit()
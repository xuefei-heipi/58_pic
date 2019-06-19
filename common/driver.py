#!/usr/bin/env python3
from time import sleep
from PIL import ImageGrab
from selenium import webdriver

'''
初始化浏览器接口
'''
def browser():
    #不加载浏览器默认界面 这个比较慢有时候等死人  超过最大等待时间还要报错影响测试
    profile=webdriver.FirefoxProfile()
    profile.set_preference("browser.startup.homepage", "about:blank")
    profile.set_preference("startup.homepage_welcome_url", "about:blank")
    profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
    driver = webdriver.Firefox(profile) #火狐

    # 火狐无头加载    缺点 只能点击刚开始页面有的 无法动态切换页面元素
    # options = webdriver.FirefoxOptions()
    # options.set_headless(True)
    # driver = webdriver.Firefox(firefox_options=options)

    # driver=webdriver.Chrome() #谷歌
    # driver=webdriver.Ie(profile) #IE
    # driver=webdriver.PhantomJS()
    driver.maximize_window() #窗口最大化
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    driver=browser()
    if driver.name == "phantomjs":
        print(True)

    driver.get("http://www.baidu.com")
    driver.get("http://www.58pic.com/piccate/1-0-0.html")

    des = driver.find_element_by_xpath("html/body/div[1]/div").get_attribute("class")

    # print(des)
    # sleep(2)
    # driver.quit()
    # options = webdriver.FirefoxOptions()
    # options.set_headless(True)
    # driver = webdriver.Firefox(firefox_options=options)
    # driver.get("http://www.baidu.com")
    # driver.find_element_by_xpath("dfs").send_keys()
    # print(driver.page_source)
    # sleep(3)
    # driver.quit()
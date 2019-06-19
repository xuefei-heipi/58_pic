import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pic.common.commomFun import Common
from pic.common.driver import browser
from pic.common.getPath import GetPath


from pic.businessView.firestView.firstView import FirstView

class LoginView(FirstView):

    qq_login_element_path = ".//*[@id='statis-qq']/i"
    # qq_chose_element_path = ".//div[@class='qlogin_show']//div//a[1]"
    qq_chose_element_path = "html/body/div[1]/div[4]/div[8]/div[1]/a[1]"
    login_id_element_path = "html/body/div[2]/div/div[2]/div[2]/div[2]"


    def qq_login(self):

        try:

            # qq_chose_element_path = ".//div[@id='qlogin']//div[3]//div[8]//div//a//span[@class='img_out_focus']"
            self.first_floor_Login()
            self.driver.find_element_by_xpath(self.qq_login_element_path).click()   #点击qq登录

            self.driver.switch_to.frame("ptlogin_iframe")   #切换到iframe
            self.driver.find_element_by_xpath(self.qq_chose_element_path).click()   #选择第一个qq登录

            try:
                # 判断个人中心是否存在
                self.mouseAbove(self.login_id_element_path)
                self.driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[3]/div[8]/a[1]/i")
                return True
            except NoSuchElementException:
                self.getScreenShot("qq_login_error")
                return False
        except NoSuchElementException:
            self.getScreenShot("qq_login_error")
            return False



def test_commom():
    driver = browser()
    driver.maximize_window()
    driver.implicitly_wait(10)
    f = LoginView(driver)
    f.driver.get("http://www.58pic.com")

    VIP_element_path = "html/body/div[5]/div[4]/div[4]/div[3]/div[3]/div[3]/div[3]/div[4]/div[6]/a[1]"
    try:
        f.driver.find_element_by_xpath(VIP_element_path).click()
        return f
    except NoSuchElementException:
        pass
        return f


if __name__=='__main__':
    f = test_commom()
    f.qq_login()

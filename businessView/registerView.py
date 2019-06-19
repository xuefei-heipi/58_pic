import logging,random
from common.desired_caps import appium_desired
from common.commom_fun import Common,By,NoSuchElementException


class RegisterView(Common):
    register_text=(By.ID,'com.tal.kaoyan:id/login_register_text')
    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')
    saveBtn = (By.ID, 'com.tal.kaoyan:id/save')

    # 注册-个人信息界面元素
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    # 完善信息列表元素
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    # 院校列表元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    # 专业列表元素
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_myself = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    def register_action(self, register_username, register_password, register_email):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('=========register_action===========')
        self.driver.find_element(*self.register_text).click()

        # 头像设置
        logging.info('set userheader')
        self.driver.find_element(*self.userheader).click()
        self.driver.find_elements(*self.item_image)[2].click()
        self.driver.find_element(*self.saveBtn).click()

        # 用户名密码填写
        logging.info('register username is %s' % register_username)
        self.driver.find_element(*self.register_username).send_keys(register_username)

        logging.info('register_password is %s' % register_password)
        self.driver.find_element(*self.register_password).send_keys(register_password)

        logging.info('register_email is %s' % register_email)
        self.driver.find_element(*self.register_email).send_keys(register_email)

        logging.info('click register button')
        self.driver.find_element(*self.register_btn).click()

        # 判断是否进入到完善信息界面--注册太频繁会被限制无法进入该界面
        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenShot('register Fail')
            return False
        else:
            self.add_register_info()
            # 注册结果判断
            if self.check_registerStatus():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info('===========add_register_info===========')

        # 院校选择:上海——同济大学
        logging.info("select school...")
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.forum_title)[1].click()
        self.driver.find_elements(*self.university)[1].click()

        # 专业选择：经济学类-统计学-经济统计学
        logging.info("select major...")
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.major_subject_title)[1].click()
        self.driver.find_elements(*self.major_group_title)[2].click()
        self.driver.find_elements(*self.major_search_item_name)[1].click()

        self.driver.find_element(*self.perfectinfomation_goBtn).click()

    def check_register_status(self):
        self.check_market_ad()
        logging.info('==========check_registerStatus===========')

        try:
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('register Fail!')
            self.getScreenShot('register_Fail')
            return False
        else:
            logging.info('register success!')
            self.getScreenShot('register_success')
            return True


if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)

    username = 'zxw2018' + 'FLY' + str(random.randint(1000, 9000))
    password = 'zxw' + str(random.randint(1000, 9000))
    email = '51zxw' + str(random.randint(1000, 9000)) + '@163.com'

    register.register_action(username, password, email)

from Product.common.commonfun import CommonFunction
from Product.common.driver import browser
from Product.spbackstage.qt_backstage import QTBackstage
import time
import re

class MainPageTest(CommonFunction):

    @CommonFunction.catch_exception
    def main_page_search(self, user_name, password, search_word, is_login=0):
        """
        主页搜索功能
        :param user_name:
        :param password:
        :param search_word:  搜索词
        :param is_login:   0 不登录  1 登录
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
            self.driver.get('https://www.58pic.com')
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)

        # 搜索框xpath
        search_path = '//div[@class="header-func"]/div[1]/div[2]/input'
        # 搜索按钮xpath
        search_btn_path = '//button[@stats-point="943"]'
        # 输入搜索关键词
        self.driver.find_element_by_xpath(search_path).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(search_path).send_keys(search_word)
        # 点击搜索按钮
        self.driver.find_element_by_xpath(search_btn_path).click()
        time.sleep(1)
        # 获取搜索页面的title
        search_title = self.driver.title
        # 获取搜索页面的面包屑
        search_crumbs = self.driver.find_element_by_xpath('//p[@class="position-left"]').get_attribute('textContent')
        if search_word in search_title and search_word in search_crumbs:
            return True
        return False

    @CommonFunction.catch_exception
    def main_page_sign_in(self, user_name, password, is_login=0):
        """
        签到测试
        :param user_name:
        :param password:
        :param is_login:   0 不登录  1 登录
        :return:
        """

        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
            self.driver.get('https://www.58pic.com')
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)

        # 签到按钮xpath
        sign_in_path = '//a[@stats-point="1226"]'
        # 点击签到
        self.driver.find_element_by_xpath(sign_in_path).click()
        time.sleep(4)
        # 获取页面
        check_word = self.driver.find_element_by_id('signInCon').get_attribute('textContent')
        if '已领' in check_word:
            return True
        return False


    @CommonFunction.catch_exception
    def main_page_subscribe(self, user_name, password, is_login=0):
        """
        首页订阅功能
        :param user_name:
        :param password:
        :param is_login:
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
            self.driver.get('https://www.58pic.com')
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)

        # 判断当前页面状态
        inital_word = self.driver.find_element_by_xpath('//div[@class="nav-floor pic-floor"]/div/a/span').get_attribute('textContent')
        # 管理订阅 按钮 xpath
        manage_subscriptions_path = '//a[@stats-point="998"]'
        ggsj_paht = '//input[@value="14"]'   # 广告设计 xpaht
        cyhb_paht = '//input[@value="18"]'   # 创意海报 xpath
        zbzj_paht = '//input[@value="19"]'   # 展板展架 xpath
        mpkz_paht = '//input[@value="20"]'   # 名片卡证 xpath
        hczz_paht = '//input[@value="21"]'   # 画册装帧 xpath
        bzsj_paht = '//input[@value="22"]'   # 包装设计 xpath
        vids_paht = '//input[@value="23"]'   # VI | 导视 xpath
        logosj_paht = '//input[@value="24"]'   # LOGO设计 xpath
        # 完成按钮 xpath
        complete_btn_path = '//span[@data-clickid="1"]'

        self.driver.find_element_by_xpath(manage_subscriptions_path).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(ggsj_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(cyhb_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(zbzj_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(mpkz_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(hczz_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(bzsj_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(vids_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(logosj_paht).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(complete_btn_path).click()
        self.driver.refresh()

        check_word = self.driver.find_element_by_xpath('//div[@class="nav-floor pic-floor"]/div/a/span').get_attribute('textContent')
        if inital_word == '广告设计' and check_word == '画册装帧':
            return True
        elif inital_word == '画册装帧' and check_word == '广告设计':
            return True

        return False

    @CommonFunction.catch_exception
    def main_banner_switch(self, user_name, password, is_login=0):
        """
        主页banner切换功能
        :param user_name:
        :param password:
        :param is_login:
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
            self.driver.get('https://www.58pic.com')
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)

        # banner xpath
        banner_path = '//div[@class="banner-box"]/div'

        self.driver.find_element_by_xpath(banner_path).click()
        time.sleep(1)
        self.switch_to_window_close()
        title_1 = self.driver.title
        self.driver.get('https://www.58pic.com')
        time.sleep(5)
        self.driver.find_element_by_xpath(banner_path).click()
        self.switch_to_window_close()
        title_2 = self.driver.title
        if title_1 != title_2:
            return True
        return False

    @CommonFunction.catch_exception
    def main_creative_center(self, user_name, password, designer_type, is_login=0):
        """
        首页创作中心
        :param user_name:
        :param password:
        :param designer_type: 0 无身份 1 UGC 2 OGC
        :param is_login:
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        self.driver.get('https://www.58pic.com')
        # 创作中心 xpath
        creative_center_path = '//a[@stats-point="946"]'
        # 鼠标hover操作
        self.mouse_above(creative_center_path)
        time.sleep(2)
        if designer_type == 0:
            check_word_1 = self.driver.find_element_by_xpath('//a[@stats-point="976"]').get_attribute('textContent')
            check_word_2 = self.driver.find_element_by_xpath('//a[@stats-point="1205"]').get_attribute('textContent')
            if check_word_1 == '申请加入' and check_word_2 == '申请加入':
                return True
            return False
        elif designer_type == 1:
            check_word_1 = self.driver.find_element_by_xpath('//a[@stats-point="983"]/..').get_attribute('textContent')
            check_word_2 = self.driver.find_element_by_xpath('//a[@stats-point="984"]/..').get_attribute('textContent')
            check_word_3 = self.driver.find_element_by_xpath('//a[@stats-point="985"]/..').get_attribute('textContent')
            check_word_4 = self.driver.find_element_by_xpath('//a[@stats-point="987"]/..').get_attribute('textContent')
            check_word_5 = self.driver.find_element_by_xpath('//a[@stats-point="978"]').get_attribute('textContent')
            check_word_6 = self.driver.find_element_by_xpath('//a[@stats-point="980"]').get_attribute('textContent')
            check_word_7 = self.driver.find_element_by_xpath('//a[@stats-point="981"]').get_attribute('textContent')
            check_word_8 = self.driver.find_element_by_xpath('//a[@stats-point="982"]').get_attribute('textContent')
            if '通过作品' in check_word_1 and '待审核' in check_word_2 and '已驳回' in check_word_3 and "可提现积分" in check_word_4 and '发布作品' in check_word_5 and '限定主题' in check_word_6 and '我的作品' in check_word_7 and '收入明细' in check_word_8:
                return True
            return False
        elif designer_type == 2:
            check_word_1 = self.driver.find_element_by_xpath('//a[@stats-point="983"]/..').get_attribute('textContent')
            check_word_2 = self.driver.find_element_by_xpath('//a[@stats-point="984"]/..').get_attribute('textContent')
            check_word_3 = self.driver.find_element_by_xpath('//a[@stats-point="985"]/..').get_attribute('textContent')
            check_word_4 = self.driver.find_element_by_xpath('//a[@stats-point="986"]/..').get_attribute('textContent')
            check_word_5 = self.driver.find_element_by_xpath('//a[@stats-point="978"]').get_attribute('textContent')
            check_word_6 = self.driver.find_element_by_xpath('//a[@stats-point="979"]').get_attribute('textContent')
            check_word_7 = self.driver.find_element_by_xpath('//a[@stats-point="981"]').get_attribute('textContent')
            check_word_8 = self.driver.find_element_by_xpath('//a[@stats-point="982"]').get_attribute('textContent')
            if '通过作品' in check_word_1 and '待审核' in check_word_2 and '已驳回' in check_word_3 and "本月收入" in check_word_4 and '发布作品' in check_word_5 and '主题领取' in check_word_6 and '我的作品' in check_word_7 and '收入明细' in check_word_8:
                return True
            return False

    @CommonFunction.catch_exception
    def main_advertisement_close(self, user_name, password, is_login=0):
        """
        首页广告关闭功能
        :param user_name:
        :param password:
        :param is_login:
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)
        # 关闭按钮 xpath
        close_btn_path = '//div[@data-type="posterIndex1"]/div/span'
        # 页面滚动到 关闭按钮处
        self.find_element_by_Js(close_btn_path)
        self.driver_execute_script02(-200)
        time.sleep(2)
        self.driver.find_element_by_xpath(close_btn_path).click()
        time.sleep(2)
        # 获取dom中 style的值
        check_word = self.driver.find_element_by_xpath('//div[@data-type="posterIndex1"]').get_attribute('style')
        if 'display: none' in check_word:
            return True
        return False

    @CommonFunction.catch_exception
    def main_page_qy_vip_switch(self, user_name, password, is_login=0):
        """
        个人切换为企业vip    必须使用帐号  xztest29
        :param user_name:
        :param password:
        :param is_login:
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)
        # 头像
        head_portrait_path = '//a[@stats-point="949"]'
        qy_switch_path = '//span[@data-id="8705"]'
        self.mouse_above(head_portrait_path)
        time.sleep(1)
        if self.driver.find_element_by_xpath(qy_switch_path).get_attribute('textContent') == '切换':
            self.mouse_above('//span[@data-id="8705"]/..')
            time.sleep(1)
            self.driver.find_element_by_xpath(qy_switch_path).click()

        elif self.driver.find_element_by_xpath(qy_switch_path).get_attribute('textContent') == '使用中':
            return True
        time.sleep(2)
        if self.driver.title == '千图网企业VIP':
            return True
        return False

    @CommonFunction.catch_exception
    def main_page_gr_vip_switch(self, user_name, password, is_login=0):
        """
        企业切换为个人vip    必须使用帐号  xztest29
        :param user_name:
        :param password:
        :param is_login:
        :return:
        """
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            self.driver.get('https://www.58pic.com')
            time.sleep(1)
        self.driver.get('https://www.58pic.com')
        # 头像
        head_portrait_path = '//a[@stats-point="949"]'
        gr_switch_path = '//div[@class="user-info-row user-header-v3"]/div[2]/p'
        self.mouse_above(head_portrait_path)
        time.sleep(1)
        try:
            # 如果 a 标签存在 就是未使用
            self.driver.find_element_by_xpath(gr_switch_path + '/a')
            if self.driver.find_element_by_xpath(gr_switch_path + '/a').get_attribute('textContent') == '切换':
                self.mouse_above(gr_switch_path)
                time.sleep(1)
                self.driver.find_element_by_xpath(gr_switch_path + '/a').click()
                time.sleep(2)
                self.mouse_above(head_portrait_path)
                if self.driver.find_element_by_xpath(gr_switch_path + '/span[2]').get_attribute('textContent') == '使用中':
                    return True
                return False
        except:
            time.sleep(1)
            if self.driver.find_element_by_xpath(gr_switch_path + '/  span[2]').get_attribute('textContent') == '使用中':
                return True
            return False



if __name__ == '__main__':
    t_driver = browser()
    b = MainPageTest(t_driver)
    print(b.main_creative_center('OGCtest2', '123456', 2, is_login=1))
    time.sleep(5)



# coding=utf-8
from Product.common.commonfun import CommonFunction
from Product.common.driver import browser
from Product.spbackstage.qt_backstage import QTBackstage
import time
import re

# 下载页xpath定位
# 个人vip定位
position = '/html/body/div[4]/div[@class="fl download-box"]/p[@class="down-info"]'
# 字库个人vip定位
position_zkgr = '/html/body/div[@class="w1200 download-main-details isYC clearfix"]/div[@class="fl download-box isZK"]/p[@class="down-info"]'
# 字库企业vip定位
position_zk = '/html/body/div[@class="w1200 download-main-limit isZK"]/div[@class="limit-showtop clearfix"]/div[@class="limit-showright"]/p[@class="limit-title1"]/i'


class DLAutomatedTest(CommonFunction):

    @CommonFunction.catch_exception
    def dl_no_jx_vip(self, user_name, password, pic_id):
        """
        无精选vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_jc_vip_1(self, user_name, password, pic_id):
        """
        无基础vip一次免费
        :param user_name:
        :param password:
        :param pic_id:
        :return:
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'sc')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '作品下载' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_jc_vip_0(self, user_name, password, pic_id):
        """
        无基础vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 1, 'sc')
        time.sleep(1)
        # self.driver.get('https://dl.58pic.com/34651443.html')   #除去免费一次
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_bg_vip(self, user_name, password, pic_id):
        """
        无办公vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        # self.driver.get('https://dl.58pic.com/32822153.html')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_zk_vip_1(self, user_name, password, pic_id):
        """
        无字库vip一次免费
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(10)
        if '作品下载' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_zk_vip_0(self, user_name, password, pic_id):
        """
        无字库vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_jx_vip_20(self, user_name, password, pic_id):
        """
        精选vip20次
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'yc')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(0.2)
        # 获取精选次数
        num1 = self.driver.find_element_by_xpath(position).text
        print(num1)
        s = list(map(int, re.findall(r"\d+", num1)))[0]
        if '千图网-作品下载' in self.driver.title and s < 20:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_jx_vip_20(self, user_name, password, pic_id):
        """
        精选vip20次用完受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 20, 'yc')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_jc_vip_20(self, user_name, password, pic_id):
        """
                基础vip20次
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'sc')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        # 获取基础次数
        num2 = self.driver.find_element_by_xpath(position).text
        print(num2)
        s = list(map(int, re.findall(r"\d+", num2)))[0]
        if '千图网-作品下载' in self.driver.title and s < 20:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_jc_vip_20(self, user_name, password, pic_id):
        """
        基础vip20次用完受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 20, 'sc')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_bg_vip_10(self, user_name, password, pic_id):
        """
                办公vip10次
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'bg')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        # 获取办公次数
        num2 = self.driver.find_element_by_xpath(position).text
        s = list(map(int, re.findall(r"\d+", num2)))[0]
        if '千图网-作品下载' in self.driver.title and s < 10:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_bg_vip_10(self, user_name, password, pic_id):
        """
                办公vip10次用完受限
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 10, 'bg')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_qy_vip_499(self, user_name, password, pic_id):
        """
        企业vip499次
        :param user_name:
        :param password:
        :param pic_id:
        :return:
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'qy499')

        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        # 获取企业次数
        num2 = self.driver.find_element_by_xpath(position).text
        s = list(map(int, re.findall(r"\d+", num2)))[0]
        if '千图网-作品下载' in self.driver.title and s < 400:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_qy_vip_499(self, user_name, password, pic_id):
        """
                企业vip499次用完受限
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
        """
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 200, 'qy499')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        # 悬浮到头像
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_zk_vip_20(self, user_name, password, pic_id):
        """
        字库vip20次
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        num = self.driver.find_element_by_xpath(position_zkgr).text
        s = list(map(int, re.findall(r"\d+", num)))[0]
        if s < 20:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_restrict_zk_vip_20(self, user_name, password, pic_id):
        """
        字库vip20次用完限制
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_zk_vip_999(self, user_name, password, pic_id, pic_id2):
        """
        字库vip999 20次授权下载
        :param user_name: 
        :param password: 
        :param pic_id: 
        :param pic_id2:
        :return:
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        head = self.driver.title
        # print(head)
        url2 = 'https://dl.58pic.com/' + str(pic_id2) + '.html?is_auto=0'
        self.driver.get(url2)
        time.sleep(1)
        head2 = self.driver.title
        # print(head2)
        if '千图网-作品下载' in head and '千图网-作品下载' in head2:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_zk_vip_999(self, user_name, password, pic_id):
        """
        字库vip999 20次授权下载用完
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        num = driver.find_element_by_xpath(position_zk).text
        print(num)
        s = list(map(int, re.findall(r"\d+", num)))[0]
        if '千图网-下载受限' in self.driver.title and s == 0:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_mf_wx(self, user_name, password, pic_id):
        """
        免费无限下载国家、官方授权素材
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        """
        self.user_login(user_name, password)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html?is_auto=0'
        self.driver.get(url)
        time.sleep(1)
        if '千图网-作品下载' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_vip_active(self, user_name, password, pic_id, is_login=0):
        """
        测试无下限下载vip有效期内下载成功
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login: 0: 不需要登录   1: 需要登录
        :return:
        """
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        url = 'https://dl.58pic.com/%s.html?is_auto=0' % pic_id
        self.driver.get(url)
        time.sleep(1)
        # 判断是否进入下载成功页
        if '作品下载' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_vip_expire(self, user_name, password, pic_id, is_login=0):
        """
        测试无vip过期下载受限
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login: 0: 不需要登录   1: 需要登录
        :return:
        """
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            # 消除免费次数
            self.driver.get('https://dl.58pic.com/34878067.html?is_auto=0')
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        url = 'https://dl.58pic.com/%s.html?is_auto=0' % pic_id
        self.driver.get(url)
        time.sleep(1)
        # 判断是否进入下载成功页
        if '下载受限' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_qy_certified_active(self, user_name, password, pic_id, is_login=0):
        """
        测试企业vip认证通过下载
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login: 0: 不需要登录   1: 需要登录
        :return:
        """
        # 修改企业vip到期时间
        if user_name == 'xztest17':
            QTBackstage().revise_qy_vip_time('1881', 1, '2030-01-01')
        elif user_name == 'xztest20':
            QTBackstage().revise_qy_vip_time('2862', 2, '2030-01-01')
        elif user_name == 'xztest21':
            QTBackstage().revise_qy_vip_time('2863', 3, '2030-01-01')
        elif user_name == 'xztest22':
            QTBackstage().revise_qy_vip_time('9512', 5, '2030-01-01')
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        url = 'https://dl.58pic.com/%s.html?is_auto=0' % pic_id
        self.driver.get(url)
        time.sleep(1)
        # 判断是否进入下载成功页
        if '作品下载' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_qy_certified_expire(self, user_name, password, pic_id, is_login=0):
        """
        测试企业vip认证通过期下载是失败
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login: 0: 不需要登录   1: 需要登录
        :return:
        """
        # 修改企业vip到期时间
        if user_name == 'xztest17':
            QTBackstage().revise_qy_vip_time('1881', 1, '2018-01-01')
        elif user_name == 'xztest20':
            QTBackstage().revise_qy_vip_time('2862', 2, '2018-01-01')
        elif user_name == 'xztest21':
            QTBackstage().revise_qy_vip_time('2863', 3, '2018-01-01')
        elif user_name == 'xztest22':
            QTBackstage().revise_qy_vip_time('9512', 5, '2018-01-01')
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        url = 'https://dl.58pic.com/%s.html?is_auto=0' % pic_id
        self.driver.get(url)
        time.sleep(1)
        # 判断是否进入下载成功页
        if '下载受限' in self.driver.title:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_qy_certified_limit(self, user_name, password, pic_id, is_login=0):
        """
        企业认证vip当日下载超过100次限制
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login:
        :return:
        """
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        import datetime
        date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        url = 'https://dl.58pic.com/%s.html?dlNumsAll=90&dlNumsToday=100&last_dl_time=%s:00&is_auto=0' % (pic_id, date)
        self.driver.get(url)
        time.sleep(1)
        # 获取检测文字
        check_word = self.driver.find_element_by_xpath('//*[@class="freq-popup"]').get_attribute('textContent')
        # 判断是否进入下载成功页
        if '下载太快啦' in check_word:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_qy_uncertified_remind(self, user_name, password, pic_id, is_login=0):
        """
        企业未认证vip当日下载提醒
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login:
        :return:
        """
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        import datetime
        date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        url = 'https://dl.58pic.com/%s.html?dlNumsAll=90&dlNumsToday=10&last_dl_time=%s:00&is_auto=0' % (pic_id, date)
        self.driver.get(url)
        time.sleep(1)
        # 获取检测文字
        check_word = self.driver.find_element_by_xpath('//*[@class="freq-popup"]').get_attribute('textContent')
        # 判断是否进入下载成功页
        if '企业版权风险提醒' in check_word:
            return True
        return False

    @CommonFunction.catch_exception
    def dl_qy_uncertified_locked(self, user_name, password, pic_id, is_login=0):
        """
        企业未认证vip下载锁号
        :param user_name:
        :param password:
        :param pic_id:
        :param is_login:
        :return:
        """
        # 判读是否需要登录
        if is_login == 1:
            # 登录
            if not self.user_login(user_name, password):
                return False
            time.sleep(1)
        else:
            self.driver.get('https://www.58pic.com/index.php?m=HelpCenter&a=addQuestion')
            time.sleep(1)
        import datetime
        date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        url = 'https://dl.58pic.com/%s.html?dlNumsAll=101&dlNumsToday=10&last_dl_time=%s:00&is_auto=0' % (pic_id, date)
        self.driver.get(url)
        time.sleep(1)
        # 获取检测文字
        check_word = self.driver.find_element_by_xpath('//*[@class="freq-popup"]').get_attribute('textContent')
        # 判断是否进入下载成功页
        if '帐号锁定！请完成认证' in check_word:
            return True
        return False

if __name__ == '__main__':
    driver = browser()
    f = DLAutomatedTest(driver)
    print(f.dl_qy_certified_limit('xztest25', '123456', '35772128', is_login=1))

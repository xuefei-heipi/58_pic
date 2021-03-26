from pic_project.common.commonfun import CommonFunction
from pic_project.common.driver import browser
import time
import re

#下载页xpath定位
position = '/html/body/div[3]/div[3]/p[2]'
position_zk = '/html/body/div[3]/div[2]/div/div[2]/p'


class DLAutomatedTest(CommonFunction):

    @CommonFunction.catch_exception
    def dl_no_jx_vip(self, user_name, password, pic_id):
        '''
        无精选vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)    #登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_jc_vip_1(self, user_name, password, pic_id):
        '''
        无基础vip一次免费
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'sc')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '作品下载' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_jc_vip_0(self, user_name, password, pic_id):
        '''
        无基础vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 1, 'sc')
        time.sleep(1)
        #self.driver.get('https://dl.58pic.com/34651443.html')   #除去免费一次
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_bg_vip(self, user_name, password, pic_id):
        '''
        无办公vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        #self.driver.get('https://dl.58pic.com/32822153.html')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_zk_vip_1(self, user_name, password, pic_id):
        '''
        无字库vip一次免费
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '作品下载' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_no_zk_vip_0(self, user_name, password, pic_id):
        '''
        无字库vip受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_jx_vip_20(self, user_name, password, pic_id):
        '''
        精选vip20次
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'yc')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        #获取精选次数
        num1= self.driver.find_element_by_xpath(position).text
        s = list(map(int, re.findall(r"\d+",num1)))[0]
        if '千图网-作品下载' in self.driver.title and s < 20:
            return True
        else:
            return False


    @CommonFunction.catch_exception
    def dl_restrict_jx_vip_20(self, user_name, password, pic_id):
        '''
        精选vip20次用完受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 20, 'yc')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_jc_vip_20(self, user_name, password, pic_id):
        '''
                基础vip20次
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'sc')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        # 获取基础次数
        num2 = self.driver.find_element_by_xpath(position).text
        s = list(map(int, re.findall(r"\d+", num2)))[0]
        if '千图网-作品下载' in self.driver.title and s < 20:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_jc_vip_20(self, user_name, password, pic_id):
        '''
        基础vip20次用完受限
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 20, 'sc')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_bg_vip_10(self, user_name, password, pic_id):
        '''
                办公vip10次
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'bg')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
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
        '''
                办公vip10次用完受限
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 10, 'bg')
        time.sleep(1)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_qy_vip_499(self, user_name, password, pic_id):
        '''
                企业vip499次
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
                '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 0, 'qy499')

        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
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
        '''
                企业vip499次用完受限
                :param user_name: 
                :param password: 
                :param pic_id: 
                :return: 
        '''
        self.user_login(user_name, password)  # 登录
        uid = self.get_user_cookies(user_name, password)
        self.change_user_vip_num_times(uid[1], 200, 'qy499')
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        # 悬浮到头像
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_zk_vip_20(self, user_name, password, pic_id):
        '''
        字库vip20次
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        num = self.driver.find_element_by_xpath(position).text
        s = list(map(int, re.findall(r"\d+", num)))[0]
        if s < 20:
            return True

        return False

    @CommonFunction.catch_exception
    def dl_restrict_zk_vip_20(self, user_name, password, pic_id):
        '''
        字库vip20次用完限制
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '千图网-下载受限' in self.driver.title:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_zk_vip_999(self, user_name, password, pic_id, pic_id2):
        '''
        字库vip999 20次授权下载
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        head = self.driver.title
        #print(head)
        url2 = 'https://dl.58pic.com/' + str(pic_id2) + '.html'
        self.driver.get(url2)
        head2 = self.driver.title
        #print(head2)
        if '千图网-作品下载' in  head and '千图网-下载受限' in head2:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_restrict_zk_vip_999(self, user_name, password, pic_id):
        '''
        字库vip999 20次授权下载用完
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)  # 登录
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        #/html/body/div[3]/div[2]/div/div[2]/p/i
        num = driver.find_element_by_xpath(position_zk).text
        print(num)
        s = list(map(int, re.findall(r"\d+", num)))[0]
        if '千图网-下载受限' in  self.driver.title and s == 0:
            return True
        else:
            return False

    @CommonFunction.catch_exception
    def dl_mf_wx(self,user_name, password, pic_id):
        '''
        免费无限下载国家、官方授权素材
        :param user_name: 
        :param password: 
        :param pic_id: 
        :return: 
        '''
        self.user_login(user_name, password)
        url = 'https://dl.58pic.com/' + str(pic_id) + '.html'
        self.driver.get(url)
        if '千图网-作品下载' in  self.driver.title:
            return True
        else:
            return False


if __name__ == '__main__':
    driver = browser()
    f = DLAutomatedTest(driver)
    print(f.dl_mf_wx('jxtest1', '123456', 34878067))
    #print(f.dl_no_jc_vip_0('jxtest1', '123456', 19515828))
    #print(f.dl_no_jc_vip_1('jxtest1', '123456', 23191179))
    #print(f.dl_jx_vip_20('jxtest', '123456', 34798744))
    #print(f.dl_restrict_jx_vip_20('jxtest', '123456', 34898619))
    #print(f.dl_jc_vip_20('jctest','123456',19515828))
    #print(f.dl_bg_vip_10('bgtest', '123456', 34686542 ))
    #print(f.dl_qy_vip_499('zktest4','123456',34802939))
    #print(f.dl_restrict_qy_vip_499('zktest4','123456',34878392))
    #print(f.dl_zk_vip_20('zktest3','123456',32822245))
    #print(f.dl_zk_vip_999('cstest17', '123456',32822232, 32837643 ))
    #print(f.dl_restrict_zk_vip_999('cstest17', '123456',32822121))
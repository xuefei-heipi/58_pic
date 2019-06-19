#!/usr/bin/env python3
from selenium.common.exceptions import NoSuchElementException
from time import  sleep
from pic.businessView.firestView.firstView import FirstView
from pic.common.driver import browser



class FirstViewCheck(FirstView):


    def check_first_floor_display(self,first_num=None, second_num=None):

        if first_num == 1:
            check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
            click_element = "点击设计创意下第" + str(second_num) + "个链接失败"
            element_name = "设计创意下第" + str(second_num) + "个链接"
        elif first_num == 2:
            check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
            click_element = "点击办公创意下第" + str(second_num) + "个链接失败"
            element_name = "办公创意下第" + str(second_num) + "个链接"
        elif first_num == 5:
            if second_num == 4:
                check_element_path = ".//*[@id='tool-header']/div/div[1]"  # 判断新句柄上 设计创意是否存在
            elif second_num == 5:
                check_element_path = "html/body/div[1]/div/div"  # 判断新句柄上 设计创意是否存在
            else:
                check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
            click_element = "点击...下第" + str(second_num) + "个链接失败"
            element_name = "...下第" + str(second_num) + "个链接"
        try:

            self.first_floor_display(first_num, second_num)

            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)   #判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)    #出错截屏
            return False


    def check_first_floor_nodisplay(self, first_num=None):

        if first_num == 3:
            check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
            click_element = "点击正版商用链接失败"
            element_name = "正版商用链接"
        elif first_num == 4:
            check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
            click_element = "点击创意趋势链接失败"
            element_name = "创意趋势链接"
        try:

            self.first_floor_nodisplay(first_num)

            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)   #判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)    #出错截屏
            return False

    def check_first_floor_VIP_chose(self, VIP_num=None):
        check_element_path = "html/body/div[4]/div/div[1]"  # 判断新句柄上 设计创意是否存在
        if VIP_num == 1:
            click_element = "点击共享VIP链接失败"
            element_name = "共享VIP链接"
        elif VIP_num == 2:
            click_element = "点击原创VIP链接失败"
            element_name = "原创VIP链接"
        elif VIP_num == 3:
            click_element = "点击办公VIP链接失败"
            element_name = "办公VIP链接"
        elif VIP_num == 4:
            click_element = "点击超级VIP链接失败"
            element_name = "超级VIP链接"
        elif VIP_num == 5:
            check_element_path = "html/body/div[5]/div[2]"  # 判断新句柄上 设计创意是否存在
            click_element = "点击企业VIP链接失败"
            element_name = "企业VIP链接"

        try:

            self.first_floor_VIP_chose(VIP_num)

            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)   #判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_first_floor_upload(self):
        check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
        click_element = "点击上传链接失败"
        element_name = "上传链接"

        try:

            self.first_floor_upload()
            all_h = self.driver.window_handles  # 获取所有句柄
            print(all_h)

            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)   #判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_first_floor_Login(self):
        check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
        click_element = "点击登录链接失败"
        element_name = "登录链接"
        try:
            self.first_floor_Login()

            result_check = self.checkFirstViewClickNoHandles(check_element_path, element_name)   #判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_first_floor_register(self):
        check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
        click_element = "点击注册链接失败"
        element_name = "注册链接"
        try:
            self.first_floor_register()

            result_check = self.checkFirstViewClickNoHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_classify(self, classify_list_num=None):
        check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在
        if classify_list_num == 1:
            click_element = "点击平面广告链接失败"
            element_name = "平面广告链接"
        elif classify_list_num == 2:
            click_element = "点击电商淘宝链接失败"
            element_name = "电商淘宝链接"
        elif classify_list_num == 3:
            click_element = "点击装饰装修链接失败"
            element_name = "装饰装修链接"
        elif classify_list_num == 4:
            click_element = "点击网页UI链接失败"
            element_name = "网页UI链接"
        elif classify_list_num == 5:
            click_element = "点击视频音效链接失败"
            element_name = "视频音效链接"
        elif classify_list_num == 6:
            click_element = "点击产品工业链接失败"
            element_name = "产品工业链接"
        elif classify_list_num == 7:
            click_element = "点击高清图库链接失败"
            element_name = "高清图库链接"
        elif classify_list_num == 8:
            click_element = "点击背景链接失败"
            element_name = "背景链接"
        elif classify_list_num == 9:
            click_element = "点击设计元素链接失败"
            element_name = "设计元素链接"
        elif classify_list_num == 10:
            click_element = "点击手机用图链接失败"
            element_name = "手机用图链接"
        elif classify_list_num == 11:
            click_element = "点击插画绘画链接失败"
            element_name = "插画绘画链接"
        elif classify_list_num == 12:
            click_element = "点击PPT模板链接失败"
            element_name = "PPT模板链接"
        elif classify_list_num == 13:
            click_element = "点击Excel模板链接失败"
            element_name = "Excel模板链接"
        elif classify_list_num == 14:
            click_element = "点击文库模板链接失败"
            element_name = "文库模板链接"
        elif classify_list_num == 15:
            click_element = "点击简历模板链接失败"
            element_name = "简历模板链接"
        elif classify_list_num == 16:
            click_element = "点击Word范文链接失败"
            element_name = "Word范文链接"
        elif classify_list_num == 17:
            click_element = "点击云简历链接失败"
            element_name = "云简历链接"

        try:
            self.second_floor_classify(classify_list_num)

            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_classify_p(self, classify_list_num=None, list_sublist_num=None):
        check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在

        try:
            describe = self.second_floor_classify_p(classify_list_num, list_sublist_num) #获取返回值
            click_element = "点击"+ describe +"链接失败"
            element_name =  describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_classify_div(self, classify_list_num=None, list_sublist_num=None, list_request_num=None):
        check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在

        try:
            describe = self.second_floor_classify_div(classify_list_num, list_sublist_num, list_request_num) #获取返回值
            click_element = "点击"+ describe +"链接失败"
            element_name =  describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_search(self, input_search_request=None):
        check_element_path = "html/body/div[4]/div/div[1]/span"  # 判断新句柄上 设计创意是否存在

        try:
            self.second_floor_search(input_search_request)
            click_element = "搜索"+ input_search_request +"功能失败"
            element_name =  input_search_request + "搜索"
            result_check = self.checkFirstViewClickNoHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_ranking_list(self):
        check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在

        try:
            describe = self.second_floor_ranking_list() #获取返回值
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_points_mall(self):
        check_element_path = "html/body/div[1]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在

        try:
            describe = self.second_floor_points_mall() #获取返回值
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_second_floor_popular_searches(self, popular_search_num=None):
        check_element_path = "html/body/div[2]/div/div[2]/div[4]"  # 判断新句柄上 设计创意是否存在

        try:
            describe = self.second_floor_popular_searches(popular_search_num) #获取返回值
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_third_floor_image_switch(self, chose_element_num=None):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在
        try:
            describe = self.third_floor_image_switch(chose_element_num) #获取返回值
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_fourth_main_link(self, main_link_num=None):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在

        try:
            results = self.fourth_main_link(main_link_num)
            describe = results[0]
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            if results[1] == True:  #可以打开新窗口
                result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
                return result_check
            else:
                if results[2] == True:
                    result_check = self.checkFirstViewClickNoHandles(check_element_path, element_name)  # 判断元素是否存在
                    return result_check
                else:
                    self.getScreenShot(click_element)  # 出错截屏
                    return False
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_fourth_secondary_link(self, secondary_link_num=None, request_link_num=None):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在
        try:
            describe = self.fourth_secondary_link(secondary_link_num, request_link_num) #获取返回值
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_fourth_more_link(self, more_link_num):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在
        try:
            self.fourth_more_link(more_link_num) #获取返回值
            click_element = "点击第"+str(more_link_num)+"个更多链接失败"
            element_name = "第"+str(more_link_num)+"个更多链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_fourth_ad_link(self, ad_num):
        check_element_path = "html/body/div[3]"  # 判断新句柄上 元素是否存在
        try:
            self.fourth_ad_link(ad_num)
            click_element = "点击第" + str(ad_num) + "个广告链接失败"
            element_name = "第" + str(ad_num) + "个广告链接"
            result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_fourth_image_link(self, floor_num=None, image_num=None):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在
        try:
            describe = self.fourth_image_link(floor_num, image_num)  # 获取返回值
            all_h = self.driver.window_handles
            print(all_h)
            click_element = "点击" + describe + "链接失败"
            element_name = describe + "链接"
            if floor_num == 1:

                result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
                return result_check
            else:
                result_check = self.checkImageLink(element_name)
                print(result_check)
                if describe == result_check:
                    return True
                else:
                    self.getScreenShot(element_name)
                    return False
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_fourth_image_download(self, floor_num=None, image_num=None):
        check_element_path = "html/body/div[5]/div[4]/div[4]/div[3]" \
                             "/div[3]/div[3]/div[3]/div[4]/div[8]/div/div/div/div[1]"  # 判断新句柄上 元素是否存在
        try:
            describe = self.fourth_image_download(floor_num, image_num)  # 获取返回值
            click_element = "点击" + describe + "下载链接失败"
            element_name = describe + "下载链接"
            result_check = self.checkLoginAlert(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_last_floor_link(self, column_num=None, request_num=None):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在
        try:
            describe = self.last_floor_link(column_num, request_num)  # 获取返回值
            click_element = "点击" + describe + "下载链接失败"
            element_name = describe + "下载链接"
            # print(click_element,element_name)
            if request_num == 6:
                result_check = self.checkFirstViewClickNoHandles(check_element_path, element_name)
            elif column_num == 5 and request_num == 2:
                if len(self.driver.window_handles) < 2:
                    self.getScreenShot(element_name)
                    return False
                else:
                    return True
            else:
                result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

    def check_right_suspend_sign(self, suspend_num=None, request_num=None):
        check_element_path = "html/body/div[2]"  # 判断新句柄上 元素是否存在
        try:
            describe = self.right_suspend_sign(suspend_num, request_num)  # 获取返回值
            click_element = "点击" + describe + "下载链接失败"
            element_name = describe + "下载链接"
            if suspend_num == 2 and request_num == 1:
                if len(self.driver.window_handles) < 2:
                    self.getScreenShot(element_name)
                    return False
                else:
                    return True
            if request_num == 3:
                result_check = self.checkLoginAlert(check_element_path, element_name)  # 判断元素是否存在
            else:
                result_check = self.checkFirstViewClickHasHandles(check_element_path, element_name)  # 判断元素是否存在
            return result_check
        except NoSuchElementException:
            self.getScreenShot(click_element)  # 出错截屏
            return False

if __name__ == '__main__':
    # for y in range(1,11):

    driver = browser()
    driver.get("http://www.58pic.com/")
    f = FirstViewCheck(driver)
    f.skipActivity()

    result = f.check_fourth_image_download(6,2)
    # f.getScreenShot('更多>>下载链接')
    print(result)
    f.driver.quit()


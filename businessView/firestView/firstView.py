# coding=utf-8
from time import sleep, ctime

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pic.common.commomFun import Common
from pic.common.driver import browser
from pic.common.getPath import GetPath
from selenium import webdriver
from pic.baseView.baseView import BaseView
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstView(Common):

    first_floor_path=".//div[@class='qt-header']"
    second_floor_path=".//div[@class='qt-search-index']"
    third_floor_path=".//div[@class='outcolor']"
    fourth_floor_path=".//div[@class='index-main']"

    def first_floor_display(self, first_num=None, second_num=None):   #第一层有display项的 如:设计创意 办公创意 ...
        try:
            elements_path = GetPath().get_first_floor_display_path(first_num, second_num)
            display_element_path=elements_path[0]
            request_element_path=elements_path[1]

            self.mouseAbove(display_element_path) #鼠标悬浮
            element = self.dominantWait(request_element_path)  #显性等待5秒,等待元素出现

            element.click()
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def first_floor_nodisplay(self, first_num=None): #第一层无display 如: 正版商用 创意趋势
        try:
            no_display_element_path = GetPath().get_first_floor_nodisplay_path(first_num)
            self.driver.find_element_by_xpath(no_display_element_path).click()
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def first_floor_VIP_chose(self, VIP_num=None):    #VIP选择
        try:
            elements_path = GetPath().get_first_floor_VIP_path(VIP_num)
            self.mouseAbove(elements_path[0])   #鼠标悬浮

            element = self.dominantWait(elements_path[1])  #显示等待5秒,等待元素出现
            element.click()
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def first_floor_upload(self):   #上传
        try:
            upload_element_path = GetPath().get_first_floor_upload_path()
            # upload_element_path = 'html/body/div[2]/div/div[2]/div[2]/p[1]'
            # print(upload_element_path)

            self.mouseAbove(upload_element_path)
            self.xpath_find(upload_element_path).click()  #普通点击
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def first_floor_Login(self):    #登录
        try:
            Login_element_path = GetPath().get_first_floor_Login_path()
            self.driver.find_element_by_xpath(Login_element_path).click()  #普通点击
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def first_floor_register(self):    #注册
        try:
            register_element_path = GetPath().get_first_floor_register_path()
            self.driver.find_element_by_xpath(register_element_path).click()  #普通点击
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_classify(self, classify_list_num=None): #分类一层
        try:
            elements_path = GetPath().get_second_floor_classify_path(classify_list_num)

            self.driver.find_element_by_xpath(elements_path[0]).click()  # 普通点击
            self.driver.find_element_by_xpath(elements_path[1]).click()  # 普通点击
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_classify_p(self, classify_list_num=None, list_sublist_num=None): #分类二层
        try:
            elements_path = GetPath().get_second_floor_classify_p_path(classify_list_num, list_sublist_num)
            self.driver.find_element_by_xpath(elements_path[0]).click()  # 普通点击

            self.mouseAbove(elements_path[1])  # 鼠标悬浮

            # print(str(self.driver.find_element_by_xpath(elements_path[2]).text))
            describe = str(self.driver.find_element_by_xpath(elements_path[2]).text).split("\n") #获取需要点击的链接文字描述
            print(describe[0])

            element = self.dominantWait(elements_path[2]) # 显示等待5秒,等待元素出现
            element.click()
            sleep(1)
            return describe[0]
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_classify_div(self, classify_list_num=None, list_sublist_num=None, list_request_num=None): #分类三层
        try:
            elements_path = GetPath().get_second_floor_classify_div_path(classify_list_num, list_sublist_num, list_request_num)

            self.driver.find_element_by_xpath(elements_path[0]).click()  # 普通点击

            self.mouseAbove(elements_path[1])  # 鼠标悬浮

            describe = str(self.driver.find_element_by_xpath(elements_path[2]).text).split("\n")  # 获取需要点击的链接文字描述
            print(describe[0])
            element = self.dominantWait(elements_path[2])  # 显示等待5秒,等待元素出现
            element.click()
            sleep(1)
            return describe[0]
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_search(self, input_search_request=None):   #搜索功能
        try:
            elements_path = GetPath().get_second_floor_search_path()

            self.driver.find_element_by_xpath(elements_path[0]).send_keys(input_search_request)  #输入需要查找的内容
            self.driver.find_element_by_xpath(elements_path[1]).click()  #点击搜索按钮

            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_ranking_list(self):    #排行榜
        try:
            ranking_list_path=self.second_floor_path+"//div//div[3]//a[1]"
            describe = self.driver.find_element_by_xpath(ranking_list_path+"//img").get_attribute("alt")  # 获取需要点击的链接文字描述
            self.driver.find_element_by_xpath(ranking_list_path).click()  # 普通点击
            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_points_mall(self): #积分商城
        try:
            points_mall_path=self.second_floor_path+"//div//div[3]//a[2]"
            describe = self.driver.find_element_by_xpath(points_mall_path + "//img").get_attribute("alt")  # 获取需要点击的链接文字描述
            self.driver.find_element_by_xpath(points_mall_path).click()  # 普通点击
            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")

    def second_floor_popular_searches(self, popular_search_num=None):    #热门搜索
        try:
            popular_search_path=self.second_floor_path+"//div//div[2]//a["+str(popular_search_num)+"]"
            describe = str(self.driver.find_element_by_xpath(popular_search_path).text)  # 获取需要点击的链接文字描述
            self.driver.find_element_by_xpath(popular_search_path).click()  # 普通点击
            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")

    def third_floor_image_switch(self, chose_element_num=None):  #图片切换层
        try:
            chose_element_path=self.third_floor_path+"//div//div[2]//div//a["+str(chose_element_num)+"]"
            request_element_path=self.third_floor_path+"//div//div[1]//div["+str(chose_element_num)+"]"
            self.driver.find_element_by_xpath(chose_element_path).click() #点击选择需要的链接图片
            describe = self.driver.find_element_by_xpath(request_element_path + "//a").get_attribute("title")  # 获取需要点击的链接文字描述
            print(describe)
            self.driver.find_element_by_xpath(request_element_path).click() #点击链接图片
            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")

    def fourth_main_link(self, main_link_num=None): #精选收藏夹 商用海报 等
        try:
            main_link_path = GetPath().get_fourth_main_link_path(main_link_num)
            is_open_new_window = self.driver.find_element_by_xpath(main_link_path).get_attribute(
                "target")  # 链接是否打开新窗口
            if is_open_new_window == "_blank":
                open = True
            else:
                open = False

            describe = str(self.driver.find_element_by_xpath(main_link_path).text) #获取元素名称
            first_url = self.driver.current_url
            self.driver.find_element_by_xpath(main_link_path).click()
            current_url = self.driver.current_url
            click_check = True
            if open == False:
                if first_url == current_url:
                    click_check = False
                else:
                    click_check = True
            sleep(1)
            return describe, open, click_check
        except:
            self.getScreenShot("界面元素未加载")

    def fourth_secondary_link(self, secondary_link_num=None, request_link_num=None):  #二十四节气 明星设计师 手机配图 夏天 等
        try:
            secondary_link_path = GetPath().get_fourth_secondary_link_path(secondary_link_num, request_link_num)
            describe = str(self.driver.find_element_by_xpath(secondary_link_path).text) #获取元素名称
            self.driver.find_element_by_xpath(secondary_link_path).click()
            print(describe)
            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")

    def fourth_more_link(self, more_link_num=None):  #主界面上的 更多
        try:
            more_link_path = GetPath().get_fourth_more_link_path(more_link_num)
            self.driver.find_element_by_xpath(more_link_path).click()
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def fourth_ad_link(self,ad_num):   #广告位点击
        try:
            ad_path="html/body/div[5]/div[4]/div[2]/a["+str(ad_num)+"]/img"
            self.driver.find_element_by_xpath(ad_path).click()
            sleep(1)
        except:
            self.getScreenShot("界面元素未加载")

    def fourth_image_link(self, floor_num=None, image_num=None):
        describe = ""
        try:
            if floor_num == 1:
                image_element_path=self.fourth_floor_path+"//div[2]//div["+str(image_num)+"]//a//div[2]"
                self.mouseAbove(image_element_path)
                sleep(1)
                describe = str(self.driver.find_element_by_xpath(image_element_path + "//p//span").text)    #获取元素名称

            elif floor_num == 2:
                stitching_path = "//div[4]//div//div//div//div"
                image_element_path=self.fourth_floor_path+ stitching_path +"//div["+str(image_num)+"]//div//a"
                describe_path = self.fourth_floor_path+ stitching_path + "//div[" + str(image_num) + "]//p"

                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)


            elif floor_num == 3:
                image_element_path=self.fourth_floor_path+"//div[4]//div[4]//div//div//div//div//div" \
                                                          "["+str(image_num)+"]//div//a"

                sleep(1)
                describe_path = self.fourth_floor_path + "//div[4]//div[4]//div//div//div//div//div" \
                                                         "[" + str(image_num) + "]//p"
                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)

            elif floor_num == 4:
                stitching_path = "//div[4]//div[4]//div[3]//div//div"
                image_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"
                describe_path = self.fourth_floor_path + stitching_path + "//div//div//div["+str(image_num)+"]//p"
                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)


            elif floor_num == 5:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div//div"
                image_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"
                describe_path = self.fourth_floor_path + stitching_path + "//div//div//div[" + str(image_num) + "]//p"

                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)


            elif floor_num == 6:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div"
                image_element_path=self.fourth_floor_path+ stitching_path +"//div//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"
                describe_path = self.fourth_floor_path + stitching_path + "//div//div//div//div[" + str(image_num) + "]//p"
                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)

            elif floor_num == 7:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div"
                image_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"
                describe_path = self.fourth_floor_path + stitching_path + "//div//div//div//div[" + str(image_num) + "]//p"
                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)


            elif floor_num == 8:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[2]//div[2]//div"
                # image_roll_next_num=[4,5,6,10,11,12]
                # image_roll_first_view_num=[1,2,3,7,8,9]
                image_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"
                describe_path = self.fourth_floor_path + stitching_path + "//div//div//div//div[" + str(image_num) + "]//p"
                self.findElementByJs(image_element_path)

                describe = str(self.driver.find_element_by_xpath(describe_path).text)
                self.mouseAbove(image_element_path)
                print(describe)

            elif floor_num == 9:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[4]//div//div"
                image_element_path=self.fourth_floor_path+ stitching_path + "//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"

                describe_path = self.fourth_floor_path + stitching_path + "//div//div/div[" + str(image_num) + "]//p"
                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)

            elif floor_num == 10:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[4]//div[3]//div//div"
                image_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//div//a"

                describe_path = self.fourth_floor_path + stitching_path + "//div//div/div[" + str(image_num) + "]//p"
                self.findElementByJs(image_element_path)
                describe = str(self.driver.find_element_by_xpath(describe_path).text)
            print(image_element_path)
            self.driver.find_element_by_xpath(image_element_path).click()
            sleep(5)
            return describe
        except Exception as ES:
            print(ES)
            self.getScreenShot("界面元素未加载")

    def fourth_image_download(self, floor_num=None, image_num=None):
        describe = ""
        try:
            floor_num = floor_num + 1

            if floor_num == 2:
                stitching_path = "//div[4]//div//div//div//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path +\
                                            "//div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path + stitching_path + "//div[" + str(image_num) + "]//p"
                image_element_path = self.fourth_floor_path + stitching_path + "//div[" + str(image_num) + "]//div//a//img"
                # if image_num <= 4:
                #     if image_num == 4:  # 当定位第四个时,鼠标可能挡在前面 需要先移开
                #         self.mouseAbove("html/body/div[5]")
                #     describe = str(self.driver.find_element_by_xpath(describe_path).text)
                #
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path +"//div[4]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #
                #     roll_next_path=self.fourth_floor_path+"//div[4]//div//div//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = str(self.driver.find_element_by_xpath(describe_path).text)
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div[" + str(
                #     image_num) + "]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)



            elif floor_num == 3:
                image_download_element_path=self.fourth_floor_path+"//div[4]//div[4]//div//div//div//div//" \
                                                                   "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+"//div[4]//div[4]//div//div//div//div//" \
                                                                   "div["+str(image_num)+"]//p"
                image_element_path = self.fourth_floor_path + "//div[4]//div[4]//div//div//div//div//div" \
                                                              "[" + str(image_num) + "]//div//a//img"


                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)   #获取描述
                #
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+"//div[4]//div//div//div//div//div//div[4]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #
                #     roll_next_path=self.fourth_floor_path+"//div[4]//div[4]//div//div//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)   #获取描述
                #     sleep(1)
                # test_element_path = self.fourth_floor_path + "//div[4]//div//div//div//div//div//div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                sleep(1)

            elif floor_num == 4:
                stitching_path = "//div[4]//div[4]//div[3]//div//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//p"
                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a//img"
                describe_path = self.fourth_floor_path + stitching_path + "//div//div//div[" + str(image_num) + "]//p"

                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)  # 获取描述
                #
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                #                                           "div[4]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #
                #     roll_next_path=self.fourth_floor_path+ stitching_path +"//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)

            elif floor_num == 5:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//p"

                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a//img"
                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)  # 获取描述
                #
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                #                                           "div[4]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #
                #     roll_next_path=self.fourth_floor_path+ stitching_path +"//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)

            elif floor_num == 6:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path +"//div//div//div//" \
                                                          "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+ stitching_path +"//div//div//div//" \
                                                          "div["+str(image_num)+"]//p"
                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a//img"
                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)  # 获取描述
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                #                                           "div[4]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #
                #     roll_next_path=self.fourth_floor_path+ stitching_path + "//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)

            elif floor_num == 7:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                                                          "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                                                          "div["+str(image_num)+"]//p"
                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a//img"

                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)  # 获取描述
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                #                                           "div[4]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #
                #     roll_next_path=self.fourth_floor_path+ stitching_path + "//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                #
                # sleep(1)

            elif floor_num == 8:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[2]//div[2]//div"
                # image_roll_next_num=[4,5,6,10,11,12]
                # image_roll_first_view_num = [1, 2, 3, 7, 8, 9]
                image_download_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                                                          "div["+str(image_num)+"]//div//div[@class='card-handle']//div//span"

                describe_path = self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                                                          "div["+str(image_num)+"]//p"

                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a"

                # if image_num in image_roll_first_view_num:
                #     describe = self.getTagText(describe_path)  # 获取描述
                #
                #
                # if image_num in image_roll_next_num:
                #     test_element_path=self.fourth_floor_path+ stitching_path + "//div//div//div//" \
                #                                           "div[3]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #     roll_next_path=self.fourth_floor_path+ stitching_path + "//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)

            elif floor_num == 9:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[4]//div//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path + "//div//div//" \
                                                          "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+ stitching_path + "//div//div//" \
                                                          "div["+str(image_num)+"]//p"
                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a//img"
                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)  # 获取描述
                #
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path + "//div//div//" \
                #                                           "div[3]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #     roll_next_path=self.fourth_floor_path+ stitching_path + "//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)

            elif floor_num == 10:
                stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[4]//div[3]//div//div"
                image_download_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//div//a//div[@class='card-handle']//div//span"
                describe_path = self.fourth_floor_path+ stitching_path +"//div//div//" \
                                                          "div["+str(image_num)+"]//p"
                image_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                                                                               "div[" + str(image_num) + "]//div//a//img"
                # if image_num <= 4:
                #     describe = self.getTagText(describe_path)  # 获取描述
                #
                # if image_num > 4:
                #     test_element_path=self.fourth_floor_path+ stitching_path +"//div//div//" \
                #                                           "div[3]//div//a//img"    #将鼠标悬浮在对应图片上,界面会显示roll-next按键
                #     self.mouseAbove(test_element_path)
                #     sleep(1)
                #     roll_next_path=self.fourth_floor_path+ stitching_path + "//div[@class='roll-next']" #将鼠标悬浮在roll-next标签上
                #     self.mouseAbove(roll_next_path)
                #     describe = self.getTagText(describe_path)  # 获取描述
                #     sleep(1)
                #
                # test_element_path = self.fourth_floor_path + stitching_path + "//div//div//" \
                #                                                               "div["+str(image_num)+"]//div//a//img"  # 将鼠标悬浮在对应图片上,界面会显示roll-next按键
                # self.mouseAbove(test_element_path)
                # sleep(1)
            # print(111)
            self.findElementByJs(image_element_path)
            # print(122)
            describe = self.getTagText(describe_path)
            self.mouseAbove(image_element_path)
            # print(133)

            sleep(1)
            self.driver.find_element_by_xpath(image_download_element_path).click()
            sleep(1)
            return describe
        except Exception as ES:
            print(ES)
            self.getScreenShot("界面元素未加载")


    def last_floor_link(self, column_num=None, request_num=None): #最下面一层链接 常见问题 关于千图网 产品服务 等
        last_floor_path=self.fourth_floor_path+"//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[4]//div[5]"

        try:
            if column_num > 4:
                request_num = request_num + 2
                element_path = last_floor_path + "//div//div//div//p[" + str(request_num) + "]//a"
                describe_path = element_path
                describe = self.getTagText(describe_path)  # 获取描述
            else:
                element_path=last_floor_path+"//div//div//dl["+str(column_num)+"]//dd["+str(request_num)+"]//a"
                describe_path = element_path
                describe = self.getTagText(describe_path)  # 获取描述


            self.driver.find_element_by_xpath(element_path).click()
            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")


    def right_suspend_sign(self, suspend_num=None, request_num=None): #右侧悬浮签到 客服 窗口
        stitching_path="//div[4]//div[4]//div[3]//div[3]//div[3]//div[3]//div[4]//div[14]"
        element_path = self.fourth_floor_path+ stitching_path + "//a["+str(suspend_num)+"]//i"  #窗口路径

        try:
            if suspend_num ==1 or suspend_num == 2:
                self.mouseAbove(element_path)
                sleep(1)
                if suspend_num == 1:
                    if request_num == 1:
                        describe_path = self.fourth_floor_path + stitching_path + "//ul[2]//a["+str(request_num)+"]//em"

                        describe = self.getTagText(describe_path)  # 获取描述
                        request_element_path = self.fourth_floor_path + stitching_path + "//ul[2]//a["+str(request_num)+"]//i"
                    elif request_num == 2:
                        describe_path = self.fourth_floor_path + stitching_path + "//ul[2]//a[" + str(request_num) + "]"

                        describe = self.getTagText(describe_path)  # 获取描述
                        request_element_path = self.fourth_floor_path + stitching_path + "//ul[2]//a[" + str(
                            request_num) + "]//i"

                    else:
                        describe_path = "html/body/div[5]/div[4]/div[4]/div[3]/div[3]/div[3]/div[3]/div[4]/div[14]/a[1]"

                        describe = self.getTagText(describe_path)  # 获取描述
                        request_element_path = "html/body/div[5]/div[4]/div[4]/div[3]/div[3]/div[3]/div[3]/div[4]/div[14]/a[1]/i"   #签到
                    self.driver.find_element_by_xpath(request_element_path).click()
                else:
                    describe_path = self.fourth_floor_path + stitching_path + "//ul[3]//p[1]/a"
                    describe = self.getTagText(describe_path)  # 获取描述

                    request_element_path = self.fourth_floor_path + stitching_path + "//ul[3]//p[1]/a"
                    self.driver.find_element_by_xpath(request_element_path).click()
            else:
                describe_path = self.fourth_floor_path+ stitching_path + "//a["+str(suspend_num)+"]"
                describe = self.getTagText(describe_path)  # 获取描述
                self.driver.find_element_by_xpath(element_path).click()

            sleep(1)
            return describe
        except:
            self.getScreenShot("界面元素未加载")






def test_commom():
    driver = browser()
    driver.maximize_window()
    driver.implicitly_wait(10)
    f = FirstView(driver)
    f.driver.get("http://www.58pic.com")
    f.driver.maximize_window()
    f.driver.implicitly_wait(10)

    VIP_element_path = "html/body/div[5]/div[4]/div[4]/div[3]/div[3]/div[3]/div[3]/div[4]/div[6]/a[1]"
    try:
        f.driver.find_element_by_xpath(VIP_element_path).click()
        return f
    except NoSuchElementException:
        pass
        return f

if __name__ == '__main__':
    # options = webdriver.FirefoxProfile()
    # options.add_extension('-headless')
    # driver = webdriver.Firefox(options=options)
    driver = browser()
    driver.get('http://www.58pic.com')
    f = FirstView(driver)
    f.skipActivity()
    f.first_floor_upload()


    #first_floor_dispaly

    # for x in range(1,6):
    #     f = test_commom()
    #     if x==3 or x==4:
    #         f.first_floor_nodisplay(x)
    #     else:
    #         f.first_floor_display(x,1)
    #     f.driver.quit()


    #first_floor_VIP
    '''
    for x in range(1,6):
        driver = browser()
        driver.maximize_window()
        driver.implicitly_wait(10)
        f = FirstView(driver)
        f.driver.get("http://www.58pic.com")
        f.driver.maximize_window()
        f.driver.implicitly_wait(10)
        f.first_floor_VIP_chose(x)
        f.driver.quit()
    '''

    #first_floor_upload
    '''
    driver = browser()
    driver.maximize_window()
    driver.implicitly_wait(10)
    f = FirstView(driver)
    f.driver.get("http://www.58pic.com")
    f.driver.maximize_window()
    f.driver.implicitly_wait(10)
    f.first_floor_upload()
    f.driver.quit()
    '''

    #first_floor_Login and register

    # f=test_commom()
    # f.first_floor_Login()
    # f.driver.quit()
    #
    # f = test_commom()
    # f.first_floor_register()
    # f.driver.quit()


    #second_floor_classify
    # for x in range(1,18):
    #     print(x)
    #     f = test_commom()
    #     f.second_floor_classify(x)
    #     f.driver.quit()

    #second_floor_search
    # f = test_commom()
    # f.second_floor_search("地球")
    # f.driver.quit()

    #second_floor_ranking_list
    # f = test_commom()
    # f.second_floor_ranking_list()
    # f.driver.quit()

    #second_floor_points_mall
    # f = test_commom()
    # f.second_floor_points_mall()
    # f.driver.quit()

    #second_floor_popular_searches
    # for x in range(1,11):
    #     f = test_commom()
    #     f.second_floor_popular_searches(x)
    #     f.driver.quit()

    #third_floor_image_switch
    # for x in range(1,9):
    #     f = test_commom()
    #     f.third_floor_image_switch(x)
    #     f.driver.quit()

    #fourth_main_link
    # f = test_commom()
    # des = f.fourth_main_link(2)
    # print(des)
    # if des[1] == True:
    #     print(1)
    # else:
    #     print(2)
    # sleep(2)
    # f.driver.quit()
    # for x in range(1,11):
    #     f = test_commom()
    #     f.fourth_main_link(x)
    #     sleep(1)
    #     f.driver.quit()

    # fourth_secondary_link
    # for x in range(1,11):
    #     f = test_commom()
    #     f.fourth_secondary_link(x,1)
    #     sleep(1)
    #     f.driver.quit()

    # fourth_more_link
    # print(ctime())
    # for x in range(1, 11):
    #     print(x)
    #     f = test_commom()
    #     f.fourth_more_link(x)
    #     sleep(1)
    #     f.driver.quit()
    # print(ctime())

    # fourth_ad_link
    # for x in range(2, 3):
    #     print(x)
    #     f = test_commom()
    #     f.fourth_ad_link(x)
    #     sleep(1)
    # f.driver.quit()

    # fourth_image_link
    # for x in range(1, 9):
    #     print(x)
    #     f = test_commom()
    #     f.fourth_image_link(10,x)
    #     sleep(1)
    #     f.driver.quit()

    # last_floor_link
    # list=[5,5,2,6,2]
    # for x in range(0,4):
    #     for y in range(1,list[x]+1):
    #         f = test_commom()
    #         f.last_floor_link(x+1,y)
    #         f.driver.quit()
    # for x in range(1,3):
    #     print(x)
    #     f = test_commom()
    #     f.last_floor_link(1,x)
    #     sleep(1)
    #     f.driver.quit()

    # fourth_image_download
    # for y in range(7,10):
    #     print(y)
    #     for x in range(1,9):
    #         print(x)
    # f = test_commom()
    # f.fourth_image_download(1,1)
    # f.driver.quit()

    # right_suspend_sign
    # f = test_commom()
    # f.right_suspend_sign(1,3)
    #
    # f.driver.quit()




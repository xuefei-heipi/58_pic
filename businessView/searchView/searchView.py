#!/usr/bin/env python3

from pic.businessView.firestView.firstView import FirstView
from pic.common.driver import browser
from time import sleep


class SearchView(FirstView):

    search_base_path = "html/body/div[4]/div/div[5]/div/div[3]/div"

    search_result_path = "html/body/div[4]/div/div[1]/em"

    second_image_describe_path = "html/body/div[4]/div/div[5]/div/div[3]/div/div[2]/p/span[2]"  #页面上第二个图片的描述 路径
    second_image_path = "html/body/div[4]/div/div[5]/div/div[3]/div/div[2]/div/a/div[3]"  #页面上第二个图片 路径

    #上面跳转路径
    page_num_path = "html/body/div[4]/div/div[5]/div/div[1]/div[3]/div/span/em" #   翻页 尖号 左边的页数 数字 路径 (上面)
    page_next_path = "html/body/div[4]/div/div[5]/div/div[1]/div[3]/div/a[2]"   #   翻页 右尖号  路径
    page_back_path = "html/body/div[4]/div/div[5]/div/div[1]/div[3]/div/a[1]"   #   翻页 左尖号  路径

    #下面跳转路径
    page_skip_fourth_num_btn_path = "html/body/div[4]/div/div[7]/b/a[3]"    # 页面跳转 第4个数字 路径
    page_skip_next_path = "html/body/div[4]/div/div[7]/a[2]"    # 页面跳转页 下一页
    page_skip_back_path = "html/body/div[4]/div/div[7]/b/a[1]"  # 页面跳转页 上一页
    page_skip_num_path = "html/body/div[4]/div/div[7]/input"    # 页面跳转页 数字
    page_skip_btn_path = "html/body/div[4]/div/div[7]/a[3]"    # 页面跳转页 数字

    search_down_ad_path = "html/body/div[4]/div/a/img"   #页面 下部广告路径


    def search_main(self,search_input):     #搜索 主接口
        self.second_floor_search(search_input)  #在主页执行搜索进入搜索页
        self.skipSearchGuide() #跳过新手指导


    def search_qq_login(self, search_input):    #用社交账号直接登录  handles = 1
        describe = "qq登录"
        try:
            self.search_main(search_input)
            qq_login_path = "html/body/div[3]/div/ul/li[2]/a[1]"
            self.xpath_find(qq_login_path).click()
            return  describe
        except :
            self.getScreenShot(describe)
            return False


    def search_wx_login(self, search_input):    #用社交账号直接登录  handles = 1
        describe = "微信登录"
        try:
            self.search_main(search_input)
            wx_login_path = "html/body/div[3]/div/ul/li[2]/a[2]"
            self.xpath_find(wx_login_path).click()
            return  describe
        except:
            self.getScreenShot(describe)
            return False

    def search_wb_login(self, search_input):    #用社交账号直接登录  handles = 1
        describe = "微博登录"
        try:
            self.search_main(search_input)
            wb_login_path = "html/body/div[3]/div/ul/li[2]/a[3]"
            self.xpath_find(wb_login_path).click()
            return  describe
        except:
            self.getScreenShot(describe)
            return False

    #分类
    def search_classify(self, search_input, classify_first_num=None,classify_second_num=None, classify_third_num=None):
        describe = ""
        try:
            self.search_main(search_input)
            classify_first_num += 1
            classify_second_num += 1
            classify_third_num += 1
            classify_first_path = ".//*[@id='industry_key']/li["+ str(classify_first_num) +"]/a"
            classify_second_path = ".//*[@id='industry_key']/li["+ str(classify_second_num) +"]/a"
            classify_third_path = ".//*[@id='industry_key']/li["+ str(classify_third_num) +"]/a"

            result_num1 = self.getTagText(self.search_result_path)
            result_num1 = self.numReplace(result_num1)

            classify_more_path = "html/body/div[4]/div/div[2]/p/a"
            self.xpath_find(classify_more_path).click()
            if classify_first_num > 1:
                describe1 = self.getTagText(classify_first_path)
                self.xpath_find(classify_first_path).click()

                describe = describe1
                # sleep(3)
            if classify_second_num > 1:
                describe2 = self.getTagText(classify_second_path)
                self.xpath_find(classify_second_path).click()
                describe = describe + "-" + describe2
                # sleep(3)
            if classify_third_num > 1:
                describe3 = self.getTagText(classify_third_path)
                self.xpath_find(classify_third_path).click()
                describe = describe + "-" + describe3

                # sleep(3)
            result_num2 = self.getTagText(self.search_result_path)
            result_num2 = self.numReplace(result_num2)
            return describe, result_num1, result_num2
        except:
            self.getScreenShot("搜索分类" + describe)
            return False


    def search_type(self, search_input=None, type_num=None ):    # 格式测试

        '''
            type_num:
            1:全部    2:PDS   3:AI    4:CDR   5:EPS   6:JPG   7:PNG   8:MOV   9:DWG   10:PPT  11:DOCX 12:XLS
        '''
        describe = ""
        try:
            self.search_main(search_input)

            type_describe_path = ".//*[@id='cate_size']/li["+ str(type_num) +"]/a"
            describe = self.getTagText(type_describe_path)
            result_num1 = self.getTagText(self.search_result_path)
            result_num1 = self.numReplace(result_num1)
            type_path = ".//*[@id='cate_size']/li[" + str(type_num) + "]/i"

            if type_num != 1:
                self.xpath_find(type_path).click()
            else:
                self.xpath_find(".//*[@id='cate_size']/li[2]/i").click()
                result_num1 = self.getTagText(self.search_result_path)
                result_num1 = self.numReplace(result_num1)
                self.xpath_find(type_path).click()
            result_num2 = self.getTagText(self.search_result_path)
            result_num2 = self.numReplace(result_num2)

            return describe, result_num1, result_num2
        except:
            self.getScreenShot("搜索格式" + describe)
            return False
        # picture_path = self.search_base_path + "/div["+ str(picture_num) +"]/div/a"
        # describe_path = self.search_base_path + "/div["+ str(picture_num) +"]/p/span[2]"
        # describe = self.getTagText(describe_path)
        # try:
        #     if picture_num == 1 or picture_num ==5:
        #
        #         ad_sign_path = self.search_base_path + "/div["+ str(picture_num) +"]/div/span"
        #         ad_sign = self.getTagText(ad_sign_path)
        #         if ad_sign == "广告":
        #             picture_type = "广告"
        #             describe = "广告"
        #         else:
        #             picture_type = "素材"
        #             describe = self.getTagText(describe_path)
        #     else:
        #         picture_type = "素材"
        #         describe = self.getTagText(describe_path)
        # except:
        #     picture_type = "素材"
        #     describe = self.getTagText(describe_path)


        # self.driver.find_element_by_xpath(picture_path).click()




    def search_material_classify(self, search_input=None, classify_num=None):  #类型
        try:
            classify_num += 1
            self.search_main(search_input)
            classify_path = "html/body/div[4]/div/div[5]/div/div[1]/div[1]/div[1]/a"    #类型路径
            self.mouseAbove(classify_path)
            classify_chose_path = ".//*[@id='cate_type']/li["+ str(classify_num) +"]/a"
            describe = self.getTagText(classify_chose_path)

            self.xpath_find(classify_chose_path).click()

            sleep(3)

            card_tag_path = "html/body/div[4]/div/div[5]/div/div[3]/div/div[2]/p/span"
            card_tag = self.getAttribute(card_tag_path, "class")
            return describe, card_tag
        except:
            self.getScreenShot("搜索类型")
            return False

    def search_copyright(self, search_input=None):     #版权
        try:
            self.search_main(search_input)
            result_num_path = "html/body/div[4]/div/div[1]/em"
            result_num1 = self.getTagText(result_num_path)
            result_num1 = self.numReplace(result_num1)

            copyright_path = "html/body/div[4]/div/div[5]/div/div[1]/div[1]/div[2]/a"
            self.mouseAbove(copyright_path)

            business_path = ".//*[@id='cate_banquan']/li[2]/a"
            describe = self.getTagText(business_path)
            self.xpath_find(business_path).click()
            result_num2 = self.getTagText(result_num_path)
            result_num2 = self.numReplace(result_num2)

            return describe, result_num1, result_num2
        except:
            self.getScreenShot("搜索版权")
            return False

    def search_color_scheme(self, search_input=None,color_num=None):       #色系
        try:
            color_num += 1
            self.search_main(search_input)
            result_num_path = "html/body/div[4]/div/div[1]/em"
            result_num1 = self.getTagText(result_num_path)
            result_num1 = self.numReplace(result_num1)
            color_scheme_path = "html/body/div[4]/div/div[5]/div/div[1]/div[1]/div[3]/a"
            describe = self.getTagText(color_scheme_path)
            self.mouseAbove(color_scheme_path)

            color_path = ".//*[@id='cate_color']/li["+ str(color_num) +"]/a"

            self.xpath_find(color_path).click()
            result_num2 = self.getTagText(result_num_path)
            result_num2 = self.numReplace(result_num2)

            return describe, result_num1, result_num2
        except:
            self.getScreenShot("搜索色系")
            return False


    def search_format(self, search_input=None,format_num=None): #版式
        try:
            format_num += 1
            self.search_main(search_input)
            result_num_path = "html/body/div[4]/div/div[1]/em"
            result_num1 = self.getTagText(result_num_path)
            result_num1 = self.numReplace(result_num1)
            format_path = "html/body/div[4]/div/div[5]/div/div[1]/div[1]/div[4]/a"
            self.mouseAbove(format_path)

            format_child_path = ".//*[@id='cate_banshi']/li["\
                                + str(format_num) +"]/a"
            describe = self.getTagText(format_child_path)
            self.xpath_find(format_child_path).click()
            result_num2 = self.getTagText(result_num_path)
            result_num2 = self.numReplace(result_num2)

            return describe, result_num1, result_num2
        except:
            self.getScreenShot("搜索版式")
            return False

    def search_sort(self, search_input=None,sort_num=None):   #排序
        """
        
        :param search_input: 
        :param sort_num:    {1:默认, 2:最新上传, 3:下载最多, 4:收藏最多}
        :return: 
        """
        try:
            self.search_main(search_input)
            sort_path = "html/body/div[4]/div/div[5]/div/div[1]/div[2]/ul/span["\
                        + str(sort_num) +"]/li/a"
            describe = self.getTagText(sort_path)   #获取排序名称
            compare_describe_path = self.second_image_describe_path
            compare_describe1 = self.getTagText(compare_describe_path)  #获取图片描述 方便比较
            if sort_num > 1:
                self.xpath_find(sort_path).click()
                sleep(3)
                compare_describe2 = self.getTagText(compare_describe_path)

            else:
                sort_num_change = sort_num + 3
                sort_path_change = "html/body/div[4]/div/div[5]/div/div[1]/div[2]/ul/span["\
                                   + str(sort_num_change) +"]/li/a"
                self.xpath_find(sort_path_change).click()
                sleep(3)
                compare_describe1 = self.getTagText(compare_describe_path)
                self.xpath_find(sort_path).click()
                sleep(3)
                compare_describe2 = self.getTagText(compare_describe_path)


            return describe, compare_describe1, compare_describe2
        except:
            self.getScreenShot("搜索排序")
            return False

    def search_related(self,search_input=None,related_num=None):     #相关搜索
        """
        
        :param search_input: 
        :param related_num: 相关搜索 第几个
        :return: 
        """
        try:
            self.search_main(search_input)
            related_path = ".//*[@id='cate_type']/a["+ str(related_num) +"]"
            describe = self.getTagText(related_path)
            search_result_path = "html/body/div[4]/div/div[1]/em"
            search_result1 = self.getTagText(search_result_path)
            self.xpath_find(related_path).click()
            sleep(1)
            search_result2 = self.getTagText(search_result_path)

            return describe, search_result1, search_result2
        except:
            self.getScreenShot("搜索相关搜索")
            return False

    def search_page_next(self, search_input=None):  #上部分 下一页跳转
        """
        
        :param search_input: 
        :return: 
        """
        try:
            self.search_main(search_input)
            describe = "翻页 右尖号"

            page_num1 = int(self.getTagText(self.page_num_path))
            image_describe1 = self.getTagText(self.second_image_describe_path)
            self.xpath_find(self.page_next_path).click()
            sleep(2)
            page_num2 = int(self.getTagText(self.page_num_path))
            image_describe2 = self.getTagText(self.second_image_describe_path)

            return describe, image_describe1, image_describe2, page_num1, page_num2
        except:
            self.getScreenShot("搜索 上部分下一页跳转")
            return False

    def search_page_back(self, search_input=None):  #上部分 上一页跳转
        """
        
        :param search_input: 
        :return: 
        """
        try:
            self.search_main(search_input)
            describe = "翻页 左尖号"
            self.xpath_find(self.page_next_path).click()
            sleep(2)
            page_num1 = int(self.getTagText(self.page_num_path))
            image_describe1 = self.getTagText(self.second_image_describe_path)
            self.xpath_find(self.page_back_path).click()
            sleep(2)
            page_num2 = int(self.getTagText(self.page_num_path))
            image_describe2 = self.getTagText(self.second_image_describe_path)

            return describe, image_describe1, image_describe2, page_num1, page_num2
        except:
            self.getScreenShot("搜索 上部分上一页跳转")
            return False

    def search_down_page_next(self, search_input=None):     #下部分 下一页跳转
        """
        
        :param search_input: 
        :return: 
        """
        try:
            self.search_main(search_input)
            describe = "底层 下一页"
            image_describe1 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num1 = int(self.getAttribute(self.page_skip_num_path, "value"))
            self.xpath_find(self.page_skip_next_path).click()
            image_describe2 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num2 = int(self.getAttribute(self.page_skip_num_path, "value"))

            return describe, image_describe1, image_describe2, page_num1, page_num2
        except:
            self.getScreenShot("搜索 下部分下一页跳转")
            return False

    def search_down_page_back(self, search_input=None):     #下部分 上一页跳转

        try:
            self.search_main(search_input)
            self.findElementByJs(self.page_skip_next_path)
            self.xpath_find(self.page_skip_next_path).click()

            describe = "底层 上一页"
            image_describe1 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num1 = int(self.getAttribute(self.page_skip_num_path, "value"))
            self.xpath_find(self.page_skip_back_path).click()
            image_describe2 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num2 = int(self.getAttribute(self.page_skip_num_path, "value"))
            return describe, image_describe1, image_describe2, page_num1, page_num2
        except:
            self.getScreenShot("搜索 下部分上一页跳转")
            return False



    def search_down_page_fourth_num_skip(self, search_input=None):  #下部分 第四个跳转按钮
        try:
            self.search_main(search_input)

            describe = "底层 第4个数字跳转"
            image_describe1 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num1 = int(self.getTagText(self.page_skip_fourth_num_btn_path))
            self.xpath_find(self.page_skip_fourth_num_btn_path).click()
            image_describe2 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num2 = int(self.getAttribute(self.page_skip_num_path, "value"))

            return describe, image_describe1, image_describe2, page_num1, page_num2
        except:
            self.getScreenShot("搜索 下部分第四个跳转按钮")
            return False

    def search_down_page_num_skip(self, search_input=None, skip_nmu=None):  #下部分 页面跳转
        try:
            self.search_main(search_input)

            describe = "底层 数字跳转"
            image_describe1 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num1 = skip_nmu
            self.xpath_find(self.page_skip_num_path).clear()
            self.xpath_find(self.page_skip_num_path).send_keys(skip_nmu)
            self.xpath_find(self.page_skip_btn_path).click()
            image_describe2 = self.getTagText(self.second_image_describe_path)
            self.findElementByJs(self.page_skip_next_path)
            page_num2 = int(self.getAttribute(self.page_skip_num_path, "value"))

            return describe, image_describe1, image_describe2, page_num1, page_num2
        except:
            self.getScreenShot("搜索 下部分页面跳转")
            return False

    def search_down_ad(self, search_input=None):    # 底部 广告
        try:
            self.search_main(search_input)
            describe = "底层广告"
            self.findElementByJs(self.search_down_ad_path)
            self.xpath_find(self.search_down_ad_path).click()
            return describe
        except:
            self.getScreenShot("搜索 底部广告")
            return False

    def search_source_click(self, search_input=None, source_num=None):     #页面素材点击
        describe = ""
        try:
            self.search_main(search_input)

            describe_path = self.search_base_path + "/div["+ str(source_num) +"]/p/span[2]"

            if source_num != 1 and source_num != 5:
                describe = self.getTagText(describe_path)
                source_path = self.search_base_path + "/div["+ str(source_num) +"]/div/a"
            else:
                self.driver.refresh()
                sleep(1)
                describe = "广告"
                source_path = self.search_base_path + "/div[" + str(source_num) + "]"
            self.findElementByJs(source_path)
            self.mouseAbove(source_path)
            self.xpath_find(source_path).click()
            sleep(1)
            return describe
        except Exception as ES:
            print(ES)
            self.getScreenShot("搜索-页面素材点击")
            return False

    def search_source_down(self,search_input=None, source_num=None):    #素材下载
        describe = ""
        try:
            self.search_main(search_input)

            source_path = "html/body/div[4]/div/div[5]/div/div[3]/div/div["+ str(source_num) +"]/div/a/div[3]/div[1]"
            source_image_path = self.search_base_path + "/div[" + str(source_num) + "]/div/a"
            describe_path = self.search_base_path + "/div[" + str(source_num) + "]/p/span[2]"
            describe = self.getTagText(describe_path)
            if source_num != 1 and source_num != 5:
                self.findElementByJs(source_image_path)
                self.mouseAbove(source_image_path)
                self.xpath_find(source_path).click()
                return describe
            else:
                return describe
        except Exception as ES:
            print(ES)
            self.getScreenShot("搜索 页面素材下载")
            return False
if __name__ == '__main__':
    # for x in range(1,5):
        driver = browser()
        f = SearchView(driver)
        f.driver.get("http://www.58pic.com")
        f.skipActivity()
        result = f.search_source_down("生活",2)
        h_all = f.driver.window_handles
        print(h_all)
        print(result)

        # f.driver.quit()

        print("gg")

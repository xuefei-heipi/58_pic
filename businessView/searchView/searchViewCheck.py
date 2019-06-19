#!/usr/bin/env python3
from time import sleep

from pic.businessView.searchView.searchView import SearchView
from pic.common.driver import browser


class SearchViewCheck(SearchView):

    base_describe = "搜索页-"
    none_result_search_path = ".//*[@id='error-area']/p"
    error_404_path = "html/body/div[1]/div"

    # 01
    def check_search_qq_login(self, search_input):  # 用社交账号直接登录  handles = 1
        describe = ""
        check_element_path = "html/body/div[1]/div/h1"
        try:
            results = self.search_qq_login(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results
                print(describe)
                check_result = self.checkSearchViewClickNoHandles(describe, check_element_path)
                return check_result
        except:
            self.getScreenShot(describe)
            return False

    # 02
    def check_search_wx_login(self, search_input):  # 用社交账号直接登录  handles = 1
        describe = ""
        check_element_path = "html/body/div[1]/div/div[1]"
        try:
            results = self.search_wx_login(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results
                check_result = self.checkSearchViewClickNoHandles(describe, check_element_path)
                return check_result
        except:
            self.getScreenShot(describe)
            return False
    # 03
    def check_search_wb_login(self, search_input):  # 用社交账号直接登录  handles = 1
        describe = ""
        check_element_path = ".//*[@id='outer']/div/div[1]/h1/a"
        try:
            results = self.search_wb_login(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results

                check_result = self.checkSearchViewClickNoHandles(describe, check_element_path)
                return check_result
        except:
            self.getScreenShot(describe)
            return False

    # 04
    # 分类
    def check_search_classify(self, search_input=None, classify_first_num=None, classify_second_num=None, classify_third_num=None):
        describe = ""
        try:
            results = self.search_classify(search_input, classify_first_num, classify_second_num, classify_third_num)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 05
    def check_search_type(self, search_input=None, type_num=None):  # 格式测试
        describe = ""
        try:
            results = self.search_type(search_input, type_num)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 06
    def check_search_material_classify(self, search_input=None, classify_num=None):  # 类型
        describe = ""
        try:
            results = self.search_material_classify(search_input, classify_num)
            describe = results[0]
            if classify_num == 1:
                if results[1] == "card-tag isYC":
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
            elif classify_num == 2:
                if results[1] == "card-tag isGX":
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
            elif classify_num == 3:
                if results[1] == "card-tag isBG":
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False


    # 07
    def check_search_copyright(self, search_input=None):  # 版权
        describe = ""
        try:
            results = self.search_copyright(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 08
    def check_search_color_scheme(self, search_input=None, color_num=None):  # 色系
        describe = ""
        try:
            results = self.search_color_scheme(search_input, color_num)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 09
    def check_search_format(self, search_input=None, format_num=None):  # 版式
        describe = ""
        try:
            results = self.search_format(search_input, format_num)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 10
    def check_search_sort(self, search_input=None, sort_num=None):  # 排序
        describe = ""
        try:
            results = self.search_sort(search_input, sort_num)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 11
    def check_search_related(self, search_input=None, related_num=None):  # 相关搜索
        describe = ""
        try:
            results = self.search_related(search_input, related_num)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] == 0 and results[2] == 0:
                    self.xpath_find(self.none_result_search_path)
                    return True
                elif results[1] != results[2]:
                    return True
        except:
            self.getScreenShot(describe)
            return False

    # 12
    def check_search_page_next(self, search_input=None):  # 上部分 下一页跳转
        describe = ""
        try:
            results = self.search_page_next(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] != results[2] and results[3] != results[4]:
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False

    # 13
    def check_search_page_back(self, search_input=None):  # 上部分 上一页跳转
        describe = ""
        try:
            results = self.search_page_back(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] != results[2] and results[3] != results[4]:
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False

    # 14
    def check_search_down_page_next(self, search_input=None):  # 下部分 下一页跳转
        describe = ""
        try:
            results = self.search_down_page_next(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] != results[2] and results[3] != results[4]:
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False

    # 15
    def check_search_down_page_back(self, search_input=None):
        describe = ""
        try:
            results = self.search_down_page_back(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] != results[2] and results[3] != results[4]:
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False

    # 16
    def check_search_down_page_fourth_num_skip(self, search_input=None):
        describe = ""
        try:
            results = self.search_down_page_fourth_num_skip(search_input)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] != results[2] and results[3] == results[4]:
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False

    # 17
    def check_search_down_page_num_skip(self, search_input=None, skip_nmu=None):
        describe = ""
        try:
            results = self.search_down_page_num_skip(search_input, skip_nmu)
            if results == False:
                return False
            else:
                describe = self.base_describe + results[0]
                if results[1] != results[2] and results[3] == results[4]:
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False

    # 18
    def check_search_down_ad(self, search_input=None):
        describe = ""
        try:
            results = self.search_down_ad(search_input)
            describe = self.base_describe + results
            check_result = self.checkSearchViewClickNoHandles(describe, "html/body/div[2]/div")
            return check_result

        except:
            self.getScreenShot(describe)
            return False

    # 19
    def check_search_source_click(self, search_input=None, source_num=None):  # 页面素材点击
        check_normal_path = "html/body/div[3]/div/div[2]/div[4]"
        check_login_path = "html/body/div[13]/div/div/div/div[1]"
        describe = ""
        try:
            results = self.search_source_click(search_input, source_num)
            describe = results
            all_h = self.driver.window_handles
            print(describe)
            print(all_h)
            if len(all_h) < 2:
                self.getScreenShot(describe)
                return False
            else:
                self.driver.switch_to_window(all_h[len(all_h) - 1])  # 跳入新句柄

            if source_num != 1 and source_num != 5:
                if self.checkElementExist(check_normal_path) or self.checkElementExist(check_login_path):
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
            else:
                if self.checkElementExist("html/body/div"):
                    return True
                else:
                    self.getScreenShot(describe)  # 出错截屏
                    return False
        except Exception as ES:
            print(ES)
            self.getScreenShot(describe)
            return False

    # 20
    def check_search_source_down(self, search_input=None, source_num=None):  # 素材下载
        describe = ""
        try:
            if source_num == 1 or source_num == 5:
                return True
            else:
                results = self.search_source_down(search_input, source_num)
                describe = results
                if self.checkElementExist("html/body/div[10]/div/div/div/div[1]"):
                    return True
                else:
                    self.getScreenShot(describe)
                    return False
        except:
            self.getScreenShot(describe)
            return False


if __name__ == '__main__':
    # driver = browser()
    # f = SearchViewCheck(driver)
    # f.driver.get("http://www.58pic.com/tupian/shenghuo.html")
    # h = f.driver.current_window_handle
    # print(h)
    # f.skipSearchGuide()
    # f.findElementByJs("/html/body/div[4]/div/div[5]/div/div[3]/div/div[2]/div/a")
    # f.xpath_find("/html/body/div[4]/div/div[5]/div/div[3]/div/div[2]/div/a").click()
    # sleep(1)
    # all_h = f.driver.window_handles
    # print(all_h)
    # print(f.getTagText("/html/body/div[4]/div[1]/div/div/div[1]"))
    # print(111)



    # all_h = f.driver.window_handles
    # print(all_h)
    driver = browser()
    f = SearchViewCheck(driver)
    f.driver.get("http://www.58pic.com")
    f.skipActivity()
    results = f.check_search_source_click("生活",1)
    # all_h = f.driver.window_handles
    # print(all_h)
    print(results)
    sleep(2)
    # f.driver.quit()
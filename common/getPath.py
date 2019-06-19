#!/usr/bin/env python3

class GetPath():

    first_floor_path = ".//div[@class='qt-header']"
    second_floor_path = ".//div[@class='qt-search-index']"
    third_floor_path = ".//div[@class='outcolor']"
    fourth_floor_path = ".//div[@class='index-main']"

    def get_first_floor_display_path(self,first_num=None, second_num=None):
        first_element_No = first_num + 1
        request_element_No = second_num
        stitching_path = "//div//div//div["
        display_element_path = self.first_floor_path + stitching_path + str(first_element_No) + "]//a"
        request_element_path = self.first_floor_path + stitching_path + str(first_element_No) + "]//div//a[" + \
                               str(request_element_No) + "]"

        return display_element_path, request_element_path

    def get_first_floor_nodisplay_path(self, first_num=None):
        first_element_No = first_num + 1
        no_display_element_path = self.first_floor_path + "//div//div//div[" + str(first_element_No) + "]//a"
        print(no_display_element_path)
        return no_display_element_path

    def get_first_floor_VIP_path(self, VIP_num=None):
        VIP_element_path = self.first_floor_path + "//div//div[2]//div[4]"
        request_VIP_element_path = self.first_floor_path + "//div//div[2]//div[4]//div//div[" + str(
            VIP_num) + "]//div//a"

        return VIP_element_path, request_VIP_element_path

    def get_first_floor_upload_path(self):
        upload_element_path = self.first_floor_path + "//div//div[2]//div[3]"
        return upload_element_path

    def get_first_floor_Login_path(self):
        Login_element_path = self.first_floor_path + "//div//div[2]//div[2]//p"
        return Login_element_path

    def get_first_floor_register_path(self):    #注册
        register_element_path=self.first_floor_path+"//div//div[2]//div[2]//p[2]"
        return register_element_path

    def get_second_floor_classify_path(self, classify_list_num=None): #分类一层
        stitching_path = "//div//div//div"
        classify_element_path=self.second_floor_path + stitching_path + "//div[1]"
        dd_element_path=self.second_floor_path + stitching_path + "//div[5]//dl//dd["+str(classify_list_num)+"]"
        return classify_element_path, dd_element_path

    def get_second_floor_classify_p_path(self, classify_list_num=None, list_sublist_num=None): #分类二层
        stitching_path = "//div//div//div"
        classify_element_path=self.second_floor_path + stitching_path + "//div[1]"
        dd_element_path=self.second_floor_path + stitching_path + "//div[5]//dl//dd["+str(classify_list_num)+"]"
        request_element_path=dd_element_path+"//div//div//div["+str(list_sublist_num)+\
                             "]//p//a"
        return  classify_element_path, dd_element_path, request_element_path

    def get_second_floor_classify_div_path(self, classify_list_num=None, list_sublist_num=None, list_request_num=None): #分类三层
        stitching_path = "//div//div//div"
        classify_element_path=self.second_floor_path + stitching_path + "//div[1]"
        dd_element_path=self.second_floor_path + stitching_path + "//div[5]//dl//dd["+str(classify_list_num)+"]"
        request_element_path=dd_element_path+"//div//div//div["+str(list_sublist_num)+\
                             "]//div//a["+str(list_request_num)+"]"

        return classify_element_path, dd_element_path, request_element_path

    def get_second_floor_search_path(self):   #搜索功能
        stitching_path = "//div//div//div"
        search_box_path=self.second_floor_path + stitching_path + "//div[2]//div//input"
        search_btn_path=self.second_floor_path + stitching_path + "//div[3]"

        return search_box_path, search_btn_path

    def get_fourth_main_link_path(self, main_link_num=None): #精选收藏夹 商用海报 等
        stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]"
        if main_link_num == 1:
            main_link_path=self.fourth_floor_path+"//div[1]//div//a"
        elif main_link_num == 2:
            main_link_path = self.fourth_floor_path + "//div[3]//div//a"
        elif main_link_num == 3:
            main_link_path = self.fourth_floor_path + "//div[4]//div[3]//div//span//a"
        elif main_link_num == 4:
            main_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[2]//span//a"
        elif main_link_num == 5:
            main_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[3]//div[2]//span//a"
        elif main_link_num == 6:
            main_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[3]//div[3]//div[2]//div//span//a"
        elif main_link_num == 7:
            main_link_path = self.fourth_floor_path + stitching_path + "//div[2]//div//span//a"
        elif main_link_num == 8:
            main_link_path = self.fourth_floor_path + stitching_path + "//div[3]//div[2]//div//span//a"
        elif main_link_num == 9:
            main_link_path = self.fourth_floor_path + stitching_path + "//div[3]//div[3]//div//span//a"
        elif main_link_num == 10:
            main_link_path = self.fourth_floor_path + stitching_path + "//div[3]//div[4]//div[2]//div//span//a"

        return main_link_path

    def get_fourth_secondary_link_path(self, secondary_link_num=None, request_link_num=None):  #二十四节气 明星设计师 手机配图 夏天 等
        stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]"
        if secondary_link_num == 1:
            secondary_link_path=self.fourth_floor_path+"//div//div[2]//a["+str(request_link_num)+"]"
        elif secondary_link_num == 2:
            secondary_link_path = self.fourth_floor_path + "//div[3]//div[2]//a[" + str(request_link_num) + "]"
        elif secondary_link_num == 3:
            secondary_link_path = self.fourth_floor_path + "//div[4]//div[3]//div[2]//a[" + \
                                  str(request_link_num) + "]"
        elif secondary_link_num == 4:
            secondary_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[2]//div[2]//a[" + \
                                  str(request_link_num) + "]"
        elif secondary_link_num == 5:
            secondary_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[3]//div[2]//div[2]//a[" + \
                                  str(request_link_num) + "]"
        elif secondary_link_num == 6:
            secondary_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[3]//div[3]//div[2]//div[2]//a[" + \
                                  str(request_link_num) + "]"
        elif secondary_link_num == 7:
            secondary_link_path = self.fourth_floor_path + stitching_path + "//div[2]//div[2]" \
                                                           "//a[" + str(request_link_num) + "]"
        elif secondary_link_num == 8:
            secondary_link_path = self.fourth_floor_path + stitching_path + "//div[3]//div[2]" \
                                                           "//div//div[2]//a[" + str(request_link_num) + "]"
        elif secondary_link_num == 9:
            secondary_link_path = self.fourth_floor_path + stitching_path + "//div[3]//div[3]" \
                                                           "//div[2]//a[" + str(request_link_num) + "]"
        elif secondary_link_num == 10:
            secondary_link_path = self.fourth_floor_path + stitching_path + "//div[3]//div[4]" \
                                                           "//div[2]//div[2]//a[" + str(request_link_num) + "]"
        return secondary_link_path

    def get_fourth_more_link_path(self, more_link_num=None):  #主界面上的 更多
        stitching_path = "//div[4]//div[4]//div[3]//div[3]//div[3]"
        if more_link_num == 1:
            more_link_path=self.fourth_floor_path+"//div//div[3]//a"
        elif more_link_num == 2:
            more_link_path = self.fourth_floor_path + "//div[3]//div[3]//a"
        elif more_link_num == 3:
            more_link_path = self.fourth_floor_path + "//div[4]//div[3]//div[3]//a"
        elif more_link_num == 4:
            more_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[2]//div[3]//a"
        elif more_link_num == 5:
            more_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[3]//div[2]//div[3]//a"
        elif more_link_num == 6:
            more_link_path = self.fourth_floor_path + "//div[4]//div[4]//div[3]//div[3]//div[2]//div[3]//a"
        elif more_link_num == 7:
            more_link_path = self.fourth_floor_path + stitching_path +  "//div[2]//div[3]" \
                                                           "//a"
        elif more_link_num == 8:
            more_link_path = self.fourth_floor_path + stitching_path +  "//div[3]//div[2]" \
                                                           "//div//div[3]//a"
        elif more_link_num == 9:
            more_link_path = self.fourth_floor_path + stitching_path +  "//div[3]//div[3]" \
                                                           "//div[3]//a"
        elif more_link_num == 10:
            more_link_path = self.fourth_floor_path + stitching_path +  "//div[3]//div[4]" \
                                                           "//div[2]//div[3]//a"
        return more_link_path

if __name__ == '__main__':
    GetPath().get_first_floor_nodisplay_path(3)
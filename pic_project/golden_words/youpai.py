# -*- coding: utf-8 -*-
import upyun

class YouPai(object):

    def __init__(self):
        # self.service = 'qiantu-js-css'
        self.service = 'qiantu-yuantu'
        self.username = 'ooopic'
        self.password = 'hckj1314pic'
        self.up = upyun.UpYun(self.service, self.username, self.password, timeout=30, endpoint=upyun.ED_AUTO)
        self.headers = {  }


    def yp_up_load(self, pic_loacl_path, pic_yp_paht):
        """
        又拍上传
        :param pic_loacl_path: 图片本地路径
        :param pic_yp_paht:     图片又拍路径
        :return:
        """
        try:
            with open(pic_loacl_path, 'rb') as f:
                self.up.put(pic_yp_paht, f, checksum=True, headers=self.headers)
                # print(res)
        except Exception as E:
            print(E)
            print('上传失败')

    def yp_delete(self, pic_yp_paht):
        """
        删除又拍图片
        :param pic_yp_paht:
        :return:
        """
        try:
            self.up.delete(pic_yp_paht)
        except Exception as E:
            print(E)
            print('删除失败')

    def get_list(self):
        res = self.up.getlist('/images/competitive/')
        print(len(res))
        print(res)

if __name__ == '__main__':
    yp = YouPai()
    pic_loacl_path = r'C:/Users/Dell/Desktop/ttt.jpg'
    pic_yp_paht = '/static/images/zhuangti-back/00d58PICea33e6Rfy370V_upload2020.jpg'

    yp.yp_up_load(pic_loacl_path, pic_yp_paht)
    # yp.yp_delete(pic_yp_paht)
    #
    # yp.get_list()
    # img_paths = [
    #     '1602473022_20200903195233009000.jpg',
    # ]
    # for img_path in img_paths:
    #     pic_loacl_path = r'C:\Users\Dell\Desktop\work\%s'  % img_path
    #     # pic_yp_paht = '/images/competitive/ibaotutest_20201012.jpg'
    #     pic_yp_paht = '/images/competitive/%s' %img_path
    #     # print(pic_yp_paht)
    #     # print(pic_loacl_path)
    #     # yp.yp_up_load(pic_loacl_path, pic_yp_paht)
    #     # yp.yp_delete(pic_yp_paht)
    #     # import time
    #     # time.sleep(2)
# -*- coding: utf-8 -*-
import upyun

class YouPai(object):

    def __init__(self):
        # self.service = 'qiantu-yuantu'
        self.service = 'qiantu-js-css'
        self.username = 'ooopic'
        self.password = 'hckj1314pic'
        self.up = upyun.UpYun(self.service, self.username, self.password, timeout=30, endpoint=upyun.ED_AUTO)
        self.headers = {  }


    def yp_up_load(self, pic_loacl_path, pic_yp_path):
        """
        又拍上传
        :param pic_loacl_path: 图片本地路径
        :param pic_yp_path:     图片又拍路径
        :return:
        """
        try:
            with open(pic_loacl_path, 'rb') as f:
                self.up.put(pic_yp_path, f, checksum=True, headers=self.headers)
                return pic_yp_path
        except:
            return False

    def yp_delete(self, pic_yp_path):
        """
        删除又拍图片
        :param pic_yp_path:
        :return:
        """
        try:
            self.up.delete(pic_yp_path)
            return True
        except:
            return False

    def get_list(self):
        # res = self.up.getlist('/images/competitive/')
        res = self.up.getlist('/movie/')
        print(len(res))
        print(res)

if __name__ == '__main__':
    yp = YouPai()
    pic_loacl_path = '1.mp4'
    # pic_yp_paht = '/static/images/zhuangti-back/00d58PICea33e6Rfy370V_upload2020.jpg'
    pic_yp_path = '/movie/1_1615382197.mp4'

    # yp.yp_up_load(pic_loacl_path, pic_yp_paht)
    # yp.get_list()
    yp.yp_delete(pic_yp_path)
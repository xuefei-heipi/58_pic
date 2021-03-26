# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
import qiniu.config

def qiniu_upload(key, localfile):
    """
    七牛上传图片接口
    :param key: 上传后保存的文件名   七牛储存的文件地址
    :param localfile:   需要上传的图片的本地地址
    :return:
    """
    #需要填写你的 Access Key 和 Secret Key
    access_key = 'OyzEe_0O8H433pm7zVEjtnSy5dVdfpsIawO2nx3f'
    secret_key = 'D57jE6_nvIw-WH78-jS2XDkGunE-NiuR_iGBS0BT'
    #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'qiantu-yuantu'
    #上传后保存的文件名
    # key = '58pic/36/79/77/sdljakliusifjla2018.jpg'
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    #要上传文件的本地路径
    # localfile = r'D:\competitive_img\800-1070.jpg'
    # print(token)
    ret, info = put_file(token, key, localfile)

# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

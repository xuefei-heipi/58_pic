# -*- coding: utf-8 -*-
import requests
from spider_movie.youpai import YouPai
import time
import os

class SpiderMovie(object):

    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

    def get_movie_url(self, upload_url, web_type):
        """
        获取视频连接
        :param upload_url:  用户填写的链接
        :param web_type:  网站类型  1->抖音     2->快手
        :return:
        """
        try:
            if web_type == 1:
                # 通过302跳转获取 页面链接
                response = requests.get(url=upload_url, headers=self.header, allow_redirects=False)
                page_url = response.headers['location']
                # 解析页面链接 获取视频id
                movie_id = page_url.split('https://www.iesdouyin.com/share/video/')[1]\
                    .split('/')[0]
                # 获取视频链接
                movie_request_url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=%s' % movie_id
                # 处理获取url
                movie_url = requests.get(url=movie_request_url, headers=self.header)\
                    .json()['item_list'][0]['video']['play_addr']['url_list'][0]

                return movie_url
            elif web_type == 2:
                # 通过302跳转获取 页面链接
                response_1 = requests.get(url, headers=self.header, allow_redirects=False)
                url_1 = response_1.headers['location']
                # 通过302跳转获取 页面链接 [不要问为啥,他就是跳了2次]
                response_2 = requests.get(url_1, headers=self.header, allow_redirects=False)
                url_2 = response_2.headers['location']
                # 解析获取视频id
                photoId = url_2.replace('//video.kuaishou.com/short-video/', '').split('?')[0]
                # print(photoId)
                url_2 = 'https:%s' % url_2
                # print(url_2)

                header_kuaishou = {
                    'Host': 'video.kuaishou.com',
                    'content-type': 'application/json',
                    'Origin': 'https://video.kuaishou.com',
                    'Cookie': 'did = web_a70a4f5fcfe4474abeaca2b79a2c7503;didv = 1615012754000;kpf = PC_WEB;kpn = KUAISHOU_VISION;clientid = 3;ktrace - context = 1 | MS43NjQ1ODM2OTgyODY2OTgyLjI4MzM3NzgyLjE2MTUwMTYxMTMzNDcuNzA3NDQ = | MS43NjQ1ODM2OTgyODY2OTgyLjg3NTMzODI5LjE2MTUwMTYxMTMzNDcuNzA3NDU = | 0 | graphql - server | webservice | false | NA;client_key = 65890b29',
                    'Referer': url_2,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.37'
                }
                # json 请求数据
                json_datas = {"operationName": "visionVideoDetail",
                         "variables": {
                             "photoId": photoId,
                             "page": "detail"
                         },
                         "query": "query visionVideoDetail($photoId: String, $type: String, $page: String, $webPageArea: String) {\n  visionVideoDetail(photoId: $photoId, type: $type, page: $page, webPageArea: $webPageArea) {\n    status\n    type\n    author {\n      id\n      name\n      following\n      headerUrl\n      __typename\n    }\n    photo {\n      id\n      duration\n      caption\n      likeCount\n      realLikeCount\n      coverUrl\n      photoUrl\n      liked\n      timestamp\n      expTag\n      llsid\n      viewCount\n      videoRatio\n      stereoType\n      __typename\n    }\n    tags {\n      type\n      name\n      __typename\n    }\n    commentLimit {\n      canAddComment\n      __typename\n    }\n    llsid\n    __typename\n  }\n}\n"}

                url_3 = 'https://video.kuaishou.com/graphql'
                res = requests.post(url_3, headers=header_kuaishou, json=json_datas)
                # print(res.json())
                kuaishou_url = res.json()['data']['visionVideoDetail']['photo']['photoUrl']

                return kuaishou_url
        except:
            return False

    def dl_movie(self, movie_url, movie_path):
        """
        下载视频
        :param movie_url: 视频连接
        :param movie_path: 视频保存的路径
        :return:
        """
        try:
            response = requests.get(url=movie_url, headers=self.header)
            with open(movie_path, 'wb') as f:
                f.write(response.content)
            return movie_path
        except:
            return False

    def delete_movie(self, movie_path):

        if os.path.exists(movie_path):
            try:
                os.remove(movie_path)
                return True
            except:
                return False
        return True

    def run(self, upload_url, web_type, movie_path, movie_id):
        """

        :param upload_url:
        :param web_type:
        :param movie_path:
        :param movie_id:
        :return:
        """
        # 获取视频url
        movie_url = self.get_movie_url(upload_url, web_type)
        if movie_url:

            # 视频保存在服务器本地
            movie_path = self.dl_movie(movie_url, movie_path)
            if movie_path:
                # 连接又拍
                yp = YouPai()
                # 视频在又拍的保存地址
                pic_yp_path = '/movie/%d_%d.mp4' % (movie_id, int(time.time()))
                # 视频上传又拍
                pic_yp_path = yp.yp_up_load(movie_path, pic_yp_path)
                # 删除本地视频
                local_is_del = self.delete_movie(movie_path)
                if pic_yp_path and local_is_del:
                    # 上传成功 一切ok
                    return {'status': 1, 'message': pic_yp_path, 'local_is_del': local_is_del}
                if pic_yp_path and not local_is_del:
                    # 上传成功  本地视频删除失败
                    return {'status': 2, 'message': pic_yp_path, 'local_is_del': local_is_del}
                if not pic_yp_path:
                    # 上传失败  本地视频删 看返回状态
                    return {'status': -1, 'message': '上传视频失败！', 'local_is_del': local_is_del}

            else:
                return {'status': -1, 'message': '下载视频失败', 'local_is_del': True}
        return {'status':-1, 'message':'获取视频url失败', 'local_is_del': True}



if __name__ == '__main__':
    kuaishou_urls = [
        'https://v.kuaishou.com/9o7grs',
        'https://v.kuaishou.com/cespMS',
    ]
    douying_urls = [
        'https://v.douyin.com/edMHEaG/'
    ]
    url = 'https://v.kuaishou.com/9o7grs'
    s_movie = SpiderMovie()
    # s_movie.run('https://v.douyin.com/edMHEaG/', '1.mp4')
    print(s_movie.run(url, 2, '1.mp4', 1))
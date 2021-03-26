# -*- coding: utf-8 -*-
import requests
from lxml import etree
from golden_words.common import *
from golden_words.qiniu_upload import qiniu_upload
import time
from selenium.common.exceptions import TimeoutException


class NiPic(object):

    def __init__(self, logger):
        #日志
        self.logger = logger
        # 竞品网站 1  昵图 2 觅知 3 昵图
        self.competitive_website = 1
        self.search_headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Connection': 'keep-alive',
                        'Cookie': 'Hm_lvt_d60c24a3d320c44bcd724270bc61f703=1600337540; JSESSIONID=B1369A26713B31A853F5118ADDE1AF3B; verifyCode=d006530a74acdc67; VerifyToken=lWjJUnFPoXu9lPajNPGb0fvVkHur6BE9dF1gV5PEy1bFZvKXDoBVM+UCxPE6LQGH; Hm_lpvt_d60c24a3d320c44bcd724270bc61f703=1600338389',
                        'Host': 'soso.nipic.com',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        self.nipic_detail_headers = {
                        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Cache - Control': 'max - age = 0',
                        'Connection': 'keep-alive',
                        'Cookie': 'Hm_lvt_d60c24a3d320c44bcd724270bc61f703=1603594631; Hm_lpvt_d60c24a3d320c44bcd724270bc61f703=1603598977',
                        'Host': 'www.nipic.com',
                        # 'Referer': 'http: // soso.nipic.com /?q = % E7 % 94 % 9F % E6 % B4 % BB',
                        'Upgrade-Insecure-Requests': '1',
                        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'

        }

        self.huitu_detail_headers = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_d60c24a3d320c44bcd724270bc61f703=1600337540; JSESSIONID=B1369A26713B31A853F5118ADDE1AF3B; verifyCode=d006530a74acdc67; VerifyToken=lWjJUnFPoXu9lPajNPGb0fvVkHur6BE9dF1gV5PEy1bFZvKXDoBVM+UCxPE6LQGH; Hm_lpvt_d60c24a3d320c44bcd724270bc61f703=1600338389',
            'Host': 'www.huitu.com',
            'Referer': 'http: // soso.nipic.com /?q = % E7 % 94 % 9F % E6 % B4 % BB',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'

        }

    def search_nipic(self, search_word):
        """
        昵图搜索结果图片链接
        :param search_word: 搜索词
        :return:
        """
        url = 'http://soso.nipic.com/?q=%s' % search_word
        # 请求
        # requests_error = False
        requests_res = True
        response = requests_daili(url, self.search_headers,  requests_res)

        if not response:
            raise ValueError("ip使用连续失败10次不能运行")

        # 获取页面元素
        html = etree.HTML(response.text)
        # 页面所有图片元素
        result = html.xpath('.//ul[@class="clearfix"]/li[@class="new-search-works-item"]')

        # 存储素材详情页url
        pic_urls = []

        #获取前20条 不足则 获取全部
        url_result = result if len(result) < 20 else result[0:20]
        for res in url_result:
            try:
                # 过滤下一页这种假图片
                if res.xpath('.//a/@class')[0] != 'search-works-thumb search-works-nextpage middle-box  ':
                    # title = res.xpath('.//a[@class="search-works-thumb relative"]/@title')[0]
                    # 解析获取url_r
                    url_r = res.xpath('.//a[@class="search-works-thumb relative"]/@href')[0]
                    pic_urls.append(url_r)
            except Exception as E:
                self.logger.info(E)

        return pic_urls

    def nipic_detail_page_webdriver(self, url, driver):
        """
        selenium 爬取数据
        :param url
        :param dirver:
        :return:
        """
        pic_info = {}

        driver_error = False
        driver_res = True
        while driver_res:
            try:
                try:
                    driver.get(url)
                except TimeoutException:
                    print('超时了 但是没关系')
                    pass
                driver_res = False
            except:
                driver.quit()
                driver = create_daili_browser(2)
                # 当driver 为 False的时候停止运行
                if not driver_res:
                    driver_error = True
                    driver_res = False
        if driver_error:
            raise ValueError("ip使用连续失败10次不能运行")

        if 'http://www.nipic.com/show/' in url:
            try:
                pic_title = get_content_by_xpath(driver, './/h1[@class="works-show-title"]')
                pic_id = get_content_by_xpath(driver, './/span[@class="pr40" and @itemprop="number"]/span')
                img_url = get_dom_src(driver, './/div[@id="static"]/img', 'src')
                pic_authorization = get_content_by_xpath(driver, './/span[@class="red1"]')
                create_time = get_content_by_xpath(driver, './/span[@class="pr40" and @itemprop="addtime"]/span')
                pic_volume = get_content_by_xpath(driver, './/span[@itemprop="filesize"]/span')
                pic_dpi = get_content_by_xpath(driver, './/span[@itemprop="pixel" and @class="pr30"]/span')
                pic_size = get_content_by_xpath(driver, './/span[@itemprop="pixel&dpi" and @class="pr30"]/span')
                pic_format = get_content_by_xpath(driver, './/span[@itemprop="file format" and @class="pr30"]/span')
                pic_color_mode = get_content_by_xpath(driver, './/span[@itemprop="mode"]/span')
                pic_price = get_content_by_xpath(driver, './/div[@class="fr works-img-price mt5 align-center"]')
                pic_key_word = get_content_by_xpath(driver, './/dd[@class="fl wordwrap"]', 2)

            except Exception as E:
                self.logger.info(E)

        elif 'http://www.nipic.com/detail/huitu' in url:
            try:
                pic_title = get_content_by_xpath(driver,
                                                 './/h1[@itemprop="name" and @class="works-show-title ellipsis"]')
                pic_id = get_content_by_xpath(driver, './/span[@itemprop="number"]/span')
                img_url = get_dom_src(driver, './/div[@id="static"]/div/span/img', 'src')
                pic_authorization = get_content_by_xpath(driver, './/span[@class="red1"]')
                create_time = get_content_by_xpath(driver, './/span[@itemprop="addtime"]/span')
                pic_volume = get_content_by_xpath(driver, './/span[@itemprop="filesize"]/span')
                pic_dpi = get_content_by_xpath(driver, './/span[@itemprop="pixel"]/span')
                pic_size = get_content_by_xpath(driver, './/span[@itemprop="pixel&dpi"]/span')
                pic_format = get_content_by_xpath(driver, './/span[@itemprop="file format"]/span')
                pic_color_mode = get_content_by_xpath(driver, './/span[@itemprop="mode"]/span')
                pic_price = get_content_by_xpath(driver, '//div[@id="huituTypeBox"]/div/label/b')
                pic_key_word = get_content_by_xpath(driver, './/dd[@class="fl wordwrap"]', 3)

            except Exception as E:
                self.logger.info(E)
        elif 'http://www.huitu.com/design/show' in url or 'http://www.huitu.com/photo/' in url:

            # 页面所有图片元素
            try:
                elements = get_elements_by_xpath(driver, './/div[@class="pic-info-box"]/label')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = ''
                for el in elements:
                    text = el.get_attribute('textContent')
                    if '编号' in text:
                        pic_id = processing_str(text.replace('编号：', ''))
                    elif '像素' in text:
                        pic_size = processing_str(text.replace('像素：', ''))
                    elif '格式' in text:
                        pic_format = processing_str(text)
                    elif '大小' in text:
                        pic_volume = processing_str(text.replace('大小：', ''))
                    elif '分辨率' in text:
                        pic_dpi = processing_str(text.replace('分辨率：', ''))
                    elif '颜色模式' in text:
                        pic_color_mode = processing_str(text.replace('颜色模式：', ''))
                pic_title = get_content_by_xpath(driver, './/h1[@class="info-right-title"]')
                img_url = get_dom_src(driver, './/div[@class="m-img-wrap"]/div/img', 'src')
                pic_authorization = get_content_by_xpath(driver, './/div[@class="left-authorization"]')
                create_time = ''
                pic_price = get_content_by_xpath(driver, './/strong[@class="money"]')
                pic_key_word = get_content_by_xpath(driver, './/div[@class="keyword-box"]', 3)

            except Exception as E:
                self.logger.info(E)
        else:
            self.logger.error('链接属于无法识别的链接，需要单独处理%s' % url)

        pic_info['pic_id'] = pic_id
        pic_info['competitive_web'] = self.competitive_website
        pic_info['pic_title'] = pic_title
        pic_info['img_url'] = img_url
        pic_info['pic_authorization'] = pic_authorization
        pic_info['create_time'] = create_time
        pic_info['pic_volume'] = pic_volume
        pic_info['pic_dpi'] = pic_dpi
        pic_info['pic_size'] = pic_size
        pic_info['pic_format'] = pic_format
        pic_info['pic_color_mode'] = pic_color_mode
        pic_info['pic_price'] = pic_price
        pic_info['pic_key_word'] = pic_key_word

        print(pic_info)
        return pic_info, driver

    def nipic_detail_page(self, url):
        """
        requests 请求 + lxml 爬取数据
        :param url:
        :return:
        """
        pic_info = {}

        # # 请求
        # response = requests.get(url=url, headers=self.nipic_detail_headers, timeout=5)
        # # 获取页面元素
        # html = etree.HTML(response.text)

        if 'http://www.nipic.com/show/' in url:
            # 请求
            response = requests_daili(url, self.nipic_detail_headers, True)
            if response.status_code != 500:
                if not response:
                    raise ValueError("ip使用连续失败10次不能运行")
            # if response.status_code == 500:
            #     self.logger.info(response.text)
            # 获取页面元素
            html = etree.HTML(response.text)
            # 页面所有图片元素

            try:
                pic_id = processing_data(html.xpath('.//span[@class="pr40" and @itemprop="number"]/span/text()'))
                title = processing_data(html.xpath('.//h1[@class="works-show-title"]/text()'))
                img_url = processing_data(html.xpath('.//div[@id="static"]/img/@src'))
                pic_authorization = processing_data(html.xpath('.//span[@class="red1"]/text()'))
                create_time = processing_data(html.xpath('.//span[@class="pr40" and @itemprop="addtime"]/span/text()'))
                pic_volume = processing_data(html.xpath('.//span[@itemprop="filesize"]/span/text()'))
                pic_dpi = processing_data(html.xpath('.//span[@itemprop="pixel" and @class="pr30"]/span/text()'))
                pic_size = processing_data(html.xpath('.//span[@itemprop="pixel&dpi" and @class="pr30"]/span/text()'))
                pic_format = processing_data(html.xpath('.//span[@itemprop="file format" and @class="pr30"]/span/text()'))
                pic_color_mode = processing_data(html.xpath('.//span[@itemprop="mode"]/span/text()'))
                pic_price = processing_data(''.join(html.xpath('.//div[@class="fr works-img-price mt5 align-center"]/descendant-or-self::text()')))
                pic_key_word = processing_data(html.xpath('.//dd[@class="fl wordwrap"]/text()'))

            except Exception as E:
                # print(E)
                self.logger.info(E)
        elif 'http://www.nipic.com/detail/huitu' in url:
            # 请求
            response = requests_daili(url, self.nipic_detail_headers, True)
            if response.status_code != 500:
                if not response:
                    raise ValueError("ip使用连续失败10次不能运行")
            # 获取页面元素
            html = etree.HTML(response.text)
            # 页面所有图片元素
            try:
                pic_id = processing_data(html.xpath('.//span[@itemprop="number"]/span/text()'))
                title = processing_data(''.join(html.xpath('.//h1[@itemprop="name" and @class="works-show-title ellipsis" ]/descendant-or-self::text()')))
                img_url = processing_data(html.xpath('.//div[@id="static"]/div/span/img/@src'))
                pic_authorization = processing_data(html.xpath('.//span[@class="red1"]/text()'))
                create_time = processing_data(html.xpath('.//span[@itemprop="addtime"]/span/text()'))
                pic_volume = processing_data(html.xpath('.//span[@itemprop="filesize"]/span/text()'))
                pic_dpi = processing_data(html.xpath('.//span[@itemprop="pixel"]/span/text()'))
                pic_size = processing_data(html.xpath('.//span[@itemprop="pixel&dpi"]/span/text()'))
                pic_format = processing_data(html.xpath('.//span[@itemprop="file format"]/span/text()'))
                pic_color_mode = processing_data(html.xpath('.//span[@itemprop="mode"]/span/text()'))
                pic_price = processing_data(html.xpath('//div[@id="huituTypeBox"]/div/label/b/text()'))
                pic_key_word = ''.join(processing_list(html.xpath('.//dd[@class="fl wordwrap"]/descendant-or-self::text()')))

            except Exception as E:
                # print(E)
                self.logger.info(E)
        elif 'http://www.huitu.com/design/' in url or 'http://www.huitu.com/photo/' in url:
            # 请求
            response = requests_daili(url, self.huitu_detail_headers, True)
            if response.status_code != 500:
                if not response:
                    raise ValueError("ip使用连续失败10次不能运行")
            # 获取页面元素
            html = etree.HTML(response.text)

            # 页面所有图片元素
            try:
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = ''
                elements = html.xpath('.//div[@class="pic-info-box"]/label')
                for x in range(1, len(elements)+1):
                    res = ''.join(html.xpath('.//div[@class="pic-info-box"]/label[%d]/descendant-or-self::text()' % x))

                    if '编号' in res :
                        pic_id = processing_data(html.xpath('.//div[@class="pic-info-box"]/label[%d]/text()' % x)).replace(
                            '编号：', '')
                    elif '像素' in res:
                        pic_size = processing_data(html.xpath('.//div[@class="pic-info-box"]/label[%d]/text()' % x)).replace(
                            '像素：', '')
                    elif '格式' in res:
                        pic_format = processing_data(
                            html.xpath('.//div[@class="pic-info-box"]/label[%d]/span[@class="ext-box"]/text()' % x)).replace(
                            ' ', '')
                    elif '大小' in res:
                        pic_volume = processing_data(
                            html.xpath('.//div[@class="pic-info-box"]/label[%d]/text()' % x)).replace('大小：', '')
                    elif '分辨率' in res:
                        pic_dpi = processing_data(html.xpath('.//div[@class="pic-info-box"]/label[%d]/text()' % x)).replace(
                            '分辨率：', '')
                    elif '颜色模式' in res:
                        pic_color_mode = processing_data(
                            html.xpath('.//div[@class="pic-info-box"]/label[%d]/text()' % x)).replace('颜色模式：', '')
                # 这个路径的详情页图片title路径需要单独处理
                if 'http://www.huitu.com/photo/dep' in url or 'http://www.huitu.com/design/dep/' in url:
                    title = processing_data(''.join(html.xpath('.//h3[@class="info-right-title"]/text()')))
                else:
                    title = processing_data(''.join(html.xpath('.//h1[@class="info-right-title"]/text()')))
                img_url = processing_data(html.xpath('.//div[@class="m-img-wrap"]/div/img/@src'))
                pic_authorization = processing_data(html.xpath('.//div[@class="left-authorization"]/descendant-or-self::text()'))
                create_time = processing_data(html.xpath('.//span[@class="pr40" and @itemprop="addtime"]/span/text()'))
                # pic_price = processing_data(''.join(html.xpath('.//strong[@class="money"]/descendant-or-self::text()')))
                pic_price = ''
                pic_key_word = ' '.join(processing_list(html.xpath('.//div[@class="keyword-box"]/descendant-or-self::text()')))

            except Exception as E:
                # print(E)
                self.logger.info(E)
        else:
            # print(11111)
            self.logger.error('链接属于无法识别的链接，需要单独处理%s' % url)
            pic_id = title = img_url = pic_authorization = create_time = pic_volume = ''
            pic_dpi = pic_size = pic_format = pic_color_mode = pic_price = pic_key_word = ''

        pic_info['pic_id'] = pic_id
        pic_info['competitive_web'] = self.competitive_website
        pic_info['pic_title'] = title
        pic_info['img_url'] = img_url
        pic_info['pic_authorization'] = pic_authorization
        pic_info['create_time'] = create_time
        pic_info['pic_volume'] = pic_volume
        pic_info['pic_dpi'] = pic_dpi
        pic_info['pic_size'] = pic_size
        pic_info['pic_format'] = pic_format
        pic_info['pic_color_mode'] = pic_color_mode
        pic_info['pic_price'] = pic_price
        pic_info['pic_key_word'] = pic_key_word

        print(pic_info)
        return pic_info


    # def qiniu_img_url(self, pic_id, img_url):
    #     """
    #
    #     :param img_url:
    #     :param pic_id:
    #     :return:
    #     """
    #     try:
    #         pic_name = r'D:/competitive_img/%s.jpg' % str(pic_id)
    #         r = requests.get(img_url, timeout=5, stream=True)
    #         if r.status_code == 200:
    #             with open(pic_name, 'wb') as fd:
    #                 for chunk in r.iter_content():
    #                     fd.write(chunk)
    #
    #         key_time = int(round(time.time()))
    #         # 作品 在七牛的地址
    #         key = '58pic/competitive/%s_%s.jpg' % (str(key_time), str(pic_id))
    #         localfile = pic_name
    #         # 上传七牛
    #         qiniu_upload(key, localfile)
    #         # 删除本地问天
    #         self.remove_img(pic_name)
    #         # 奇葩的七牛上传的时候不能带 /
    #         insert_key = '/' + key
    #         qn_pic_info = {
    #             'qn_img_url': insert_key,  # 七牛保存的图片地址
    #             'upload_time': key_time # 上传七牛的时间
    #         }
    #     except Exception as E:
    #         self.logger.warning(E)
    #         self.logger.warning('%s 素材上传七牛失败' % str(pic_id))
    #         return False
    #
    #
    #     return qn_pic_info

if __name__ == '__main__':

    # logger = write_log()
    nipic = NiPic()
    # nipic.nipic_detail_page('http://www.nipic.com/show/32193966.html')
    # time_stamp = int(round(time.time() * 1000))
    # print(time_stamp)
    urls = nipic.search_nipic('双十一')
    print(urls)
    for url in urls:
        print(url)
        nipic.nipic_detail_page(url)
        import random
        time.sleep(random.randint(1,2))



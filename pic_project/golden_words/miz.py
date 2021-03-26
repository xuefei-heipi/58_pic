# -*- coding: utf-8 -*-
import sys, os
import requests
from lxml import etree
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from golden_words.common import *
from time import sleep
# from golden_words.qiniu_upload import qiniu_upload
import time
from selenium.common.exceptions import TimeoutException


class Miz(object):

    def __init__(self, logger):
        # 日志
        self.logger = logger
        # 竞品网站 1  昵图 2 觅知
        self.competitive_website = 2

        self.headers = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'couponSign=1; ustk=20200930_3728983598_471428252; ufrom=111; Hm_lvt_aa0de2c55d65303b7191698178841e01=1601453198; semplan=1; semunit=1; semkeywordid=1; semsource=1; Qs_lvt_158497=1601453197; Hm_lvt_d8453059bf561226f5e970ffb07bd9d2=1601453198; backurl=http%3A%2F%2Fwww.51miz.com%2Fso-sucai%2F1578030.html; Qs_pv_158497=555132378244680700%2C2464954806747624000%2C3901435740251661000%2C3163365578080710700%2C4128121242843345000; Hm_lpvt_d8453059bf561226f5e970ffb07bd9d2=1601453387; Hm_lpvt_aa0de2c55d65303b7191698178841e01=1601453387',
            'Sec - Fetch - Mode': 'navigate',
            'Sec - Fetch - Site': 'none',
            'Host': 'www.51miz.com',
            'Sec - Fetch - User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }

    def get_miz_search_url(self, search_word):
        """
        获取觅知网的搜索url
        :param search_word:
        :return:
        """

        url = 'https://www.51miz.com/?m=Search&ajax=1&keyword=%s&plate_path=sucai' % search_word

        # res = requests.get(url=url, headers=self.headers)
        requests_res = True
        response = requests_daili(url, self.headers, requests_res)

        if not response:
            raise ValueError("ip使用连续失败10次不能运行")

        if response.status_code == 200:
            try:
                url = eval(response.text)['url'].replace('\\', '')
                return url
            except:
                return False
        return False

    def search_miz(self, search_word):
        """
        爬取觅知网搜索页数据
        :param search_word:
        :return:
        """
        # 获取url
        url = self.get_miz_search_url(search_word)
        # 请求
        if url:
            # response = requests.get(url=url, headers=self.headers)
            requests_res = True
            response = requests_daili(url, self.headers, requests_res)

            if not response:
                raise ValueError("ip使用连续失败10次不能运行")

            # 获取页面元素
            html = etree.HTML(response.text)
            # 页面所有图片元素
            result = html.xpath('.//div[@class="flex-images pr"]/div[@class="element-box item"]')

            # 存储素材详情页url
            pic_urls = []

            # 获取前20条 不足则 获取全部
            url_result = result

            for res in url_result:
                try:
                    if len(pic_urls) >= 20:
                        break
                    # 解析获取url_r
                    url_r = res.xpath('.//div[@class="element-box-detail"]/div[@class="element pr oh"]'
                                      '/a[@class="image-box"]/@href')[0]
                    # 过滤掉非正常素材链接
                    if 'https://www.51miz.com/sucai' in url_r:
                        pic_urls.append(url_r)
                    elif 'https://www.51miz.com/muban' in url_r:
                        pic_urls.append(url_r)
                except Exception as E:
                    self.logger.warning(E)

            return pic_urls

        # 如果没有返回数据 或者 程序异常
        return []

    def miz_detail_page_webdriver(self, url, driver):
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
                driver = create_daili_browser(type=2)
                # 当driver 为 False的时候停止运行
                if not driver_res:
                    driver_error = True
                    driver_res = False

        if driver_error:
            raise ValueError("ip使用连续失败10次不能运行")


        if 'https://www.51miz.com/sucai/' in url:
            try:
                elements = get_elements_by_xpath(driver, './/div[@class="otherinfo oh fn14"]/div')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = pic_authorization = ''
                for el in elements:
                    text = el.get_attribute('textContent')
                    if '素材编号ID' in text:
                        pic_id = processing_str(text.replace('素材编号ID： ', ''))
                    elif 'PNG尺寸' in text:
                        pic_size = processing_str(text.replace('PNG尺寸： ', ''))
                    elif '源文件格式' in text:
                        pic_format = processing_str(text.replace('源文件格式： ', ''))
                    elif '大小' in text:
                        pic_volume = processing_str(text.replace('大小：', ''))
                    elif '分辨率' in text:
                        pic_dpi = processing_str(text.replace('分辨率： ', ''))
                    elif '颜色模式' in text:
                        pic_color_mode = processing_str(text.replace('颜色模式： ', ''))
                    elif '授权方式' in text:
                        pic_authorization = processing_str(text.replace('授权方式： ', ''))

                pic_title = get_content_by_xpath(driver, './/h1[@class="iftip"]').replace('\xa0', '')
                img_url = get_dom_src(driver, './/div[@class="show-box fl pr"]/div[@class="img-box oh pr"]/img', 'src')
                create_time = ''
                pic_price = ''
                pic_key_word = get_content_by_xpath(driver, './/div[@class="tags fn14"]/p[2]/span[2]', 2)

            except Exception as E:
                self.logger.warning(E)


        elif 'https://www.51miz.com/muban' in url:
            try:
                elements = get_elements_by_xpath(driver, './/div[@id="detailed-box"]/ul/li')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = pic_authorization = pic_price = ''
                for el in elements:
                    text = el.get_attribute('textContent')
                    if '编号' in text:
                        pic_id = processing_str(text.replace('编号', '')).replace('D', '')
                    elif '尺寸' in text:
                        pic_size = processing_str(text.replace('尺寸', ''))
                    elif '格式' in text:
                        pic_format = processing_str(text.replace('格式', ''))
                    elif '大小' in text:
                        pic_volume = processing_str(text.replace('大小', ''))
                    elif '分辨率' in text:
                        pic_dpi = processing_str(text.replace('分辨率', ''))
                    elif '颜色模式' in text:
                        pic_color_mode = processing_str(text.replace('颜色模式', ''))
                    elif '授权方式' in text:
                        pic_authorization = processing_str(text.replace('授权方式', ''))
                    elif '价格' in text:
                        pic_price = processing_str(text.replace('价格', ''))
                pic_title = get_content_by_xpath(driver, './/div[@class="showTitle"]/div[@class="titleBox"]/h1/span')
                img_url = get_dom_src(driver, './/div[@class="preview-content"]/div/img', 'src')
                create_time = ''
                pic_key_word = ''

                elements_key_word = get_elements_by_xpath(driver , './/div[@class="showBox-left fl"]/div[@class="showKeyword color-bbb fn12"]')
                for el in elements_key_word:
                    if '标签' in el.get_attribute('textContent'):
                        pic_key_word = get_content_by_xpath(el, './/p', 2)

            except Exception as E:
                self.logger.warning(E)
        else:
            self.logger.warning('链接属于无法识别的链接，需要单独处理%s' % url)


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
        return pic_info , driver


    def miz_detail_page(self, url):

        """
        request爬取数据
        :param url
        :param dirver:
        :return:
        """
        pic_info = {}

        # 请求
        response = requests.get(url=url, headers=self.headers, timeout=5)
        html = etree.HTML(response.text)

        if 'https://www.51miz.com/sucai/' in url:
            try:
                # 获取页面元素
                elements = html.xpath('.//div[@class="otherinfo oh fn14"]/div')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = pic_authorization = ''

                for x in range(1, len(elements)+1):
                    res = ''.join(html.xpath('.//div[@class="otherinfo oh fn14"]/div[%d]/descendant-or-self::text()' % x))
                    if '素材编号ID' in res :
                        pic_id = res.replace('素材编号ID：', '')
                    elif 'PNG尺寸' in res:
                        pic_size = res.replace('PNG尺寸：', '')
                    elif '源文件格式' in res:
                        pic_format = res.replace('源文件格式：', '')
                    elif '大小' in res:
                        pic_volume = res.replace('大小：', '')
                    elif '分辨率' in res:
                        pic_dpi = res.replace('分辨率：', '')
                    elif '颜色模式' in res:
                        pic_color_mode = res.replace('颜色模式：', '')
                    elif '授权方式' in res:
                        pic_authorization = res.replace('授权方式：', '')
                pic_title = processing_data(html.xpath('.//h1[@class="iftip"]/descendant-or-self::text()'))
                img_url = processing_data(html.xpath('.//div[@class="show-box fl pr"]/div[@class="img-box oh pr"]/img/@src'))
                create_time = ''
                pic_price = ''
                pic_key_word = processing_data(html.xpath('.//div[@class="tags fn14"]/p[2]/span[2]/descendant-or-self::text()'))

            except Exception as E:
                # print(E)
                self.logger.warning(E)


        elif 'https://www.51miz.com/muban' in url:
            try:
                elements = html.xpath('.//div[@id="detailed-box"]/ul/li')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = pic_authorization = pic_price = ''
                #遍历获取 每一个 数据
                for x in range(1, len(elements)+1):
                    res = ''.join(html.xpath('.//div[@id="detailed-box"]/ul/li[%d]/descendant-or-self::text()' % x))
                    res_value = ''.join(html.xpath('.//div[@id="detailed-box"]/ul/li[%d]/'
                                                   'span[@class="fr detailed-value"]/descendant-or-self::text()' % x))
                    if '编号' in res:
                        pic_id = res_value.replace('D', '').replace('摄影图片仅供参考\xa0', '').replace('字体仅供参考\xa0', '')
                    elif '尺寸' in res:
                        pic_size = res_value.replace('尺寸', '').replace('摄影图片仅供参考\xa0', '')
                    elif '格式' in res:
                        pic_format = res_value.replace('格式', '')
                    elif '大小' in res:
                        pic_volume = res_value.replace('大小', '')
                    elif '分辨率' in res:
                        pic_dpi = res_value.replace('分辨率', '')
                    elif '颜色模式' in res:
                        pic_color_mode = res_value.replace('颜色模式', '')
                    elif '授权方式' in res:
                        pic_authorization = res_value.replace('授权方式', '')
                    elif '价格' in res:
                        pic_price = res_value.replace('价格', '')
                pic_title = processing_data(html.xpath('.//div[@class="showTitle"]/div[@class="titleBox"]/h1/span/descendant-or-self::text()'))
                img_url = processing_data(html.xpath('.//div[@class="preview-content"]/div/img/@src'))
                #对切图做处理获取整图
                if '-0.jpg' in img_url:
                    img_url = img_url.split('-0.jpg')[0]
                create_time = ''
                pic_key_word = ''

                elements_key_word = html.xpath('.//div[@class="showBox-left fl"]/div[@class="showKeyword color-bbb fn12"]')
                for x in range(1, len(elements_key_word) + 1):
                    res = ''.join(html.xpath('.//div[@class="showBox-left fl"]/'
                                             'div[@class="showKeyword color-bbb fn12"][%d]/descendant-or-self::text()' % x))
                    res_value = ''.join(html.xpath('.//div[@class="showBox-left fl"]/'
                                             'div[@class="showKeyword color-bbb fn12"][%d]/p/descendant-or-self::text()' % x))
                    if '标签' in res:
                        pic_key_word = res_value

            except Exception as E:
                # print(E)
                self.logger.warning(E)
        else:
            # print(111)

            self.logger.warning('链接属于无法识别的链接，需要单独处理%s' % url)

        # 图片url处理一下
        if 'https:' not in img_url:
            img_url = 'https:%s' % img_url

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
        return pic_info

if __name__ == '__main__':
    miz = Miz()
    # driver = browser()

    url = 'https://www.51miz.com/muban/510270.html'
    miz.miz_detail_page(url)


# -*- coding: utf-8 -*-
import sys, os
import requests
from lxml import etree
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from golden_words.common import *
from selenium.common.exceptions import TimeoutException
from time import sleep
# from golden_words.qiniu_upload import qiniu_upload
import time


class IBaoTu(object):

    def __init__(self, logger):
        # 日志
        self.logger = logger
        # 竞品网站 1  昵图 2 觅知 3 包图
        self.competitive_website = 3

        self.headers = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'couponSign=1; ustk=20200930_3728983598_471428252; ufrom=111; Hm_lvt_aa0de2c55d65303b7191698178841e01=1601453198; semplan=1; semunit=1; semkeywordid=1; semsource=1; Qs_lvt_158497=1601453197; Hm_lvt_d8453059bf561226f5e970ffb07bd9d2=1601453198; backurl=http%3A%2F%2Fwww.51miz.com%2Fso-sucai%2F1578030.html; Qs_pv_158497=555132378244680700%2C2464954806747624000%2C3901435740251661000%2C3163365578080710700%2C4128121242843345000; Hm_lpvt_d8453059bf561226f5e970ffb07bd9d2=1601453387; Hm_lpvt_aa0de2c55d65303b7191698178841e01=1601453387',
            'Sec - Fetch - Mode': 'navigate',
            'Sec - Fetch - Site': 'none',
            'Host': 'ibaotu.com',
            'Sec - Fetch - User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }

    def get_baotu_search_url(self, search_word):
        """
        获取包图网的搜索url
        :param search_word:
        :return:
        """

        url = 'https://ibaotu.com/index.php?m=search&a=check&kw=%s' % search_word

        # res = requests.get(url=url, headers=self.headers)
        # requests_error = False
        requests_res = True
        res = requests_daili(url, self.headers, requests_res)
        if not res:
            raise ValueError("ip使用连续失败10次不能运行")

        if res.status_code == 200:
            try:
                r_json = res.json()['py']
                url = 'https://ibaotu.com/tupian/%s.html' % r_json
                return url
            except:
                return False
        return False

    def search_baotu(self, search_word):

        # 获取url
        url = self.get_baotu_search_url(search_word)
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
            result = html.xpath('.//div[@class="bt-body search clearfix"]/dl[@class="pic-box pr-container "]')
            # 存储素材详情页url
            pic_urls = []

            # 获取前20条 不足则 获取全部
            url_result = result

            for res in url_result:
                try:
                    if len(pic_urls) >= 20:
                        break
                    # 解析获取url_r
                    url_r = res.xpath('.//dd/div[@class="hover-pop"]'
                                      '/div[@class="pop-tit gradient-ver-wb clearfix"]/a/@href')[0]
                    # 需要单独处理一下 没有协议
                    url_r = 'https:%s' % url_r
                    # 过滤掉非正常素材链接
                    if '//ibaotu.com/sucai/' in url_r:
                        pic_urls.append(url_r)
                except Exception as E:
                    self.logger.warning(E)
            return pic_urls
        # 搜索获取url 错误时
        return []


    def baotu_detail_page_webdriver(self, url, driver):
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


        if 'https://ibaotu.com/sucai/' in url:
            try:
                elements = get_elements_by_xpath(driver, './/ul[@class="details-wrap"]/li')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = pic_authorization = create_time = ''
                for el in elements:
                    text = el.get_attribute('textContent')
                    if '素材编号' in text:
                        pic_id = processing_str(text.replace('素材编号：', ''))
                    elif '尺寸像素' in text:
                        pic_size = processing_str(text.replace('尺寸像素：', ''))
                    elif '文件格式' in text:
                        pic_format = processing_str(text.replace('文件格式：', ''))
                    elif '文件大小' in text:
                        pic_volume = processing_str(text.replace('文件大小：', ''))
                    elif '分辨率' in text:
                        pic_dpi = processing_str(text.replace('分辨率：', ''))
                    elif '颜色模式：' in text:
                        pic_color_mode = processing_str(text.replace('颜色模式：', ''))
                    elif '授权方式' in text:
                        pic_authorization = processing_str(text.replace('授权方式： ', ''))
                    elif '上传时间' in text:
                        create_time = processing_str(text.replace('上传时间：', ''))

                pic_title = get_content_by_xpath(driver, './/h1[@class="works-name"]')
                img_url = get_dom_src(driver, './/div[@class="work-imgs"]/div[@class="img-wrap "]/img', 'src')
                # 包图太坑1
                if img_url == '':
                    img_url = get_dom_src(driver, './/div[@class="work-imgs"]/div[@class="img-wrap "]/a/img', 'src')
                # 包图太坑2    https://ibaotu.com/sucai/19509158.html
                if img_url == '':
                    img_url = get_dom_src(driver, './/img[@class="scrollLoading"]', 'src')
                # 包图没有价格属性
                pic_price = ''
                # 包图 key word 需要单独处理
                pic_key_word = ''
                elements_key_word = get_elements_by_xpath(driver, './/div[@class="related-search clearfix"]/a')
                for el in elements_key_word:
                    pic_key_word = pic_key_word + el.get_attribute('textContent') + ' '
            except Exception as E:
                self.logger.warning(E)

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


    def baotu_detail_page(self, url):

        pic_info = {}

        requests_res = True
        response = requests_daili(url, self.headers, requests_res)

        if not response:
            raise ValueError("ip使用连续失败10次不能运行")
        # 获取页面元素
        html = etree.HTML(response.text)

        if 'https://ibaotu.com/sucai/' in url:
            try:
                elements = html.xpath('.//ul[@class="details-wrap"]/li')
                pic_id = pic_size = pic_format = pic_volume = pic_dpi = pic_color_mode = pic_authorization = create_time = ''

                for x in range(1, len(elements)+1):

                    res = ''.join(html.xpath('.//ul[@class="details-wrap"]/li[%d]/descendant-or-self::text()' % x))
                    res_value = ''.join(html.xpath('.//ul[@class="details-wrap"]/li[%d]/span[2]/descendant-or-self::text()' % x))
                    if '素材编号' in res:
                        # filter 方法去除str中非数字
                        pic_id = ''.join(filter(str.isdigit, processing_data(res_value).replace('素材编号：', '')))
                    elif '尺寸像素' in res:
                        pic_size = processing_data(res_value).replace('尺寸像素：', '').replace('联系客户经理', '')
                    elif '文件格式' in res:
                        pic_format = processing_data(res_value).replace('文件格式：', '')
                    elif '文件大小' in res:
                        pic_volume = processing_data(res_value).replace('文件大小：', '')\
                            .replace('联系客户经理', '')
                    elif '分辨率' in res:
                        pic_dpi = processing_data(res_value).replace('分辨率：', '')
                    elif '颜色模式：' in res:
                        pic_color_mode = processing_data(res_value).replace('颜色模式：', '')\
                            .replace('摄影图片仅供参考咨询企业客服', '')
                    elif '授权方式' in res:
                        pic_authorization = processing_data(res_value).replace('授权方式： ', '')
                    elif '上传时间' in res:
                        create_time = processing_data(res_value).replace('上传时间：', '')

                pic_title = processing_data(html.xpath('.//h1[@class="works-name"]/descendant-or-self::text()'))
                img_url = processing_data(html.xpath('.//div[@class="work-imgs"]/div[@class="img-wrap "]/img/@src'))
                # 包图太坑1
                if img_url == '':
                    img_url = processing_data(html.xpath('.//div[@class="work-imgs"]/div[@class="img-wrap "]/a/img/@src'))
                # 包图太坑2    https://ibaotu.com/sucai/19509158.html
                if img_url == '':
                    img_url = processing_data(html.xpath('.//img[@class="scrollLoading"]@src'))
                # 包图没有价格属性
                pic_price = ''
                # 包图 key word 需要单独处理
                pic_key_word = ' '.join(html.xpath('.//div[@class="related-search clearfix"]/a/descendant-or-self::text()'))
                # elements_key_word = get_elements_by_xpath(driver, './/div[@class="related-search clearfix"]/a')
                # for el in elements_key_word:
                #     pic_key_word = pic_key_word + el.get_attribute('textContent') + ' '
            except Exception as E:
                print(E)
                # self.logger.warning(E)

        else:
            print(1)
            # self.logger.error('链接属于无法识别的链接，需要单独处理%s' % url)

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
    ibaotu = IBaoTu()
    url = 'https://ibaotu.com/sucai/19565930.html'
    ibaotu.baotu_detail_page(url)

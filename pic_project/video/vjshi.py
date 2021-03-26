# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
from video.common import *
import time
import logging
import os

class VJShi(object):

    def __init__(self):
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'Hm_lvt_d60c24a3d320c44bcd724270bc61f703=1600337540; JSESSIONID=B1369A26713B31A853F5118ADDE1AF3B; verifyCode=d006530a74acdc67; VerifyToken=lWjJUnFPoXu9lPajNPGb0fvVkHur6BE9dF1gV5PEy1bFZvKXDoBVM+UCxPE6LQGH; Hm_lpvt_d60c24a3d320c44bcd724270bc61f703=1600338389',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'

        }

    def category_page(self, page_num, cursor):

        # url = 'https://www.vjshi.com/aemuban.html?order=down&p=%d' % page_num
        url = 'https://www.vjshi.com/premiere.html?order=down&p=%d' % page_num
        try:
            response = requests.get(url=url, headers=self.header, timeout=5)
            # 获取页面元素
            html = etree.HTML(response.text)
            # 页面所有图片元素
            result = html.xpath('.//div[@id="card-container-l"]/div[@class="card card-l"]')
            # print(len(result))
            for res in result:
                pic_info = {}
                pic_id = pic_title = pic_detail_url = videoinfo = ''
                try:
                    pic_id = res.xpath('.//div[@class="card-inner-top-wrap"]/img/@data-id')[0]
                except:
                    pass
                try:
                    pic_title = res.xpath('.//div[@class="card-inner-top-wrap"]/img/@alt')[0]
                except:
                    pass
                try:
                    pic_detail_url = res.xpath('.//div[@class="card-body "]/a/@href')[0]
                except:
                    pass

                videoinfo = lxml_to_dict(res.xpath('.//div[@class="card-title"]/@videoinfo'))
                pic_upload_time = videoinfo['posttime']
                pic_price = videoinfo['price']
                pic_size = videoinfo['resolution']
                pic_dl_num = videoinfo['download']
                pic_info['pic_id'] = pic_id
                pic_info['pic_title'] = pic_title
                pic_info['pic_dl_num'] = pic_dl_num
                pic_info['pic_detail_url'] = pic_detail_url
                pic_info['pic_upload_time'] = pic_upload_time
                pic_info['pic_price'] = pic_price
                pic_info['pic_size'] = pic_size
                pic_info['page_num'] = page_num
                print(pic_info)
                if not is_pic_exist(pic_id, cursor):
                    insert_pic(pic_info, cursor)
        except Exception as E:
            print(E)

    def vjshi_detial_info(self, url, driver):
        """

        :param url:
        :param driver:
        :return:
        """
        try:
            pic_info = {}
            driver.get(url)
            category_first = category_second = collection_num = key_word = pic_img = ''
            category = get_elements_by_xpath(driver, './/div[@class="crumb-wrap"]/div[@class="crumb-item-wrap"]')
            category_first = category[1].find_element(By.XPATH, './/a').get_attribute('title')
            category_second = category[2].find_element(By.XPATH, './/a').get_attribute('title')
            collection_num = driver.find_element(By.XPATH, './/div[@class="fav-btn-container"]').get_attribute('data-favdata')
            pic_img = driver.find_element(By.XPATH, './/div[@class="video-screenshot"]/img').get_attribute('src')
            try:
                el_key_words_1 = get_elements_by_xpath(driver, './/div[@class="tags"]/a')
            except:
                el_key_words_1 = []
            try:
                el_key_words_2 = get_elements_by_xpath(driver, './/div[@class="tags"]/span')
            except:
                el_key_words_2 = []

            for el in el_key_words_1:
                key_word = key_word + el.get_attribute('title') + ' '

            for el in el_key_words_2:
                key_word = key_word + el.get_attribute('title') + ' '

            pic_info['category_first'] = category_first
            pic_info['category_second'] = category_second
            pic_info['collection_num'] = collection_num
            pic_info['pic_img'] = pic_img
            pic_info['key_word'] = key_word

            return pic_info
        except:
            return False








if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    vjs = VJShi()
    try:
        sql_search = 'SELECT id, pic_id, pic_detail_url from vjshi_pic_info where id >3985 and pic_dl_num >10 and pic_img is null limit 1000'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        driver = browser()
        for row in rows:
            time.sleep(5)
            print(row['id'], row['pic_detail_url'])
            id = row['id']
            pic_id = row['pic_id']
            url = row['pic_detail_url']
            pic_info = vjs.vjshi_detial_info(url, driver)
            if pic_info:
                try:
                    update_sql = "UPDATE `vjshi_pic_info` " \
                                 "SET " \
                                 "`category_first`= '%s', " \
                                 "`category_second`= '%s', " \
                                 "`collection_num`= %d, " \
                                 "`pic_img`= '%s', " \
                                 "`key_word`= '%s' " \
                                 " WHERE (`id`=%d)" % (pic_info['category_first'],
                                                       pic_info['category_second'],
                                                       int(pic_info['collection_num']),
                                                       pic_info['pic_img'],
                                                       pic_info['key_word'],
                                                       int(id))
                    print(update_sql)
                    cursor.execute(update_sql)
                    cursor.connection.commit()
                    img_path = r'D:\vjshi\%d.jpg' % pic_id
                    dl_jpg(pic_info['pic_img'], img_path)
                except Exception as E:
                    print(E)


    finally:
        cursor.close()
        connection.close()
        driver.quit()
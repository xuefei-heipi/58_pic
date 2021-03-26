import requests
from lxml import etree
from envato_elements.common import *
import time

class EnvatoElement():

    def get_page_source(self, page_source, cursor):

        # 获取页面元素
        html = etree.HTML(page_source)
        # 页面所有图片元素
        result = html.xpath('.//div[@class="_2c8GJ3US"]/ul[@class="_3tOCfha1"]/li')
        print('当前页面素材数量 %d' % len(result))
        # 遍历当前页面所有素材
        for res in result:
            # pic_id = pic_title_e = pic_detail_url = pic_img_url = ''   /bookmarks/widget?item_id=9959555
            # 获取pic_id
            pic_id = res.xpath('.//a[@class="_3bLezeVQ _3dxbieth"]/@href')[0]
            pic_id = pic_id.split('-')[len(pic_id.split('-')) - 1]
            # 获取素材名称
            pic_title = res.xpath('.//a[@class="_3bLezeVQ _3dxbieth"]/@title')[0]
            # 获取素材 详情页链接
            pic_detail_url = res.xpath('.//a[@class="_3bLezeVQ _3dxbieth"]/@href')[0]
            pic_detail_url = 'https://elements.envato.com' + pic_detail_url
            if not is_pic_exist(pic_id, cursor):
                # pass
                insert_pic(pic_id, pic_detail_url, pic_title, cursor)

    def detail_info(self, page_source, id, cursor):

        # 获取页面元素
        html = etree.HTML(page_source)
        # 页面所有图片元素
        # pic_img_url = html.xpath('.//img[@class="ZmIhWAy-"]/@src')[0]
        pic_img_url = find_by_xpath(html, './/img[@class="ZmIhWAy-"]/@src', 0)
        # pic_mp4_url = html.xpath('.//a[@class="_22O4G05l"]/@href')[0]
        pic_mp4_url = find_by_xpath(html, './/a[@class="_22O4G05l"]/@href', 0)
        # first_category = html.xpath('.//div[@class="DdeHkWSY"][1]/a[2]/text()')[0]
        first_category = find_by_xpath(html, './/div[@class="DdeHkWSY"][1]/a[2]/text()', 0)
        # second_category = html.xpath('.//a[@class="_3Z5eaALu"]/text()')[0]
        second_category = find_by_xpath(html, './/a[@class="_3Z5eaALu"]/text()', 0)
        # application_supported = html.xpath('.//span[@class="_14FlqylH"]/text()')[0]
        application_supported = find_by_xpath(html, './/span[@class="_14FlqylH"]/text()', 0)
        try:
            attributes = html.xpath('.//table[@class="_3wBcrhm2"]/tbody/tr')
        except:
            attributes = []
        length = resolution = file_size = ''
        for att in attributes:
            # att_name = att.xpath('.//th/text()')[0]
            att_name = find_by_xpath(att,'.//th/text()', 0)
            # att_attribute = att.xpath('.//td/text()')[0]
            att_attribute = find_by_xpath(att,'.//td/text()', 0)
            if att_name == 'Length':
                length = att_attribute
            elif att_name == 'Resolution':
                resolution = att_attribute
            elif att_name == 'File Size':
                file_size = att_attribute
        tags = ''
        try:
            item_tags = html.xpath('.//div[@class="_1UnpPzWd"]/div')
        except:
            item_tags = []
        item_spans = html.xpath('.//div[@class="_1UnpPzWd"]/span')

        for itm in item_tags:
            itme = find_by_xpath(itm, './/a/text()', 0)
            tags = tags + itme + ','
        if len(item_spans) > 1:
            for itm_s in item_spans:
                itme = find_by_xpath(itm_s, './/a/text()', 0)
                tags = tags + itme + ','

        update_pic(cursor, id, pic_img_url, pic_mp4_url, first_category, second_category, application_supported,
               length, resolution, file_size, tags)
        # print(pic_img_url)
        # print(pic_mp4_url)
        # print(first_category)
        # print(second_category)
        # print(application_supported)
        # print(length)
        # print(resolution)
        # print(file_size)
        # print(tags)
if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    ee = EnvatoElement()
    driver = browser()
    driver.maximize_window()
    try:
        url = 'https://elements.envato.com/instagram-stories-pack-UENQHG6'
        driver.get(url)
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=800"
        driver.execute_script(js)
        try:
            driver.find_element_by_xpath('.//button[@class="_1SrXAO-p"]').click()
        except:
            pass
        time.sleep(2)
        page_source = driver.page_source
        ee.detail_info(page_source, 2617, cursor)
    finally:
        cursor.close()
        connection.close()



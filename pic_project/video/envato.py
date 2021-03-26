import requests
from lxml import etree
from video.common import *

class Envato(object):

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

        # url = 'https://videohive.net/category/premiere-pro-templates?page=%d&sort=sales' % page_num
        url = 'https://videohive.net/category/after-effects-project-files?page=%d&sort=sales' % page_num
        response = requests.get(url=url, headers=self.header, timeout=5)

        # 获取页面元素
        html = etree.HTML(response.text)
        # 页面所有图片元素
        result = html.xpath('.//ul[@class="_2tY3C"]/li')

        for res in result:
            pic_info = {}
            # pic_id = pic_title_e = pic_detail_url = pic_img_url = ''   /bookmarks/widget?item_id=9959555

            pic_id = res.xpath('.//span[@class="_1CDxH"]/a[2]/@href')[0].replace('/bookmarks/widget?item_id=', '')
            pic_title_e = res.xpath('.//h3[@class="_2WWZB"]/a/text()')[0]
            pic_detail_url = res.xpath('.//h3[@class="_2WWZB"]/a/@href')[0]
            # pic_img_url = res.xpath('.//div[@class="video-player"]/video/@poster')[0]
            print(pic_id, pic_title_e, pic_detail_url)


            # pic_info['pic_id'] = pic_id
            # pic_info['pic_title_e'] = pic_title_e
            # pic_info['pic_detail_url'] = pic_detail_url
            # # pic_info['pic_img_url'] = pic_img_url
            # pic_info['page_num'] = page_num

            sql_search = "select `id` from 58pic_envato_info where `pic_detail_url` = %s limit 1"
            # sql_search = "select pic_id from 58pic_competitor_pic where `c_id` = %s AND `act` = %s"
            if cursor.execute(sql_search, pic_detail_url):
                continue
            sql_insert = "insert into 58pic_envato_info (" \
                        "pic_id," \
                        "pic_title_e," \
                        "pic_detail_url," \
                        "page_num) values " \
                        "(%s, %s, %s, %s)"
            cursor.execute(sql_insert, [
                pic_id,
                pic_title_e,
                pic_detail_url,
                page_num
            ])
            cursor.connection.commit()

        # return pic_info


    def detail_page(self, id, url, cursor):

        # url = 'https://videohive.net/item/pet-store-intro-tv-show/1952833'

        try:
            response = requests.get(url=url, headers=self.header, timeout=5)

            # 获取页面元素
            html = etree.HTML(response.text)
            pic_key_word_e = ''
            pic_img_url = html.xpath('.//div[@class="video-preview-wrapper"]/a/img/@src')[0]
            pic_dl_num = ''.join(html.xpath('.//div[@class="sidebar-stats"]/div[1]/div/strong/text()')).replace('\n', '').replace(' ', '').replace(',', '')
            pic_keys = html.xpath('.//span[@class="meta-attributes__attr-tags"]/a')
            for pic_key in pic_keys:
                pic_key_word_e = pic_key_word_e + pic_key.xpath('.//text()')[0] + ','
            try:
                category_first_e = html.xpath('.//nav[@class="breadcrumbs h-text-truncate "]/a[3]/text()')[0]
            except:
                category_first_e = ''
            try:
                category_second_e = html.xpath('.//nav[@class="breadcrumbs h-text-truncate "]/a[4]/text()')[0]
            except:
                category_second_e = ''
            try:
                category_third_e = html.xpath('.//nav[@class="breadcrumbs h-text-truncate "]/a[5]/text()')[0]
            except:
                category_third_e = ''
            try:
                category_fourth_e = html.xpath('.//nav[@class="breadcrumbs h-text-truncate "]/a[6]/text()')[0]
            except:
                category_fourth_e= ''

            print(pic_img_url)
            print(pic_dl_num)
            print(pic_key_word_e)
            print(category_first_e)
            print(category_second_e)
            print(category_third_e)
            print(category_fourth_e)

            sql_update = 'UPDATE `58pic_envato_info` SET ' \
                         '`pic_img_url`= "%s", ' \
                         '`pic_dl_num`= %d ,' \
                         '`pic_key_word_e`= "%s",' \
                         '`category_first_e`= "%s",' \
                         '`category_second_e`= "%s",' \
                         '`category_third_e`= "%s",' \
                         '`category_fourth_e`= "%s"' \
                         ' WHERE (`id`=%d)' % (pic_img_url, int(pic_dl_num), pic_key_word_e,
                                               category_first_e, category_second_e,category_third_e, category_fourth_e, int(id))
            # print(sql_update)
            cursor.execute(sql_update)
            cursor.connection.commit()
        except Exception as E:
            print(E)

if __name__ == '__main__':
    # connection = get_sql_connection()
    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    # try:
    #     envatoV2 = Envato()
    #     for page_num in range(1, 61):
    #         envatoV2.category_page(page_num, cursor)
    # except Exception as E:
    #     print(E)
    # finally:
    #     cursor.close()
    #     connection.close()


    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT id, pic_detail_url FROM `58pic_envato_info` where category_first_e is null'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        envato = Envato()
        for row in rows:
            id = row['id']
            url = row['pic_detail_url']
            envato.detail_page(id, url, cursor)
    finally:
        cursor.close()
        connection.close()



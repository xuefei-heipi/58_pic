# -*- coding: utf-8 -*-
import requests
from lxml import etree
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from golden_words.nipic import NiPic
from golden_words.ibaotu import IBaoTu
from golden_words.miz import Miz
from golden_words.common import *
from time import sleep
import random
import threading

def insert_info(res, logger, nipic, miz, baotu, type):
    """

    :param res:
    :param logger:
    :param nipic:
    :param miz:
    :param baotu:
    :param type:
    :return:
    """
    try:

        connection = get_sql_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        # driver = create_daili_browser(2)
        search_word_id = res['s_id']
        search_word = res['keyword']
        if type == 1:
            pic_urls = nipic.search_nipic(search_word)
        elif type == 2:
            pic_urls = miz.search_miz(search_word)
        elif type == 3:
            pic_urls = baotu.search_baotu(search_word)
        for pic_url in pic_urls:
            print(pic_url)
            if not is_pic_exist(pic_url, cursor):
                time.sleep(random.randint(1,3))
                if type == 1:
                    # pic_info, driver = nipic.nipic_detail_page_webdriver(pic_url, driver)
                    pic_info = nipic.nipic_detail_page(pic_url)
                elif type == 2:
                    # pic_info, driver = miz.miz_detail_page_webdriver(pic_url, driver)
                    pic_info = miz.miz_detail_page(pic_url)
                elif type == 3:
                    # pic_info, driver = baotu.baotu_detail_page_webdriver(pic_url, driver)
                    pic_info = baotu.baotu_detail_page(pic_url)
                # 判断爬取的数据中是否有 素材id 和 img url
                if pic_info['pic_id'] != '' and pic_info['img_url'] != '':
                    # 爬取图片并且 上传 七牛 和 又拍
                    upload_pic_info = upload_pic(pic_info['pic_id'], pic_info['img_url'])
                    if upload_pic_info is not False:
                        pic_info['pic_url'] = pic_url
                        pic_info['upload_time'] = upload_pic_info['upload_time']
                        pic_info['qn_img_url'] = upload_pic_info['upload_img_url']
                        pic_info['search_word'] = search_word
                        pic_info['search_word_id'] = search_word_id

                        insert_pic(pic_info, cursor, logger)
                else:
                    # 网络原因可能访问后没有返回结果
                    logger.warning('%s 数据爬取失败' % pic_url)
                sleep(random.randint(1, 2))
        # import datetime
        # date_add = datetime.datetime.now().strftime('%Y%m%d')
        date_add = '20200930'
        # 更新58pic_compepitor_words 表对应的web爬取结果
        if type == 1:
            sql_update_web = 'update `58pic_compepitor_words` set `nipic` = 1 where date = "%s" and `s_id` = %d' \
                         % (date_add, int(search_word_id))
        elif type == 2:
            sql_update_web = 'update `58pic_compepitor_words` set `miz` = 1 where date = "%s" and `s_id` = %d' \
                         % (date_add, int(search_word_id))
        elif type == 3:
            sql_update_web = 'update `58pic_compepitor_words` set `ibaotu` = 1 where date = "%s" and `s_id` = %d' \
                         % (date_add, int(search_word_id))
        cursor.execute(sql_update_web)
        cursor.connection.commit()

        # 更新58pic_compepitor_words crawled如果 所有web都爬取结束
        search_sql_crawled = 'SELECT * FROM `58pic_compepitor_words` where`date` = "20200930" and `s_id` = %d limit 1' % int(search_word_id)
        cursor.execute(search_sql_crawled)
        res_crawled = cursor.fetchone()
        if res_crawled['nipic'] == 1 and res_crawled['miz'] == 1 and res_crawled['ibaotu'] == 1:
            sql_update_crawled = 'update `58pic_compepitor_words` set `crawled` = 1 where date = "%s" and `s_id` = %d' \
                         % (date_add, int(search_word_id))
            cursor.execute(sql_update_crawled)
            cursor.connection.commit()


    except ValueError:
        logger.warning("ip使用连续失败10次不能运行")
        return None
    except Exception as E:
        logger.warning(E)
    finally:
        # driver.quit()
        cursor.close()
        connection.close()


def run(rows, logger, nipic, miz, baotu, type):
    try:
        for row in rows:
            res = {}
            res['s_id'] = row['s_id']
            res['keyword'] = row['keyword']
            print(res)

            if len(res) > 0:
                insert_info(res, logger, nipic, miz, baotu, type)
    except:
        pass


if __name__ == '__main__':
    # import datetime
    # date = datetime.datetime.now().strftime('%Y%m%d')
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql_get_word1 = 'SELECT * FROM `58pic_compepitor_words` where `crawled` = 0 and `nipic`=0 and `date` = "20200930" and keyword <> "" and id < 9397;'
    sql_get_word2 = 'SELECT * FROM `58pic_compepitor_words` where `crawled` = 0 and `nipic`=0 and `date` = "20200930" and keyword <> "" and id BETWEEN 9396 and 11397 ;'
    sql_get_word3 = 'SELECT * FROM `58pic_compepitor_words` where `crawled` = 0 and `nipic`=0 and `date` = "20200930" and keyword <> "" and id > 11397;'

    cursor.execute(sql_get_word1)
    rows1 = cursor.fetchall()

    cursor.execute(sql_get_word2)
    rows2 = cursor.fetchall()

    cursor.execute(sql_get_word3)
    rows3 = cursor.fetchall()

    logger = write_log()
    nipic = NiPic(logger)
    miz = Miz(logger)
    baotu = IBaoTu(logger)
    try:
        # run(rows1, logger, nipic, miz, baotu, 1)
        # 线程处理
        threads = []
        t1 = threading.Thread(target=run, args=(rows1, logger, nipic, miz, baotu, 1,))
        t2 = threading.Thread(target=run, args=(rows2, logger, nipic, miz, baotu, 1,))
        t3 = threading.Thread(target=run, args=(rows3, logger, nipic, miz, baotu, 1,))
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)

        for thread in threads:
            thread.start()
            time.sleep(10)
            # thread.join()
        t1.join()
        t2.join()
        t3.join()

    except Exception as E:
        logger.warning(E)
    finally:
        cursor.close()
        connection.close()








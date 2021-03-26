import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
from concurrent.futures import ThreadPoolExecutor
from envatoV2.common import *

def main_dl(rows):
    for row in rows:
        img_name = row['pic_id']
        print(img_name)
        img_url = row['pic_img_url']
        pic_local_path = 'D:/envatoV2/%s.jpg' % img_name
        if not os.path.exists(pic_local_path):
            print('开始下载素材: %d' % img_name)
            dl_jpg(pic_local_path, img_url)

if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        # while True:
        sql_search_1 = 'SELECT * FROM `58pic_envatov2` where pic_img_url is not null limit 1, 8000'
        sql_search_2 = 'SELECT * FROM `58pic_envatov2` where pic_img_url is not null limit 8001, 13000'
        sql_search_3 = 'SELECT * FROM `58pic_envatov2` where pic_img_url is not null limit 13001, 18213'
        cursor.execute(sql_search_1)
        rows_1 = cursor.fetchall()
        cursor.execute(sql_search_2)
        rows_2 = cursor.fetchall()
        cursor.execute(sql_search_3)
        rows_3 = cursor.fetchall()
        row_list = [rows_1, rows_2, rows_3]
        max_pools = 3
        pool = ThreadPoolExecutor(max_workers=max_pools)
        for x in range(max_pools):
            pool.submit(main_dl, row_list[x])

        pool.shutdown()
            # time.sleep(600)
    except Exception as E:
        print(E)

    finally:
        cursor.close()
        connection.close()
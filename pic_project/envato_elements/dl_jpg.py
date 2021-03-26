import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
from envato_elements.common import *

if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        # while True:
        sql_search = 'SELECT * FROM `58pic_envato_element` where pic_img_url is not null'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        for row in rows:
            img_name = row['pic_id']
            print(img_name)
            img_url = row['pic_img_url']
            pic_local_path = 'D:/envato_elements/%s.jpg' % img_name
            if not os.path.exists(pic_local_path):
                dl_jpg(pic_local_path, img_url)

            # time.sleep(600)
    except Exception as E:
        print(E)

    finally:
        cursor.close()
        connection.close()
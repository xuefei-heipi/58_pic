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

try:
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql_unexpected_title_search = 'SELECT * FROM `58pic_competitive_info` where pic_title = "";'
    cursor.execute(sql_unexpected_title_search)
    rows = cursor.fetchall()
    logger = write_log()
    nipic = NiPic(logger)
    for row in rows:
        id = row['id']
        pic_url = row['pic_url']
        if 'http://www.huitu.com/' in pic_url:
            pic_title = nipic.nipic_detail_page(pic_url)['pic_title']

            upload_title = 'update 58pic_competitive_info set `pic_title` = "%s" where `id` = %d' % (pic_title, id)
            cursor.execute(upload_title)
            cursor.connection.commit()



finally:

    cursor.close()
    connection.close()
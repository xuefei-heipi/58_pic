import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from golden_words.common import *

def re_firmly():
    try:
        connection = get_sql_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql_search = 'SELECT * FROM `58pic_competitive_info`;'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        for row in rows:
            info = {
                1: 'nipic',
                2: 'miz',
                3: 'ibaotu'
            }
            id = row['id']
            print(id)
            web_id = row['competitive_web']
            search_word_id = row['search_word_id']
            update_search = 'update 58pic_compepitor_words set %s = 1 where `s_id` = %d' % (info[web_id], search_word_id)
            cursor.execute(update_search)
            cursor.connection.commit()
    finally:
        connection.close()
        cursor.close()

def replace_zh():
    try:
        connection = get_sql_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql_search = 'SELECT * FROM `58pic_competitive_info` where `competitive_web` = 3;'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        for row in rows:
            id = row['id']
            pic_id = row['pic_id']
            pic_id = ''.join(filter(str.isdigit, pic_id))
            print(id)
            update_search = 'update 58pic_competitive_info set `pic_id` = "%s" where `id` = %d' % (pic_id, id)
            cursor.execute(update_search)
            cursor.connection.commit()
    finally:
        connection.close()
        cursor.close()

replace_zh()
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from mysql_test.common import get_sql_connection
import pymysql
import csv

if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    uids = [
        '32607860',
        '32606934',
        '32606928',
        '32610449',
        '32607820',
        '32607036',
        '32701305',
        '32609480',
        '32609418',
        '32609704',
        '32610040',
        '32606096',
        '54805481',
        '56673783',
        '45826524'
    ]
    try:
        for uid in uids:
            sql_fav_ids_num = "SELECT id FROM `58pic_favorites` WHERE `uid` = %s " % uid

            cursor.execute(sql_fav_ids_num)

            rows = cursor.fetchall()
            file_name = '%s.csv' % uid
            with open(file_name, 'w+', newline='') as file:
                writer = csv.writer(file, dialect='excel',)
                # rows = [{'id': 5772396}, {'id': 18296938}]
                for row in rows:
                    # print(row['id'])
                    table_id = row['id'] % 80
                    sql_pic_duplicate = "SELECT id FROM `58pic_favorites_info_%d` WHERE `favor_id` = '%d'" % (table_id, row['id'])
                    sql_pic_no_duplicate = "SELECT id FROM `58pic_favorites_info_%d` WHERE `favor_id` = '%d' GROUP BY picid" % (table_id, row['id'])
                    cursor.execute(sql_pic_duplicate)
                    duplicate_nums = len(cursor.fetchall())
                    cursor.execute(sql_pic_no_duplicate)
                    no_duplicate_nums = len(cursor.fetchall())
                    if duplicate_nums != no_duplicate_nums:
                        print(row['id'], duplicate_nums, no_duplicate_nums)
                        writer.writerow([row['id'], duplicate_nums, no_duplicate_nums])

    except Exception as E:
        print(E)

    finally:
        cursor.close()
        connection.close()



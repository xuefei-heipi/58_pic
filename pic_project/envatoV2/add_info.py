from envatoV2.envato import Envato
from envatoV2.common import *


if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    ee = Envato()
    try:
        sql_search = 'SELECT * FROM `58pic_envatov2` where pic_img_url is null;'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        for row in rows:
            pic_id = row['pic_id']
            print(pic_id)
            url = row['pic_detail_url']
            try:
                ee.get_info(url, pic_id, cursor)
            except Exception as E:
                print(E)
    except Exception as E:
        print(E)

    finally:
        cursor.close()
        connection.close()

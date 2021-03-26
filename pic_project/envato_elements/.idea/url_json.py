from envato_elements.common import *

if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        sql_search = 'SELECT * FROM `58pic_envato_element`'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        with open('./pic.json', 'w+') as file:
            for row in rows:
                img_name = row['pic_id']
                img_url = row['pic_detail_url']
                res = '{"pid":"%s","purl":"%s"},' % (img_name, img_url)

                file.writelines(res+'\n')


    except Exception as E:
        print(E)

    finally:
        cursor.close()
        connection.close()
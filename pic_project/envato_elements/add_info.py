from envato_elements.common import *
from envato_elements.envato_element import EnvatoElement
import time

if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    ee = EnvatoElement()
    driver = browser()
    driver.maximize_window()
    try:
        sql_search = 'SELECT * FROM `58pic_envato_element` where pic_img_url = "" ;'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        for row in rows:
            # url = 'https://elements.envato.com/instagram-stories-pack-UENQHG6'
            url = row['pic_detail_url']
            id = row['id']
            print(id)
            driver.get(url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=750"
            driver.execute_script(js)
            try:
                driver.find_element_by_xpath('.//button[@class="_1SrXAO-p"]').click()
            except:
                pass
            time.sleep(2)
            page_source = driver.page_source
            ee.detail_info(page_source, id, cursor)
    finally:
        cursor.close()
        connection.close()
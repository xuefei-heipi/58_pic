from envato_elements.common import *
from envato_elements.envato_element import EnvatoElement
import time
if __name__ == '__main__':
    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        driver = browser()
        for x in range(1, 51):
            print(x)
            # 'https://elements.envato.com/video-templates/kit/compatible-with-premiere-pro/sort-by-popular/pg-%d'
            # url = 'https://elements.envato.com/video-templates/kit/compatible-with-apple-motion/sort-by-popular'
            url = 'https://elements.envato.com/video-templates/kit/compatible-with-final-cut-pro/sort-by-popular'
            # url = 'https://elements.envato.com/video-templates/kit/compatible-with-premiere-pro/sort-by-popular/pg-%d' % x
            driver.get(url)
            time.sleep(3)
            page_source = driver.page_source
            ee = EnvatoElement()
            ee.get_page_source(page_source, cursor)
        driver.quit()

    finally:
        cursor.close()
        connection.close()
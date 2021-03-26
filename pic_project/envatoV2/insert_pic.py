
from envatoV2.common import *
from envatoV2.envato import Envato

if __name__ == '__main__':

    connection = get_sql_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    envtao = Envato()
    try:
        # url = 'https://videohive.net/search/pack?page=1&sort=sales'


        urls = [
        'https://videohive.net/category/after-effects-project-files/elements?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/titles?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/logo-stings?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/openers?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/broadcast-packages?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/product-promo?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/video-displays?page=%d&term=kit',
        'https://videohive.net/category/after-effects-project-files/infographics?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/backgrounds?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/elements?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/overlays?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/transitions?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/bugs?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/miscellaneous?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/interface-effects?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/lower-thirds?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/infographics?page=%d&term=kit',
        'https://videohive.net/category/motion-graphics/revealer?page=%d&term=kit'
        ]
        for url in urls:
            for page_num in range(1, 61):
                print(page_num)
                # url = 'https://videohive.net/category/after-effects-project-files/openers?page=%d&term=pack' % page_num
                url_ = url % page_num
                print(url_)
                try:
                    if not envtao.get_page_source(url_, cursor):
                        break
                except Exception as E:
                    print(E)

    finally:
        cursor.close()
        connection.close()
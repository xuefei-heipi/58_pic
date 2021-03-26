# -*- coding: utf-8 -*-
# 面向对象
# 百度翻译 -- 网页版(自动获取token,sign)
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests
import js2py
import json
import re
import time
from video.common import *


class WebFanyi:
    """百度翻译网页版爬虫"""
    def __init__(self,query_str):
        self.session = requests.session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.session.headers = headers
        self.baidu_url = "https://www.baidu.com/"
        self.root_url = "https://fanyi.baidu.com/"
        self.lang_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/v2transapi"
        self.query_str = query_str

    def get_token_gtk(self):
        """
        获取token和gtk(用于合成Sign)
        :return:
        """

        self.session.get(self.root_url)
        resp = self.session.get(self.root_url)
        html_str = resp.content.decode()
        # print(html_str)
        token = re.findall(r"token: '(.*?)'", html_str)[0]
        gtk = re.findall(r"window.gtk = '(.*?)'", html_str)[0]
        return token,gtk

    def generate_sign(self,gtk):
        """生成sign"""
        # 1. 准备js编译环境
        context = js2py.EvalJs()
        with open('webtrans.js', encoding='utf8') as f:
            js_data = f.read()
            js_data = re.sub("window\[l\]",'"'+gtk+'"',js_data)
            # js_data = re.sub("window\[l\]", "\"{}\"".format(gtk), js_data)
            # print(js_data)
            context.execute(js_data)
        sign = context.e(self.query_str)
        # print(sign)
        return sign

    def lang_detect(self):
        """
        获取语言转换类型.eg: zh-->en
        :return:
        """

        lang_resp = self.session.post(self.lang_url,data={"query":self.query_str})
        lang_json_str = lang_resp.content.decode()  # {"error":0,"msg":"success","lan":"zh"}
        lan = json.loads(lang_json_str)['lan']
        to = "en" if lan == "zh" else "zh"
        return lan,to


    def parse_url(self,post_data):

        trans_resp = self.session.post(self.trans_url,data=post_data)
        print(trans_resp)
        if trans_resp.status_code != 200:
            time.sleep(5)
        trans_json_str = trans_resp.content.decode()
        # print(trans_json_str)
        trans_json = json.loads(trans_json_str)
        result = trans_json["trans_result"]["data"][0]["dst"]



        # print("{}: {}".format(self.query_str,result))
        # print(result)
        return result

    def run(self):
        """实现逻辑"""

        # 1.获取百度的cookie,(缺乏百度首页的cookie会始终报错998)
        self.session.get(self.baidu_url)
        # 2. 获取百度翻译的token和gtk(用于合成sign)
        token, gtk = self.get_token_gtk()
        # 3. 生成sign
        sign = self.generate_sign(gtk)
        # 4. 获取语言转换类型.eg: zh-->en
        lan, to = self.lang_detect()
        # 5. 发送请求,获取响应,输出结果
        post_data = {
            "from": lan,
            "to": to,
            "query": self.query_str,
            "transtype": "realtime",
            "simple_means_flag": 3,
            "sign": sign,
            "token": token
        }

        return self.parse_url(post_data)



if __name__ == '__main__':
    # web_fanyi = WebFanyi('Elegant christmas element collection with realistic design')
    # print(web_fanyi.run())
    try:
        connection = get_sql_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql_search = "SELECT * FROM `58pic_envato_info` where category_fourth_e <> '' and category_fourth_zh = '';"
        # sql_search = 'SELECT * FROM `58pic_envato_info` where id = 1170;'
        cursor.execute(sql_search)
        rows = cursor.fetchall()
        for row in rows:
            id = row['id']
            print(id)
            pic_title_e = row['pic_title_e']
            pic_key_word_e = row['pic_key_word_e'].replace(',', ' , ')
            category_first_e = row['category_first_e']
            category_second_e = row['category_second_e']
            category_third_e = row['category_third_e']
            category_fourth_e = row['category_fourth_e']

            # print(pic_title_e)
            # print(pic_key_word_e)
            # print(category_first_e)
            # print(category_second_e)
            # print(category_third_e)
            # print(category_fourth_e)

            try:
                if pic_title_e:
                    pic_title_zh = WebFanyi(pic_title_e).run()
                else:
                    pic_title_e= ''
                if pic_key_word_e:
                    pic_key_word_zh = WebFanyi(pic_key_word_e).run()
                else:
                    pic_key_word_zh = ''
                if category_first_e:
                    category_first_zh = WebFanyi(category_first_e).run()
                else:
                    category_first_zh = ''
                if category_second_e:
                    category_second_zh = WebFanyi(category_second_e).run()
                else:
                    category_second_zh = ''
                if category_third_e:
                    category_third_zh = WebFanyi(category_third_e).run()
                else:
                    category_third_zh = ''
                if category_fourth_e:
                    category_fourth_zh = WebFanyi(category_fourth_e).run()
                else:
                    category_fourth_zh = ''
            except:
                import time
                time.sleep(10)
                connection


            # print(pic_title_zh)
            # print(pic_key_word_zh)
            # print(category_first_zh)
            # print(category_second_zh)
            # print(category_third_zh)
            # print(category_fourth_zh)

            sql_update = 'UPDATE `58pic_envato_info` SET ' \
                         '`pic_title_zh`= "%s", ' \
                         '`pic_key_word_zh`= "%s" ,' \
                         '`category_first_zh`= "%s",' \
                         '`category_second_zh`= "%s",' \
                         '`category_third_zh`= "%s",' \
                         '`category_fourth_zh`= "%s"' \
                         ' WHERE (`id`=%d)' % (pic_title_zh, pic_key_word_zh, category_first_zh,
                                               category_second_zh, category_third_zh,category_fourth_zh, int(id))
            cursor.execute(sql_update)
            cursor.connection.commit()

    except Exception as E:
        print(E)
    finally:
        cursor.close()
        connection.close()
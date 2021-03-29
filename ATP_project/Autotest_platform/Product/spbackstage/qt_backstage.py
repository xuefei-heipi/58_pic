#-*-conding:utf-8-*-
import csv
from time import sleep

import requests
from urllib import request
import json

import time
import re

def get_token():
    url = 'http://qt.58pic.com/index.php?r=web/login'

    datas = {
        'username': '薛飞',
        'password': 'XUE5430782',
    }
    headers = {
        'Authorization': 'Basic aGNrajU4cGljOkh4eEpRdDhQMUN4Mk9sbw=='
    }
    response = requests.post(url=url, data=datas, headers=headers)


    return '&access-token=' + response.json()['data']['token']


class QTBackstage():
    '''
    千图后台
    '''

    def __init__(self):
        self.access_token = get_token()
        self.add_url = 'http://sp.58pic.com/index.php?m=userMng&a=addvip' + self.access_token
        self.add_user_url = 'http://sp.58pic.com/index.php?m=tools&a=addUser' + self.access_token
        self.add_uid_to_white_list_url = 'http://sp.58pic.com/index.php?m=auditstools&a=loginallow' + self.access_token

        self.cookies = {
            '58pic_id': '368',
            '58pic_name': '%22%5Cu859b%5Cu98de%22',
            'PHPSESSID': 'ggji8shk5aps3c95onsrs45b51',
        }


        self.headers = {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,ar;q=0.8,en;q=0.7',
            'Authorization': 'Basic aGNrajU4cGljOkh4eEpRdDhQMUN4Mk9sbw==',
            # 'Cache-Control': 'max-age=0',
            # 'Connection': 'keep-alive',
            # 'Cookie': 'qt_visitor_id=%226ae59061bb91c004e0e8d280f21fa020%22; qt_ur_type=2; awake=0; FIRSTVISITED=1554144933.613; qt_type=2; ISREQUEST=1; qt_risk_visitor_id=%22a2d483553d786a535b34b2dfa1aff5b3%22; qiantudata2018jssdkcross=%7B%22distinct_id%22%3A%22169da41b71a46e-0740c40fb76ae9-5701631-2073600-169da41b71b91%22%2C%22props%22%3A%7B%22latest_traffic_pic_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22latest_referrer%22%3A%22%22%2C%22latest_referrer_host%22%3A%22%22%2C%22latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; qt_createtime=1553702400; qt_addtime=%222019-03-28%22; qt_updatetime=%222019-04-04%22; funnel_sponsor=4; history_search=%22%7B%5C%22%25B9%25FA%25BB%25D5_%5C%22%3A%5C%22%5C%5C%5C%2Ftupian%5C%5C%5C%2Fguohui.html%5C%22%7D%22; showAd:6ae59061bb91c004e0e8d280f21fa020=%22w6SIEgLKiJOIC5HVD3fKoJzHztu8mdyXyMi8mwmWmdrLmgu7zdi7mgyYmwzHmdiWiIWIywr5zxj3AxnLCL2Pzci9iJeIlcj3DxjUiJOZlcjZAg26x6rPBwvZiJO5lcjSyxn3x6nOB6DFDgLTzsi9mtu4nta3mZqZmh3SEYj7AwqIoIjZAg26qwq9nMfLntKWnJfIyJKXyZaWnguWztHKmJGWzJiXzMeWmJaIlcjHzhzLCNrPC5vYx5LKiJOInsiSiNr4CM7IoIiXiIWIC5HVD423Aw4LCYi9iJqWiIWIBgfZDf2ZAg26x6rPBwuIoJe4ntqXndiYmZf2lhSIEgLKiJOIC5HVD3fKoJzHztu8mdyXyMi8mwmWmdrLmgu7zdi7mgyYmwzHmdiWiIWIywr5zxj3AxnLCL2Pzci9iJmIlcj3DxjUiJOXlcjZAg26x6rPBwvZiJOXmcWIBgfZDf2ZAg26x6rPBwuIoJe4ntqYntKYmtb2xq%3D%3D%22; imgCodeKey=%22f2bc20bcb01d0da9e61c2de1fd62d54e%22; success_target_path=%22https%3A%5C%2F%5C%2Fwww.58pic.com%5C%2Findex.php%3Fm%3Duserinfo%26a%3DgetImgCaptch%26v%3D1555318414465%22; WEBPARAMS=is_pay=1; qt_uid=0; 58pic_id=%22368%22; 58pic_name=%22%5Cu859b%5Cu98de%22; 58pic_level=%220%22; Hm_lvt_41d92aaaf21b7b22785ea85eb88e7cea=1554807698,1555036523,1555292375,1555401537; Hm_lvt_644763986e48f2374d9118a9ae189e14=1554807698,1555036524,1555292375,1555401538; referer=%22https%3A%5C%2F%5C%2Fwww.58pic.com%5C%2Fpiccate%5C%2F2-130-375.html%22; qt_utime=1555402514; PHPSESSID='+ str(phpsessid),
            # 'Host': 'sp.58pic.com',
            # 'Origin': 'http://sp.58pic.com',
            # 'Upgrade-Insecure-Requests': '1',
            'X-Requested-With': 'XMLHttpRequest',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

    def add_vip(self, uid, vip_type, limit, time_type, time_value, reason):
        '''
        添加vip
        :param uid:  需要添加的账号id   int
        :param vip_type: 1 共享  2 原创  3 办公  int
        :param limit: 0 海量  1 每日受限20次   2 每日受限10次（办公）  int
        :param time_type: 1 输入天数， 2 到期时间， 3 终生  int
        :param time_value: 5 ，    2018-12-1      无需传   int  string
        :param reason: 添加原因   string
        :return:
        '''
        #数据
        datas = {
            'uid': uid,
            'vip_type': vip_type,
            'limit': limit,
            'time_type': time_type,
            'time_value': time_value,
            'reason': reason
        }
        #获取返回值
        response = requests.request('post', self.add_url, cookies=self.cookies, data=datas, headers=self.headers)
        if json.loads(response.text)['info'] == '添加成功！':
            if datas['vip_type'] == 1:
                print('uid：%s：共享VIP添加成功' % str(datas['uid']))
            elif datas['vip_type'] == 2:
                print('uid：%s：原创VIP添加成功' % str(datas['uid']))
            else:
                print('uid：%s：办公VIP添加成功' % str(datas['uid']))
        else:
            print(json.loads(response.text)['info'])

    def get_uid(self, username , password):
        '''
        获取账号uid
        :param username: 用户名
        :param password: 密码
        :return: uid
        '''
        # datas = {
        #     'm': 'userMng',
        #     'a': 'vip',
        #     'uid': '',
        #     'name': username,
        #     'phone': '',
        #     'email': ''
        # }
        # # print(datas)
        # url = 'http://sp.58pic.com/?m=userMng&a=vip&uid=&name=' + str(username) + '&phone=&email='
        # response = requests.request('get', url, cookies=self.cookies, data=datas, headers=self.headers)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(response.text)
        # print(soup.find(id='contentid').text)
        # if username == soup.find_all('td')[8].text:
        #     uid = soup.find(id='contentid').text
        #     print(uid)
        #     return uid
        # else:
        #     return None
        login_by_passwd_new_request_url = 'https://www.58pic.com/index.php?m=userinfo&a=loginByPasswdNew' + self.access_token
        datas = {
            'username': username,
            'userpass': password
        }
        response = requests.post(url=login_by_passwd_new_request_url, data=datas)
        print(response)
        print(response.cookies)
        new_cookie = response.cookies.get('risk_forbid_login_uid')
        # print(new_cookie)
        uid = str(new_cookie).replace('%22', '').split('%')[0]
        print(uid)
        return  uid



    def creat_account(self, username):
        '''
        创建账号
        :param username: 账号用户名
        :return: uid 返回账号uid
        '''
        datas = {
            'days': 0,
            'pwd': '123456',
            'usernames': username
        }
        requests.request('post', self.add_user_url, cookies=self.cookies, data=datas, headers=self.headers)
        uid = self.get_uid(username)
        if uid != None:
            # print("创建账号 %s 成功" %username)
            return uid

    def add_uid_to_white_list(self, uid):
        '''
        将uid添加白名单 登录不需要绑定手机号
        :param uid:
        :return:
        '''
        datas = {
            'ids': uid,
            'action': 'save'
        }
        response = requests.request('post', self.add_uid_to_white_list_url, cookies=self.cookies, data=datas, headers=self.headers)
        # print(response.status_code)
        if response.status_code == 200:
            print('uid%s添加白名单成功' %str(uid))

    def get_user_pic_download_url(self, uid, page_num, file):
        '''
        获取用户上传素材的下载链接
        :param uid: 用户uid
        :param page_num: 以通过列表的页数
        :return:
        '''
        #全部素材url
        url = 'http://sp.58pic.com/index.php?m=Sucai&a=all&pid=&uid=' + str(uid) +'&title=&ptid=&theme_id=0&' \
              'style_id=&industry=&kid=&bigclass=&pic=&is_zb_search=&shtime=&yc=&uptime=&subtime=&page=' + str(page_num) + self.access_token


        #已驳回url
        # url = 'http://sp.58pic.com/index.php?m=Sucai&pid=&uid='+ str(uid) + \
        #       '&title=&ptid=&theme_id=0&style_id=&industry=&kid=&bigclass=&source=&is_zb_search=&shtime=&yc=&first_sub=&uptime=&subtime=&score_s=&score_e=&pic_status=refuse&' \
        #       'page='+ str(page_num)

        responses = requests.request('get', url=url, cookies=self.cookies, headers=self.headers) #获取返回值

        response_href1 = re.findall('href=\"/index.php\?m=Sucai&a=downloadRarFile&id=(.*?)\"', responses.text, re.S) #用正则匹配返回

        # print(response_href1)
        #没有链接停止查询
        if len(response_href1) == 0:
            return 0
        for x in response_href1:
            x = 'http://sp.58pic.com/index.php?m=Sucai&a=downloadRarFile&id=' + x + self.access_token
            x = self.get_302_dl_url(x)
            x_feed = x + '\r\n'
            try:
                #判断链接是否能够访问
                if request.urlopen(x, timeout=0.5).status == 200:
                    file.write(x_feed)
                    file.write('\r\n')
                    print(x)
            except:
                pass

        #有链接继续下一页
        return 1

    def get_302_dl_url(self, url):
        '''
        通过302跳转获取下载地址
        :param url: 第一层地址
        :return: 下载地址
        '''
        #获取第二层地址，注意不允许自动302跳转 allow_redirects=Fals
        response = requests.request('get', url=url, cookies=self.cookies, headers=self.headers, allow_redirects=False)
        url_302_1 = response.headers['Location']

        # 获取第三层地址，注意不允许自动302跳转 allow_redirects=Fals
        response_302_1 = requests.request('get', url=url_302_1, cookies=self.cookies, headers=self.headers, allow_redirects=False)

        return response_302_1.headers['Location']

    def change_pic_format(self, pic_id, old_format_id, new_format_id):
        '''
        修改素材属性
        :param pic_id: 素材id
        :param old_format_id: 素材旧格式id
        :param new_format_id: 素材新格式id
        :return:
        '''
        #接口链接
        url = 'http://sp.58pic.com/index.php?m=Sucai&a=editFormat&pic_id='+ str(pic_id)\
              +'&old_format_id=' + str(old_format_id)\
              +'&new_format_id=' + str(new_format_id) + self.access_token

        #请求接口
        response = requests.request('get', url=url, cookies = self.cookies, headers = self.headers)
        print(response.text)

    def delete_pic(self, pic_id):
        '''
        后台删除素材
        :param pic_id: 素材id
        :return:
        '''
        try:
            url = 'http://sp.58pic.com/index.php?m=Sucai&a=delPic' + self.access_token
            datas = {
                'picid': pic_id,
                'reason': '该用户涉嫌大范围抄袭，所有作品下架， 需求人  扬芳'
            }
            response = requests.post(url=url, cookies=self.cookies, data=datas, headers=self.headers).status_code
            print(response)
            if response == 200:
                print('%s:删除成功！' %pic_id)
            else:
                print('删除素材%s失败' %pic_id)
        except:
            print('删除素材%s失败' %pic_id)

    def pic_reject(self, pic_id):

        datas = {
            'did': '6',
            'isyc': '1',
            'isno': '0',
            'reason': '猴子音乐千图在线下线的作品',
            'status': '0',
            'id': pic_id,
            'themeid': '7313',

        }
        try:
            url = 'http://sp.58pic.com/index.php?m=Sucai&a=checkPic' + self.access_token
            response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)
            print(response.text)
            if response.status_code == 200:
                print('%s :素材驳回完成' % pic_id)
            else:
                print('%s :素材驳回失败' % pic_id)
        except:
            print('%s :素材驳回失败' % pic_id)


    def clear_browse_record(self, uid):
        '''
        清除账号的浏览记录
        :param uid:
        :return:
        '''
        datas = {
            'uid': uid
        }
        url = 'http://sp.58pic.com/index.php?m=auditstools&a=ajaxGetUserShowLimit' + self.access_token
        response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)
        # print(response.status_code)


    def add_forbidden_dl(self, uid, reason):
        '''
        下载终生限制
        :param uid:
        :return:
        '''

        datas = {
            'type': 1,
            'uid': uid,
            'range': 2,
            'expire': 0,
            'days': 0,
            'forbid_reason': 8,
            'reason': reason
        }

        url = 'http://sp.58pic.com/index.php?m=riskControlSystem&a=ajaxRiskForbiddenAdd' + self.access_token
        response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)

        if response.status_code == 200:
            print('%s :下载封禁添加完成' %uid)
        else:
            print('%s :下载封禁添加失败' %uid)


    def add_integral(self, uid, integral, reason):
        '''
        添加积分
        :param uid:  用户id
        :param integral: 积分
        :param reason: 原因
        :return:
        '''

        url = 'http://sp.58pic.com/?m=userMng&a=addQtb' + self.access_token
        datas = {
            'id': uid,
            'deal_type': 1,
            'qtb': integral,
            'reason': reason,
        }
        try:
            response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)

            if response.status_code == 200:
                print('%s : 积分添加成功' %uid)
            else:
                print('%s : 积分添加失败' % uid)
        except Exception as E:
            print(E)
            print('%s : 积分添加失败' % uid)

    def move_favor_owner(self, old_owner, favor_id, new_owner):
        '''
        修改收藏夹归属
        :param old_owner: 收藏夹老拥有者
        :param favor_id: 收藏夹的id
        :param new_owner: 收藏夹新拥有者
        :return:
        '''

        url = 'http://sp.58pic.com/?m=favorites&a=moveFavorOwner' + self.access_token

        datas = {
            'oldOwner': old_owner,
            'favor_id': favor_id,
            'newOwner': new_owner
        }

        try:
            response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)

            if response.status_code == 200:
                print('%s : 收藏夹转移成功' % favor_id)
            else:
                print('%s : 收藏夹转移失败' % favor_id)
        except Exception as E:
            print(E)
            print('%s : 收藏夹转移失败' % favor_id)

    def move_delpic_owner(self, old_uid=None, new_uid=58129708, is_id_list=1):
        '''
        修改删除素材的拥有者，用户很多情况下不需要被删除的无版权素材
        :param new_uid: 新用户
        :param old_uid: 旧用户id
        :param is_id_list: 是否查看要迁移素材的id，1 要查询但不迁移   非1  查询迁移
        :return:
        '''

        if is_id_list != 1:
            url = 'http://sp.58pic.com/index.php?m=getTempData&a=delNoCprightPic&new_uid=%s&old_uid=%s' % (new_uid, old_uid) + self.access_token
        else:
            url = 'http://sp.58pic.com/index.php?m=getTempData&a=delNoCprightPic&new_uid=%s&old_uid=%s&is_id_list=1' % (new_uid, old_uid) + self.access_token
        try:
            response = requests.request('get', url, cookies=self.cookies, headers=self.headers)
            if response.status_code == 200:
                print({'new_uid, old_uid'}, {new_uid, old_uid})
                if is_id_list != 1:
                    print('迁移成功！迁移的素材id：')
                    for pic_id in response.json()['data']['pic_id_list']:
                        print(pic_id)
                else:
                    print('需要迁移的素材id：')
                    for pic_id in response.json()['data']:
                        print(pic_id)

            else:
                print('迁移失败！')
        except:
            print('迁移失败！')

    def pic_material(self, pic_id, pic_type):
        '''
        图片自动套样机
        :param pic_id:  素材id
        :param pic_type: 素材种类  1 背景  2 元素
        :return:
        '''

        if pic_type == 1:

            url = 'http://sp.58pic.com/index.php?m=material&a=checkok4' + self.access_token

            datas = {
                'pic_id': pic_id
            }
        elif pic_type == 2:
            url = 'http://sp.58pic.com/index.php?m=material&a=designYj' + self.access_token
            datas = {
                'pic_id': pic_id,
                'color': 1
            }
        else:
            print('素材种类错误')
            return None

        try:
            response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)

            if response.status_code == 200:

                print('%s : 素材套样机成功' % pic_id)
            else:
                print('%s : 素材套样机失败' % pic_id)
        except Exception as E:
            print(E)
            print('%s : 素材套样机失败' % pic_id)

    def change_password(self, uid, new_password):
        '''
        修改密码
        :param uid:
        :param new_password:
        :return:
        '''
        url = 'http://sp.58pic.com/?m=auditstools&a=reGenPWD&uid=%s&pwd=%s&w=wtf' %(uid, new_password) + self.access_token

        try:
            response = requests.request('post', url, cookies=self.cookies,  headers=self.headers)

            if response.status_code == 200:

                print('%s : 修改密码成功' % uid)
            else:
                print('%s : 修改密码失败' % uid)
        except Exception as E:
            print(E)
            print('%s : 修改密码失败' % uid)

    def sent_message(self, uid, redeem_code):
        '''
        给用户发送站内信  这里内容使用在 发送爱奇艺兑换码
        :param uid: 用户uid
        :param redeem_code: 兑换码
        :return:
        '''
        url = 'http://sp.58pic.com/?m=MessageSystem&a=add&action=' + self.access_token

        datas = {
            'title': '春节充值599充值送爱奇艺VIP',
            'main_text': '兑换码: %s 兑换码使用流程：http://mrw.so/5fjnbK' % redeem_code,
            #https://www.58pic.com/index.php?m=Blog&a=detail&blog=732
            'jump_url': 'https://www.58pic.com/u/%s/message/' % uid,
            'record': '春节充值599充值送爱奇艺VIP',
            'send_type': 1,
            'user_type': 1,
            'input_user': uid,
            'cron_time': '1',
            'over_time': '2020-01-15 00:00:00',
            'user_file': ''
        }

        try:
            response = requests.request('post', url, data=datas, cookies=self.cookies,  headers=self.headers)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:

                print('%s : message发送成功' % uid)
            else:
                print('%s : message发送失败' % uid)
        except Exception as E:
            print(E)
            print('%s : message发送失败' % uid)


    def OGC_change_info(self, id, field_type, value):
        '''
        修改OGC信息
        :param id:  信息id  不是uid
        :param field_type:   身份证号：1   手机号： 其他
        :param value:
        :return:
        '''

        if field_type == 1:
            field = 'id_card'
        else:
            field = 'phone'

        url = 'http://sp.58pic.com/index.php?m=ogcshenheNew2&a=updateField' + self.access_token
        datas = {
            'id': id,
            'field': field,
            'value': value
        }
        try:
            response = requests.request('post', url, data=datas, cookies=self.cookies,  headers=self.headers)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:

                print('%s : 修改信息成功' % id)
            else:
                print('%s : 修改信息失败' % id)
        except Exception as E:
            print(E)
            print('%s : 修改信息失败' % id)

    def UGC_change_info(self, id, field_type, value):
        '''
        修改UGC信息
        :param id:  信息id  不是uid
        :param field_type:   身份证号：1   手机号： 其他
        :param value:
        :return:
        '''

        if field_type == 1:
            field = 'id_card'
        else:
            field = 'phone'

        url = 'http://sp.58pic.com/index.php?m=integralMoney&a=updateField' + self.access_token
        datas = {
            'id': id,
            'field': field,
            'value': value
        }
        try:
            response = requests.request('post', url, data=datas, cookies=self.cookies,  headers=self.headers)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:

                print('%s : 修改信息成功' % id)
            else:
                print('%s : 修改信息失败' % id)
        except Exception as E:
            print(E)
            print('%s : 修改信息失败' % id)

    def update_code_shop(self, id, code):
        '''
        更新积分商城后台兑换码
        :param id:
        :param code:
        :return:
        '''
        url = 'http://sp.58pic.com/index.php?m=shop&a=updateCode' + self.access_token
        datas = {
            'id': id,
            'code': code
        }
        try:
            response = requests.request('post', url, data=datas, cookies=self.cookies, headers=self.headers)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:

                print('%s : 更新订单成功' % id)
            else:
                print('%s : 更新订单失败' % id)
        except Exception as E:
            print(E)
            print('%s : 更新订单失败' % id)

    def update_express_shop(self, id, express, expressNo):
        '''

        :param id:
        :param express:
        :param expressNo:
        :return:
        '''
        url = 'http://sp.58pic.com/index.php?m=shop&a=updateExpress' + self.access_token
        datas = {
            'id': id,
            'express': express,
            'expressNo': expressNo
        }
        try:
            response = requests.request('post', url, data=datas, cookies=self.cookies, headers=self.headers)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:

                print('%s : 更新订单成功' % id)
            else:
                print('%s : 更新订单失败' % id)
        except Exception as E:
            print(E)
            print('%s : 更新订单失败' % id)

    def revise_qy_vip_time(self, qy_id , vip_type, end_time):
        """
        修改企业vip时间
        :param qy_id:  企业id
        :param vip_type:    修改vip的类型    1:基础版    2: 专业版   3：旗舰版  5： 转售版
        :param end_time:    企业vip的结束时间   2030 - 01 - 01
        :return:
        """
        url= 'http://sp.58pic.com/?m=qiyeV2Ajax&a=ajaxAddQyVip' + self.access_token
        datas = {
            'qy_id': qy_id,
            'vip_type': vip_type,
            'date_type': 2,
            'expire': end_time,
            'reason': '测试'
        }

        try:
            response = requests.request('post', url, cookies=self.cookies, data=datas, headers=self.headers)

            if response.status_code == 200:
                print('企业%s : 修改时间成功' % qy_id)
            else:
                print('企业%s : 修改时间失败' % qy_id)
        except Exception as E:
            print(E)
            print('企业%s : 修改时间失败' % qy_id)



if __name__ == '__main__':
    # qtbkstage = QTBackstage('gvph8jp4ha9hpt8v0n9stbnsti')
    qtbkstage = QTBackstage()

    qtbkstage.revise_qy_vip_time('2863', 3, '2030-01-01')



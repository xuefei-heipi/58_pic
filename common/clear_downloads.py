import urllib.parse
import urllib.request
import requests


def change_user_vip_num_times1(user_id, downloaded_times, vip_type='all'):
    '''
    修改用户vip剩余次数
    :param user_id: 用户id
    :param downloaded_times: 已下载的次数 
    :param vip_type: VIP类型  all——所有，yc——精选，sc——基础，bg——办公
    :return: 
    '''
    # 请求方法
    request_url = 'http://cron.58pic.com/index.php?c=QATools&a=setTodayDownloadNum&' + \
                  'uid=' + str(user_id) + '&' + \
                  'num=' + str(downloaded_times) + '&' + \
                  'type=' + str(vip_type)

    # 头部
    header = {
        'Authorization': 'Basic UUFUb29scy41OHBpYy5jb206NXIlI2xxWXAybFFU'
    }
    # 请求
    f=requests.get(request_url, headers=header).json()
    print(f)

change_user_vip_num_times1(53842774,0,'sc')


# def change_user_vip_num_times(uid ,type, num):
#     url = 'http://cron.58pic.com/index.php?c=QATools&a=setTodayDownloadNum'
#     user = 'QATools.58pic.com'
#     passwd = '5r%#lqYp2lQT'
#
#     body = {
#         'uid':uid,
#         'type':type,
#         'num':num
#     }
#     #拼接url
#     query_string = urllib.parse.urlencode(body)
#     url1 = url + '&' + query_string
#     print(url1)
#
#     # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
#     psmg = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#     # 2. 添加账户信息，第一个参数是与服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是url、 用户名、密码
#     psmg.add_password(None, url1, user, passwd)
#     # 3. 构建一个代理基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
#     hdlr = urllib.request.HTTPBasicAuthHandler(psmg)
#     # 4. 通过 build_opener()方法使用这些代理hdlr对象，创建自定义opener对象
#     opener = urllib.request.build_opener(hdlr)
#     # 5. 构造Request 请求
#     request = urllib.request.Request(url1)
#     # 6. 使用自定义opener发送请求
#     response = opener.open(request)
#     print(response.read())
#
# clear(55244033,'bg',0)
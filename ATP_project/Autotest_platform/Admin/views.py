#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.contrib import messages
from Product.models import Hosts, TestStatus, JsCssCheckInfo, FastCheckDetail, ConsoleCheckInfo, ConsoleCheckDetail
import json
import os
import pymysql
import time
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)  #认证给出的用户名和密码
        if user is not None and user.is_active:    #判断用户名和密码是否有效
            auth.login(request, user)
            request.session['user'] = username  #跨请求的保持user参数
            response = HttpResponseRedirect('/admin/index')
            return response
        else:
            messages.add_message(request, messages.WARNING, '账户或者密码错误，请检查')
            return render(request, 'page/1登录.html')

    return render(request, 'page/1登录.html')


@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'page/1登录.htm')


@login_required
def index(request):
    # return render(request, "page/首页.html")
    hosts = Hosts.objects.all()
    for host in hosts:
        master_host = host.masterHost
        dl_host = host.dlHost
        upload_host = host.uploadHost
    check_status = {
        0: '未检测',
        1: '检测中',
        2: '检测完成',
    }

    test_status = TestStatus.objects.get(id=1)  # 获取页面对应状态
    js_css_check_info = JsCssCheckInfo.objects.get(id=1)  # 获取js文件检测数据
    js_css_detail = FastCheckDetail.objects.filter()  # js文件检测出错详细明细

    jcci_starttime = js_css_check_info.startTime.strftime('%Y-%m-%d %H:%M:%S')
    jcci_endtime = js_css_check_info.endTime.strftime('%Y-%m-%d %H:%M:%S')
    jcci_check_file_num = js_css_check_info.checkFileNum
    jcci_error_file_num = js_css_check_info.errorFileNum

    con_check_info = ConsoleCheckInfo.objects.get(id=1)  # 获取console log文件检测数据
    con_check_detail = ConsoleCheckDetail.objects.filter()  # console log文件检测出错详细明细

    con_starttime = con_check_info.startTime.strftime('%Y-%m-%d %H:%M:%S')
    con_endtime = con_check_info.endTime.strftime('%Y-%m-%d %H:%M:%S')
    con_check_file_num = con_check_info.checkFileNum
    con_error_file_num = con_check_info.errorFileNum

    # console log 测试 使用的用户名和密码
    con_check_username = 'OGCtest2' if test_status.fastCheckUsername == '' else test_status.fastCheckUsername
    con_check_password = '123456' if test_status.fastCheckPassword == '' else test_status.fastCheckPassword

    content = {
        master_host: 'checked',
        dl_host: 'checked',
        upload_host: 'checked',
        'jscss_checktype': check_status[test_status.fastJsCssStatus],
        'console_checktype': check_status[test_status.fastConsoleStatus],
        'j_start_time': jcci_starttime,
        'j_end_time': jcci_endtime,
        'j_check_file_num': jcci_check_file_num,
        'j_error_file_num': jcci_error_file_num,
        'js_css_detail': js_css_detail,
        'c_start_time': con_starttime,
        'c_end_time': con_endtime,
        'c_check_file_num': con_check_file_num,
        'c_error_file_num': con_error_file_num,
        'con_detail': con_check_detail,
        'username': con_check_username,
        'password': con_check_password,
    }

    return render(request, "page/fastest.html", content)



@login_required
def project(request):
    return render(request, "page/2项目管理.html")


@login_required
def project_config(request, project_id):
    from Product.models import Project
    from Autotest_platform.helper.util import get_model
    p = get_model(Project, id=project_id)
    name = p.name if p else ""
    return render(request, "page/2项目管理--环境配置.html", {"projectId": project_id, "projectName": name})


@login_required
def page(request):
    return render(request, "page/3页面管理.html")


@login_required
def element(request):
    return render(request, "page/4页面元素.html")


@login_required
def keyword(request):
    return render(request, "page/5关键字库.html")


@login_required
def keyword_create(request):
    return render(request, "page/5-1新建关键字.html")


@login_required
def keyword_edit(request, keyword_id):
    from Product.models import Keyword, Project
    from Autotest_platform.helper.util import get_model
    kw = get_model(Keyword, id=keyword_id)
    projectId = kw.projectId if kw else 0
    p = get_model(Project, id=projectId)
    projectName = p.name if projectId > 0 and p else "通用"
    keywordName = kw.name if kw else ""
    return render(request, "page/5-2编辑关键字.html",
                  {"id": projectId, "projectName": projectName, "keywordId": keyword_id, "keywordName": keywordName})


@login_required
def testcase(request):
    return render(request, "page/6测试用例.html")


@login_required
def testcase_create(request):
    return render(request, "page/6-1新建测试用例.html")


@login_required
def testcase_edit(request, testcase_id):
    return render(request, "page/6-1编辑测试用例.html", {"testcaseId": testcase_id})


@login_required
def result(request):
    return render(request, "page/7测试结果.html")


@login_required
def result_see(request, result_id):
    return render(request, "page/7-1查看测试结果.html", {"id": result_id})


@login_required
def task(request):
    return render(request, "page/9任务管理.html")


@login_required
def loginConfig(request):
    return render(request, "page/8登录配置.html")


@login_required
def loginConfig_create(request):
    return render(request, "page/8-1新建登录配置.html")


@login_required
def loginConfig_edit(request, login_id):
    return render(request, "page/8-1编辑登录配置.html", {"id": login_id})


@login_required
def fastest(request):
    hosts = Hosts.objects.all()
    for host in hosts:
        master_host = host.masterHost
        dl_host = host.dlHost
        upload_host = host.uploadHost
    check_status = {
        0: '未检测',
        1: '检测中',
        2: '检测完成',
    }

    test_status = TestStatus.objects.get(id=1)  #获取页面对应状态
    js_css_check_info = JsCssCheckInfo.objects.get(id=1)    #获取js文件检测数据
    js_css_detail = FastCheckDetail.objects.filter()    #js文件检测出错详细明细

    jcci_starttime = js_css_check_info.startTime.strftime('%Y-%m-%d %H:%M:%S')
    jcci_endtime = js_css_check_info.endTime.strftime('%Y-%m-%d %H:%M:%S')
    jcci_check_file_num = js_css_check_info.checkFileNum
    jcci_error_file_num = js_css_check_info.errorFileNum

    con_check_info = ConsoleCheckInfo.objects.get(id=1)  #获取console log文件检测数据
    con_check_detail = ConsoleCheckDetail.objects.filter()  #console log文件检测出错详细明细

    con_starttime = con_check_info.startTime.strftime('%Y-%m-%d %H:%M:%S')
    con_endtime = con_check_info.endTime.strftime('%Y-%m-%d %H:%M:%S')
    con_check_file_num = con_check_info.checkFileNum
    con_error_file_num = con_check_info.errorFileNum

    #console log 测试 使用的用户名和密码
    con_check_username = 'OGCtest2' if test_status.fastCheckUsername == '' else test_status.fastCheckUsername
    con_check_password = '123456' if test_status.fastCheckPassword == '' else test_status.fastCheckPassword

    content = {
        master_host: 'checked',
        dl_host: 'checked',
        upload_host: 'checked',
        'jscss_checktype': check_status[test_status.fastJsCssStatus],
        'console_checktype': check_status[test_status.fastConsoleStatus],
        'j_start_time': jcci_starttime,
        'j_end_time': jcci_endtime,
        'j_check_file_num': jcci_check_file_num,
        'j_error_file_num': jcci_error_file_num,
        'js_css_detail': js_css_detail,
        'c_start_time': con_starttime,
        'c_end_time': con_endtime,
        'c_check_file_num': con_check_file_num,
        'c_error_file_num': con_error_file_num,
        'con_detail': con_check_detail,
        'username': con_check_username,
        'password': con_check_password,
    }

    return render(request, "page/fastest.html", content)


@login_required
def fastest_js_ignore(request):

    return render(request, 'page/fJcIgnoreMain.html')


@login_required
def fastest_js_ignore_create(request):

    return render(request, 'page/fJcIgnoreAdd.html')


@login_required
def fastest_js_ignore_main(request, ignore_id):

    return render(request, "page/fJcIgnoreEdit.html", {"ignore_id": ignore_id})


@login_required
def fastest_console_url(request):

    return render(request, 'page/fConsoleUrlMain.html')


@login_required
def fastest_console_create(request):

    return render(request, 'page/fConsoleUrlAdd.html')


@login_required
def fastest_console_main(request, url_id):

    return render(request, "page/fConsoleUrlEdit.html", {"url_id": url_id})


@login_required
def fastest_console_ignore(request):

    return render(request, "page/fConsoleIgnoreMain.html")


@login_required
def fastest_console_ignore_create(request):

    return render(request, "page/fConsoleIgnoreAdd.html")


@login_required
def fastest_console_ignore_main(request, c_ignore_id):

    return render(request, "page/fConsoleIgnoreEdit.html", {"c_ignore_id": c_ignore_id})


@login_required
def functional_testing(request):

    return render(request, "page/functionaltesting.html")
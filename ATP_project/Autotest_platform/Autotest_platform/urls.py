"""Autotest_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from Admin.views import *
from Product.views import Project, Page, Element, Keyword, TestCase, TestResult, Public, TestTasks, Environment, Login, \
    Fastest, FunctionTest # ,
    #User


urlpatterns = [
    # project
    path('api/v1/project/create', Project.create),
    path('api/v1/project/delete/<int:project_id>', Project.delete),
    path('api/v1/project/edit/<int:project_id>', Project.edit),
    path('api/v1/project', Project.find),
    path('api/v1/project/<int:project_id>', Project.get),
    # environment
    path('api/v1/environment/create', Environment.create),
    path('api/v1/environment/delete/<int:environment_id>', Environment.delete),
    path('api/v1/environment/edit/<int:environment_id>', Environment.edit),
    path('api/v1/environment', Environment.find),
    path('api/v1/environment/<int:environment_id>', Environment.get),
    # page
    path('api/v1/page/create', Page.create),
    path('api/v1/page/delete/<int:page_id>', Page.delete),
    path('api/v1/page/edit/<int:page_id>', Page.edit),
    path('api/v1/page', Page.find),
    path('api/v1/page/<int:page_id>', Page.get),
    # element
    path('api/v1/element/create', Element.create),
    path('api/v1/element/delete/<int:element_id>', Element.delete),
    path('api/v1/element/edit/<int:element_id>', Element.edit),
    path('api/v1/element', Element.find),
    path('api/v1/element/<int:element_id>', Element.get),
    # keyword
    path('api/v1/keyword/create', Keyword.create),
    path('api/v1/keyword/delete/<int:keyword_id>', Keyword.delete),
    path('api/v1/keyword/edit/<int:keyword_id>', Keyword.edit),
    path('api/v1/keyword', Keyword.find),
    path('api/v1/keyword/<int:keyword_id>', Keyword.get),
    # testcase
    path('api/v1/testcase/create', TestCase.create),
    path('api/v1/testcase/delete/<int:testcase_id>', TestCase.delete),
    path('api/v1/testcase/edit/<int:testcase_id>', TestCase.edit),
    path('api/v1/testcase', TestCase.find),
    path('api/v1/testcase/<int:testcase_id>', TestCase.get),
    path('api/v1/testcase/copy/<int:testcase_id>', TestCase.copy),
    # tasks
    path('api/v1/task/create', TestTasks.create),
    path('api/v1/task/delete/<int:task_id>', TestTasks.delete),
    path('api/v1/task/edit/<int:task_id>', TestTasks.edit),
    path('api/v1/task', TestTasks.find),
    path('api/v1/task/<int:task_id>', TestTasks.get),
    path('api/v1/task/running/<int:task_id>', TestTasks.test),
    # Login
    path('api/v1/login/create', Login.create),
    path('api/v1/login/delete/<int:login_id>', Login.delete),
    path('api/v1/login/edit/<int:login_id>', Login.edit),
    path('api/v1/login', Login.find),
    path('api/v1/login/<int:login_id>', Login.get),
    path('api/v1/login/bind/<int:login_id>', Login.bind),
    path('api/v1/login/unbind/<int:EnvironmentLogin_id>', Login.unbind),
    path('api/v1/login/bind/edit/<int:EnvironmentLogin_id>', Login.edit_bind),


    path('api/v1/testcase/running/<int:testcase_id>', TestCase.test),
    path('api/v1/result', TestResult.find),
    path('api/v1/result/delete/<int:result_id>', TestResult.delete),
    path('api/v1/result/<int:result_id>', TestResult.get),
    path('api/v1/browser', Public.data),
    path('api/v1/projectSummary', Public.index),
    path('api/v1/barChar', Public.bar_char),
    path('api/v1/lineChar', Public.line_char),

    
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('admin/index', index),
    path('admin/project', project),
    path('admin/project/<int:project_id>', project_config),
    path('admin/page', page),
    path('admin/element', element),
    path('admin/keyword', keyword),
    path('admin/keyword/create', keyword_create),
    path('admin/keyword/edit/<int:keyword_id>', keyword_edit),
    path('admin/testcase', testcase),
    path('admin/testcase/create', testcase_create),
    path('admin/testcase/<int:testcase_id>', testcase_edit),
    path('admin/loginConfig', loginConfig),
    path('admin/loginConfig/create', loginConfig_create),
    path('admin/loginConfig/edit/<int:login_id>', loginConfig_edit),
    path('admin/task', task),
    path('admin/result', result),
    path('admin/result/<int:result_id>', result_see),

    #Fastest
    path('admin/fastest', fastest),

    #JS Ignore 页面
    path('admin/js_ignore', fastest_js_ignore),
    path('admin/fastest/create_js', fastest_js_ignore_create),
    path('api/v1/fastest/js_ignore/<int:ignore_id>', fastest_js_ignore_main),
    #JS Ignore 请求
    path('api/v1/fastest/js_ignore/create', Fastest.js_ignore_create),
    path('api/v1/js_result', Fastest.js_ignore_find),
    path('api/v1/js_ignore/delete/<int:ignore_id>', Fastest.js_ignore_delete),
    path('api/v1/js_ignore/<int:ignore_id>', Fastest.js_ignore_get),
    path('api/v1/js_ignore/update/<int:ignore_id>', Fastest.js_ignore_update),

    #Console log 检测url 页面
    path('admin/console_url', fastest_console_url),
    path('admin/console_url/create', fastest_console_create),
    path('api/v1/console_url/<int:url_id>', fastest_console_main),
    #Console log 检测url 请求
    path('api/v1/fastest/console_url/create', Fastest.console_url_create),
    path('api/v1/console_url_result', Fastest.console_url_find),
    path('api/v1/console_url/edit_url/<int:url_id>', Fastest.console_url_get),
    path('api/v1/console_url/edit_url/update/<int:url_id>', Fastest.console_url_update),
    path('api/v1/console/delete/<int:url_id>', Fastest.console_url_delete),
    #Console log 忽略文件 页面
    path('admin/console_ignore', fastest_console_ignore),
    path('admin/console_ignore/create', fastest_console_ignore_create),
    path('api/v1/console_ignore/<int:c_ignore_id>', fastest_console_ignore_main),
    # Console log 忽略文件 请求
    path('api/v1/fastest/console_ignore/create', Fastest.console_ignore_create),
    path('api/v1/console_ignore_result', Fastest.console_ignore_find),
    path('api/v1/console_ignore/edit/<int:c_ignore_id>', Fastest.console_ignore_get),
    path('api/v1/console_ignore/edit_ignore/update/<int:c_ignore_id>', Fastest.console_ignore_update),
    path('api/v1/console_ignore/delete/<int:c_ignore_id>', Fastest.console_ignore_delete),

    path('api/v1/fastest/change_host', Fastest.change_host),
    path('api/v1/fastest/check_source', Fastest.check_source),
    path('api/v1/fastest/get_browser_console', Fastest.get_browser_console),
    path('api/v1/fastest/console/change_check_user', Fastest.console_change_user),

    #Functional testing
    path('admin/functionaltesting', functional_testing),
    path('api/v1/functionaltesting/get_function_list', FunctionTest.get_function_list),
    path('api/v1/functionaltesting/fun_test/<int:test_id>', FunctionTest.do_function_test),
    path('api/v1/functionaltesting/get_report/<int:test_id>', FunctionTest.get_report),

]

from pic_project.templates.headtop.firsttop import DLAutomatedTest

def test_headtop(browser):
    print('测试登陆首页')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_landing('zdtest4', '123456')
    # result =False
    assert result

def test_headtop_classification_01(browser):
    num = 1
    num1 = 1
    print('测试分类一级菜单平面广告')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_02(browser):
    num = 1
    num1 = 2
    print('测试分类一级菜单电商淘宝')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_03(browser):
    num = 2
    num1 = 1
    print('测试分类一级菜单元素')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_04(browser):
    num = 2
    num1 = 2
    print('测试分类一级菜单背景')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_05(browser):
    num = 2
    num1 = 3
    print('测试分类一级菜单艺术字')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_06(browser):
    num = 3
    num1 = 1
    print('测试分类一级菜单插画')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_07(browser):
    num = 3
    num1 = 2
    print('测试分类一级菜单新媒体用图')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_08(browser):
    num = 4
    num1 = 1
    print('测试分类一级菜单PPT模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_09(browser):
    num = 4
    num1 = 2
    print('测试分类一级菜单Word模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_10(browser):
    num = 5
    num1 = 1
    print('测试分类一级菜单摄影图库')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_11(browser):
    num = 5
    num1 = 2
    print('测试分类一级菜单视频音频')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_12(browser):
    num = 6
    num1 = 1
    print('测试分类一级菜单装饰装修')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_13(browser):
    num = 6
    num1 = 2
    print('测试分类一级菜单3D模型')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_14(browser):
    num = 7
    num1 = 1
    print('测试分类一级菜单简历模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_15(browser):
    num = 7
    num1 = 2
    print('测试分类一级菜单Excel模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_16(browser):
    num = 8
    num1 = 1
    print('测试分类一级菜单GIF动图')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_17(browser):
    num = 8
    num1 = 2
    print('测试分类一级菜单卡通形象')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_18(browser):
    num = 9
    num1 = 1
    print('测试分类一级菜单字库')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_19(browser):
    num = 9
    num1 = 2
    print('测试分类一级菜单网页UI')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification( num, num1)
    assert result

def test_headtop_classification_menu_01(browser):
    num = 1
    num2 = 1
    num3 = 1
    print('测试分类平面广告下节日海报')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_02(browser):
    num = 1
    num2 = 2
    num3 = 1
    print('测试分类电商淘宝下海报/banner')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_03(browser):
    num = 2
    num2 = 1
    num3 = 1
    print('测试分类艺术字下节日素材')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_04(browser):
    num = 2
    num2 = 2
    num3 = 1
    print('测试分类元素下装饰图案')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_05(browser):
    num = 2
    num2 = 3
    num3 = 1
    print('测试分类背景下广告背景')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_06(browser):
    num = 3
    num2 = 1
    num3 = 1
    print('测试分类插画下情感表达')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_07(browser):
    num = 3
    num2 = 2
    num3 = 1
    print('测试分类新媒体用图下手机海报')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_08(browser):
    num = 4
    num2 = 1
    num3 = 1
    print('测试分类PPT模板下工作汇报')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_09(browser):
    num = 4
    num2 = 2
    num3 = 1
    print('测试分类Word模板下信纸/背景')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_10(browser):
    num = 5
    num2 = 1
    num3 = 1
    print('测试分类视频音频下精选配乐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_11(browser):
    num = 5
    num2 = 2
    num3 = 1
    print('测试分类摄影图库下城市/地标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_12(browser):
    num = 6
    num2 = 1
    num3 = 1
    print('测试分类装饰装修下背景墙')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_13(browser):
    num = 6
    num2 = 2
    num3 = 1
    print('测试分类3D模型下陈设饰品')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_14(browser):
    num = 7
    num2 = 1
    num3 = 1
    print('测试分类简历模板下IT/互联网')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_15(browser):
    num = 7
    num2 = 2
    num3 = 1
    print('测试分类Excel下财务报表')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_16(browser):
    num = 8
    num2 = 1
    num3 = 1
    print('测试分类GIF动图下动态元素')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_17(browser):
    num = 8
    num2 = 2
    num3 = 1
    print('测试分类卡通形象下男孩皓皓')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_18(browser):
    num = 9
    num2 = 1
    num3 = 1
    print('测试分类字库下黑体')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_19(browser):
    num = 9
    num2 = 2
    num3 = 1
    print('测试分类网页UI下icon图标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_classification_menu( num, num2, num3)
    assert result

def test_search_outside_01(browser):
    num = 1
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_02(browser):
    num = 2
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_03(browser):
    num = 3
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_04(browser):
    num = 4
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_05(browser):
    num = 5
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_06(browser):
    num = 6
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_07(browser):
    num = 7
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_search_outside_08(browser):
    num = 8
    print('测试搜索框外搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_search_outside(num)
    assert result

def test_within_search_01(browser):
    num = 1
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_02(browser):
    num = 2
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_03(browser):
    num = 3
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_04(browser):
    num = 4
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_05(browser):
    num = 5
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_06(browser):
    num = 6
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_07(browser):
    num = 7
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_08(browser):
    num = 8
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_09(browser):
    num = 9
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_within_search_10(browser):
    num = 10
    print('测试搜索框内搜索词')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_within_search( num)
    assert result

def test_home_upload(browser):

    print('测试公共上传作品按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_upload()
    assert result

def test_home_personal_vip_01(browser):

    print('测试公共个人vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_personal_vip()
    assert result

def test_home_personal_vip_02(browser):
    num = 1
    num1 = 1
    print('测试公共个人vip浮窗精选vip按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_personalvip_suspension(num, num1)
    assert result

def test_home_personal_vip_03(browser):
    num = 1
    num1 = 2
    print('测试公共个人vip浮窗基础vip按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_personalvip_suspension(num, num1)
    assert result

def test_home_personal_vip_04(browser):
    num = 3
    num1 = 1
    print('测试公共个人vip浮窗办公vip按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_personalvip_suspension(num, num1)
    assert result

def test_home_personal_vip_05(browser):
    num = 3
    num1 = 2
    print('测试公共个人vip浮窗字体vip按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_personalvip_suspension(num, num1)
    assert result

def test_home_personal_vip_06(browser):

    print('测试公共个人vip浮窗199vip按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_personalvip_suspension()
    assert result

def test_home_message(browser):

    print('测试消息')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_message()
    assert result

def test_head_portrait(browser):

    print('测试头像下拉框')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_head_portrait()
    assert result

def test_head_portrait_01(browser):
    num = 1
    num1 = 1

    print('测试头像下拉框,精选vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_head_portrait(num,num1)
    assert result

def test_head_portrait_02(browser):
    num = 2
    num1 = 1
    print('测试头像下拉框,作品管理')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_head_portrait(num,num1)
    assert result

def test_head_portrait_03(browser):
    num2 = 2
    print('测试头像下拉框,企业vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_head_portrait(num2)
    assert result

def test_home_sidebar_collar_vip_01(browser):
    num = None
    print('测试侧边栏免费领取vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_collar_vip(num)
    assert result

def test_home_sidebar_collar_vip_02(browser):
    num = 1
    print('测试侧边栏免费领取vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_collar_vip(num)
    assert result

def test_home_sidebar_collar_vip_03(browser):
    num = 2
    print('测试侧边栏免费领取vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_collar_vip(num)
    assert result

def test_home_sidebar_check_in_01(browser):
    num = 1
    print('测试悬浮到签到上点击积分')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_check_in(num)
    assert result

def test_home_sidebar_check_in_02(browser):
    num = 2
    print('测试悬浮到签到上点击积分商城')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_check_in(num)
    assert result

def test_home_sidebar_daily_activities_01(browser):
    num = 2
    num1 = 1
    print('测试悬浮到签到上点击积分商城')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_daily_activities(num, num1)
    assert result

def test_home_sidebar_daily_activities_02(browser):
    num = 1
    num1 = 1
    print('测试悬浮到签到上点击积分商城')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_daily_activities(num, num1)
    assert result

def test_home_sidebar_theme_activity_01(browser):
    num = 1
    print('测试侧边栏弹窗主题活动页,创意教程')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_theme_activity(num)
    assert result

def test_home_sidebar_theme_activity_02(browser):
    num = 2
    num1 = 1
    print('测试侧边栏弹窗主题活动页,创意教程')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_theme_activity(num, num1)
    assert result

def test_home_sidebar_customer_service_01(browser):

    print('测试侧边栏客服悬浮框,常见问题')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_customer_service()
    assert result

def test_home_sidebar_customer_service_02(browser):
    num = 1
    print('测试侧边栏客服悬浮框,联系客服按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_customer_service(num)
    assert result

def test_home_sidebar_make_money_01(browser):

    print('测试侧边栏客服悬浮框,联系客服按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_make_money()
    assert result

def test_home_sidebar_make_money_02(browser):
    num = 1
    print('测试侧边栏客服悬浮框,联系客服按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sidebar_make_money(num)
    assert result

def test_home_feedback(browser):

    print('测试侧边栏反馈按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_feedback()
    assert result

def test_teardown(browser):
    assert True
    browser.quit()
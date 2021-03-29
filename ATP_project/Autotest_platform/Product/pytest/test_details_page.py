from pic_project.templates.headtop.details_page import DLAutomatedTest

def test_home_landing(browser):
    print('测试登陆首页')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_landing('zdtest4', '123456')
    assert result


def test_current_position_01(browser):
    id = 32237240
    num = 1
    print('测试详情页当前位置-首页')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_current_position(id, num)
    assert result

def test_current_position_02(browser):
    id = 32237240
    num = 2
    print('测试详情页当前位置-一级分类')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_current_position(id, num)
    assert result

def test_current_position_03(browser):
    id = 32237240
    num = 3
    print('测试详情页当前位置-二级分类')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_current_position(id, num)
    assert result

def test_details_commercial_standard_01(browser):
    num = 1
    print('测试详情页查看商标授权-点击商标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_commercial_standard(id, num)
    assert  result

def test_details_commercial_standard_02(browser):

    print('测试详情页查看商标授权-点击悬浮框上获取按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_commercial_standard(id)
    assert  result

def test_details_click_vip_01(browser):

    print('测试详情页点击vip标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_click_vip(id)
    assert  result

def test_details_click_vip_02(browser):
    num = 1
    print('测试详情页点击vip标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.details_click_vip(id,num)
    assert  result

def test_details_download_button_01(browser):

    print('测试详情页下载按钮')



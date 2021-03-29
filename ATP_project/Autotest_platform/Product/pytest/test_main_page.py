#coding=utf-8
from Product.template.main_page.main_page import MainPageTest


def test_main_page_01(browser):
    print('主页搜索功能')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_page_search('OGCtest2', '123456', '生活', is_login=1)
    assert result
    # browser.quit()      #false 后的代码不在执行

def test_main_page_02(browser):
    print('签到测试')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_page_sign_in('xfcztest100', '123456', is_login=1)
    assert result

def test_main_page_03(browser):
    print('首页订阅功能')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_page_subscribe('xztest1', '123456', is_login=1)
    assert result

def test_main_page_04(browser):
    print('主页banner切换功能')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_banner_switch('xztest1', '123456', is_login=0)
    assert result

def test_main_page_05(browser):
    print('首页创作中心--无身份')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_creative_center('xztest1', '123456', 0, is_login=0)
    assert result

def test_main_page_06(browser):
    print('首页创作中心--UGC')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_creative_center('UGCtest2', '123456', 1, is_login=1)
    assert result

def test_main_page_07(browser):
    print('首页创作中心--OGC')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_creative_center('OGCtest2', '123456', 2, is_login=1)
    assert result

def test_main_page_08(browser):
    print('首页广告关闭功能')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_advertisement_close('OGCtest2', '123456', is_login=0)
    assert result

def test_main_page_09(browser):
    print('个人切换为企业vip')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_page_qy_vip_switch('xztest29', '123456', is_login=1)
    assert result

def test_main_page_10(browser):
    print('企业切换为个人vip')
    main_page_module = MainPageTest(browser)
    result = main_page_module.main_page_gr_vip_switch('xztest29', '123456', is_login=0)
    assert result



def test_teardown(browser):
    assert True
    browser.quit()


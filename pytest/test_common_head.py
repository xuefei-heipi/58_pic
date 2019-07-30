from pic_project.modules.headtop.firsttop import DLAutomatedTest

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
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_02(browser):
    num = 1
    num1 = 2
    print('测试分类一级菜单电商淘宝')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_03(browser):
    num = 2
    num1 = 1
    print('测试分类一级菜单元素')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_04(browser):
    num = 2
    num1 = 2
    print('测试分类一级菜单背景')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_05(browser):
    num = 2
    num1 = 3
    print('测试分类一级菜单艺术字')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_06(browser):
    num = 3
    num1 = 1
    print('测试分类一级菜单插画')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_07(browser):
    num = 3
    num1 = 2
    print('测试分类一级菜单新媒体用图')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_08(browser):
    num = 4
    num1 = 1
    print('测试分类一级菜单PPT模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_09(browser):
    num = 4
    num1 = 2
    print('测试分类一级菜单Word模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_10(browser):
    num = 5
    num1 = 1
    print('测试分类一级菜单摄影图库')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_11(browser):
    num = 5
    num1 = 2
    print('测试分类一级菜单视频音频')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_12(browser):
    num = 6
    num1 = 1
    print('测试分类一级菜单装饰装修')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_13(browser):
    num = 6
    num1 = 2
    print('测试分类一级菜单3D模型')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_14(browser):
    num = 7
    num1 = 1
    print('测试分类一级菜单简历模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_15(browser):
    num = 7
    num1 = 2
    print('测试分类一级菜单Excel模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_16(browser):
    num = 8
    num1 = 1
    print('测试分类一级菜单GIF动图')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_17(browser):
    num = 8
    num1 = 2
    print('测试分类一级菜单卡通形象')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_18(browser):
    num = 9
    num1 = 1
    print('测试分类一级菜单字库')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_19(browser):
    num = 9
    num1 = 2
    print('测试分类一级菜单网页UI')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification( num, num1)
    assert result

def test_headtop_classification_menu_01(browser):
    num = 1
    num2 = 1
    num3 = 1
    print('测试分类平面广告下节日海报')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_02(browser):
    num = 1
    num2 = 2
    num3 = 1
    print('测试分类电商淘宝下海报/banner')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_03(browser):
    num = 2
    num2 = 1
    num3 = 1
    print('测试分类艺术字下节日素材')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_04(browser):
    num = 2
    num2 = 2
    num3 = 1
    print('测试分类元素下装饰图案')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_05(browser):
    num = 2
    num2 = 3
    num3 = 1
    print('测试分类背景下广告背景')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_06(browser):
    num = 3
    num2 = 1
    num3 = 1
    print('测试分类插画下情感表达')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_07(browser):
    num = 3
    num2 = 2
    num3 = 1
    print('测试分类新媒体用图下手机海报')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_08(browser):
    num = 4
    num2 = 1
    num3 = 1
    print('测试分类PPT模板下工作汇报')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_09(browser):
    num = 4
    num2 = 2
    num3 = 1
    print('测试分类Word模板下信纸/背景')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_10(browser):
    num = 5
    num2 = 1
    num3 = 1
    print('测试分类视频音频下精选配乐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_11(browser):
    num = 5
    num2 = 2
    num3 = 1
    print('测试分类摄影图库下城市/地标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_12(browser):
    num = 6
    num2 = 1
    num3 = 1
    print('测试分类装饰装修下背景墙')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_13(browser):
    num = 6
    num2 = 2
    num3 = 1
    print('测试分类3D模型下陈设饰品')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_14(browser):
    num = 7
    num2 = 1
    num3 = 1
    print('测试分类简历模板下IT/互联网')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_15(browser):
    num = 7
    num2 = 2
    num3 = 1
    print('测试分类Excel下财务报表')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_16(browser):
    num = 8
    num2 = 1
    num3 = 1
    print('测试分类GIF动图下动态元素')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_17(browser):
    num = 8
    num2 = 2
    num3 = 1
    print('测试分类卡通形象下男孩皓皓')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_18(browser):
    num = 9
    num2 = 1
    num3 = 1
    print('测试分类字库下黑体')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_19(browser):
    num = 9
    num2 = 2
    num3 = 1
    print('测试分类网页UI下icon图标')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_classification_menu( num, num2, num3)
    assert result

def test_headtop_classification_menu_19(browser):
    num = 1
    print('测试搜索框外')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_search_outside(num)
    assert result

def test_teardown(browser):
    assert True
    browser.quit()
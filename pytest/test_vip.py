from pic_project.modules.download.dl_58pic import DLAutomatedTest

def test_download_01(browser):
    print('测试无精选vip')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_jx_vip('jxtest1', '123456', 34798744)
    assert result
    # browser.quit()      #false 后的代码不在执行

def test_download_02(browser):
    print('测试无基础vip有一次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_jc_vip_1('jxtest1', '123456', 33903514)
    assert result

def test_download_03(browser):
    print('测试无基础vip无一次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_jc_vip_0('jxtest1', '123456', 33823278)
    assert result

def test_download_04(browser):
    print('测试无办公vip无一次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_bg_vip('jxtest1', '123456', 34664946)
    assert result

def test_download_05(browser):
    print('测试无字库vip有一次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_zk_vip_1('jxtest1', '123456', 32822245)
    assert result

def test_download_06(browser):
    print('测试无字库vip无一次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_zk_vip_0('jxtest1', '123456', 32822231)
    assert result

def test_download_07(browser):
    print('测试精选vip20次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_jx_vip_20('jxtest', '123456', 34798744)
    assert result

def test_download_08(browser):
    print('测试精选vip20次用完受限')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_restrict_jx_vip_20('jxtest', '123456', 34898619)
    assert result

def test_download_09(browser):
    print('测试基础vip20次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_jc_vip_20('jctest', '123456', 27100433)
    assert result

def test_download_10(browser):
    print('测试基础vip20次用完受限')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_restrict_jc_vip_20('jctest', '123456', 28182874)
    assert result

def test_download_11(browser):
    print('测试办公vip10次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_bg_vip_10('bgtest', '123456', 34686542)
    assert result

def test_download_12(browser):
    print('测试办公10次用完受限')
    dl_module =DLAutomatedTest(browser)
    result = dl_module.dl_restrict_bg_vip_10('bgtest', '123456', 15466255)
    assert result

def test_download_13(browser):
    print('测试字库20次下载')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_zk_vip_20('zktest3','123456',32822245)
    assert result

# def test_download_14(browser):
#     print('测试字库20次用完受限')
#     dl_module = DLAutomatedTest(browser)
#     result = dl_module.dl_restrict_zk_vip_20('zktest3','123456', 32822219)
#     assert  result

def test_download_15(browser):
    print('测试企业499下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_vip_499('zktest4','123456',34802939)
    assert result

def test_download_16(browser):
    print('测试企业499，次数用完受限')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_restrict_qy_vip_499('zktest4','123456',34816506)
    assert result

def test_download_17(browser):
    print('测试字库999下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_zk_vip_999('zktest5', '123456',32822232, 32837643 )
    assert result

# def test_download_18(browser):
#     print('测试字库999，下载次数用完受限')
#     dl_module =   DLAutomatedTest(browser)
#     result = dl_module.dl_restrict_zk_vip_999('cstest17', '123456',32822121)
#     assert result

def test_download_18(browser):
    print('测试免费下载国家授权素材')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_mf_wx('wxtest', '123456', 34878067)
    assert result

def test_teardown(browser):
    assert True
    browser.quit()


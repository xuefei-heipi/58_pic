#coding=utf-8
from Product.template.download.dl_58pic import DLAutomatedTest


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
    result = dl_module.dl_no_zk_vip_1('zknovip', '123456', 35135657)
    assert True


def test_download_06(browser):
    print('测试无字库vip无一次下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_no_zk_vip_0('jxtest1', '123456', 35011375)
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
    result = dl_module.dl_zk_vip_20('zktest3', '123456', 35135640)
    assert result


def test_download_15(browser):
    print('测试企业499下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_vip_499('zktest4','123456',34802939)
    assert result


def test_download_16(browser):
    print('499，次数用完受限')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_restrict_qy_vip_499('zktest4', '123456', 34816506)
    assert result


def test_download_17(browser):
    print('测试字库999下载机会')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_zk_vip_999('zktest5', '123456', 35011405, 34831774)
    assert result


def test_download_18(browser):
    print('测试免费下载国家授权素材')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_mf_wx('wxtest', '123456', 34878067)
    assert result

def test_download_19(browser):
    print('测试三终身下载精选')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_active('xztest14', '123456', '35738620', is_login=1)
    assert result

def test_download_20(browser):
    print('测试三终身下载基础')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_active('xztest14', '123456', '35728873', is_login=0)
    assert result

def test_download_21(browser):
    print('测试三终身下载办公')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_active('xztest14', '123456', '35515085', is_login=0)
    assert result

def test_download_22(browser):
    print('测试vip过期下载受限精选')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_expire('xztest15', '123456', '35738620', is_login=1)
    assert result

def test_download_23(browser):
    print('测试vip过期下载受限基础')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_expire('xztest15', '123456', '35728873', is_login=0)
    assert result

def test_download_24(browser):
    print('测试vip过期下载受限办公')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_expire('xztest15', '123456', '35515085', is_login=0)
    assert result

def test_download_25(browser):
    print('测试vip过期下载受限字体')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_vip_expire('xztest15', '123456', '34221666', is_login=0)
    assert result

def test_download_26(browser):
    print('测试企业vip认证通过下载 基础版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_active('xztest17', '123456', '35515085', is_login=1)
    assert result

def test_download_27(browser):
    print('测试企业vip认证通过下载 专业版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_active('xztest20', '123456', '35515085', is_login=1)
    assert result

def test_download_28(browser):
    print('测试企业vip认证通过下载 旗舰版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_active('xztest21', '123456', '35515085', is_login=1)
    assert result

def test_download_29(browser):
    print('测试企业vip认证通过过期下载 基础版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_expire('xztest17', '123456', '35515085', is_login=1)
    assert result

def test_download_30(browser):
    print('测试企业vip认证通过过期下载 专业版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_expire('xztest20', '123456', '35515085', is_login=1)
    assert result

def test_download_31(browser):
    print('测试企业vip认证通过过期下载 旗舰版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_expire('xztest21', '123456', '35515085', is_login=1)
    assert result

def test_download_32(browser):
    print('测试企业vip认证通过下载 转售版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_active('xztest22', '123456', '35515085', is_login=1)
    assert result

def test_download_33(browser):
    print('测试企业vip认证通过过期下载 转售版')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_expire('xztest12', '123456', '35515085', is_login=1)
    assert result

def test_download_34(browser):
    print('测试企业vip认证通过下载 基础版成员')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_active('xztest23', '123456', '35515085', is_login=1)
    assert result

def test_download_35(browser):
    print('测试企业vip认证通过下载 基础版成员被冻结')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_expire('xztest24', '123456', '35515085', is_login=1)
    assert result

def test_download_36(browser):
    print('企业认证vip当日下载超过100次限制  超级管理员')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_limit('xztest25', '123456', '35772128', is_login=1)
    assert result

def test_download_37(browser):
    print('企业认证vip当日下载超过100次限制  成员')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_certified_limit('xztest26', '123456', '35772128', is_login=1)
    assert result

def test_download_38(browser):
    print('企业未认证vip当日下载提醒  超级管理员')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_uncertified_remind('xztest27', '123456', '35772128', is_login=1)
    assert result

def test_download_39(browser):
    print('企业未认证vip当日下载提醒  成员')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_uncertified_remind('xztest28', '123456', '35772128', is_login=1)
    assert result

def test_download_39(browser):
    print('企业未认证vip下载锁号  成员')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.dl_qy_uncertified_locked('xztest28', '123456', '35772128', is_login=0)
    assert result


def test_teardown(browser):
    assert True
    browser.quit()


from pic_project.modules.headtop.firsttop import DLAutomatedTest

def test_headtop(browser):
    print('测试登陆首页')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_landing('zdtest4', '123456')
    # result =False
    assert result

def test_headtop_pingmian(browser):
    print('测试首页banner菜单平面广告')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_pingmian()
    assert result

def test_headtop_dianshangtaobao(browser):
    print('测试首页banner菜单电商淘宝')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_dianshangtaobao()
    assert result

def test_headtop_shejiyuansu(browser):
    print('测试首页banner菜单设计元素')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_shejiyuansu()
    assert result

def test_headtop_PPTmuban(browser):
    print('测试首页banner菜单PPT模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_PPTmuban()
    assert result

def test_headtop_chahuahuihua(browser):
    print('测试首页banner菜单插画绘画')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_chahuahuihua()
    assert result

def test_headtop_shipingyinxiao(browser):
    print('测试首页banner菜单视频音效')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_shipingyinxiao()
    assert result

def test_headtop_zhuangshizhuangxiu(browser):
    print('测试首页固定菜单-装饰装修')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_zhuangshizhuangxiu()
    assert result

def test_headtop_sheyingtuku(browser):
    print('测试首页固定菜单-摄影图库')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_sheyingtuku()
    assert result

def test_headtop_wangyeui(browser):
    print('测试首页固定菜单-网页UI')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_wangyeUI()
    assert result

def test_headtop_meitiyongtu(browser):
    print('测试首页固定菜单-媒体用图')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_meitiyongtu()
    assert result

def test_headtop_gifdongtu(browser):
    print('测试首页固定菜单-GIF动图')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_GIFdongtu()
    assert result

def test_headtop_wordmuban(browser):
    print('测试首页固定菜单-word模板')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_wordmuban()
    assert result

def test_headtop_teyaoshenqing(browser):
    print('测试首页固定菜单-特邀申请')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_teyaoshenqing()
    assert result

def test_headtop_jifengshangcheng(browser):
    print('测试首页固定菜单-积分商城')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_jifengshangcheng()
    assert result

def test_headtop_huodong(browser):
    print('测试首页固定菜单-活动')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_huodong()
    assert result

def test_headtop_chuangyiqushi(browser):
    print('测试首页固定菜单-创意趋势')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_chuangyiqushi()
    assert result

def test_headtop_qiantubox(browser):
    print('测试首页千图工具-千图box')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_honme_qiantugongju_qiantubox()
    assert result

def test_headtop_qiantuyangji(browser):
    print('测试首页千图工具-千图样机')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_qiantugongju_qiantuyangji()
    assert result

def test_headtop_shejigongju(browser):
    print('测试首页千图工具- 设计工具')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_qiantugongju_shejigongju()
    assert result

def test_headtop_blog(browser):
    print('测试首页博客')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_blog()
    assert result

def test_headtop_collection(browser):
    print('测试首页精选收藏夹楼层')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_collection()
    assert result

def test_headtop_collection_recommend_01(browser):
    print('测试精选收藏夹楼层-千图精选-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection_recommend(1)
    assert result

def test_headtop_collection_recommend_02(browser):
    print('测试精选收藏夹楼层-插画风-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection_recommend(2)
    assert result

def test_headtop_collection_recommend_03(browser):
    print('测试精选收藏夹楼层-优秀设计师-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection_recommend(3)
    assert result

def test_headtop_collection_recommend_04(browser):
    print('测试精选收藏夹楼层-热门趋势-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection_recommend(4)
    assert result

def test_headtop_collection_01(browser):
    print('测试首页精选收藏夹楼层-千图精选收藏夹')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection(1,1)
    assert result

def test_headtop_collection_02(browser):
    print('测试首页精选收藏夹楼层-插画风收藏夹')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection(2,1)
    assert result

def test_headtop_collection_03(browser):
    print('测试首页精选收藏夹楼层-优秀设计师收藏夹')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection(3,1)
    assert result

def test_headtop_collection_04(browser):
    print('测试首页精选收藏夹楼层-热门趋势收藏夹')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_collection(4,1)
    assert result

def test_headtop_designer_01(browser):
    above = 1
    num = 1
    print('测试明星设计师推荐-设计师卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer(above,num)
    assert result

def test_headtop_designer_02(browser):
    above = 2
    num = 1
    print('测试明星设计师推荐-设计师卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer(above,num)
    assert result

def test_headtop_designer_03(browser):
    above = 3
    num = 1
    print('测试明星设计师推荐-设计达人卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer(above,num)
    assert result

def test_headtop_designer_change_01(browser):
    above = 2
    num = 1
    print('测试明星设计师推荐换一批按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer_change(above,num)
    assert result

def test_headtop_designer_change_02(browser):
    above = 3
    num = 1
    print('测试明星设计师推荐换一批按钮')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer_change(above,num)
    assert result

def test_headtop_designer_attention_01(browser):
    above = 1
    num = 1
    print('测试明星设计师推荐卡片关注')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer_attention(above,num)
    assert result

def test_headtop_designer_attention_02(browser):
    above = 2
    num = 1
    print('测试明星设计师推荐卡片关注')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer_attention(above,num)
    assert result

def test_headtop_designer_attention_03(browser):
    above = 3
    num = 1
    print('测试设计达人推荐卡片关注')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_designer_attention(above,num)
    assert result

def test_headtop_floorname_01(browser):
    num = 1
    print('测试首页点击平面广告最新推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floorname(num)
    assert result

def test_headtop_floorname_02(browser):
    num = 2
    print('测试首页点击电商淘宝最新推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floorname(num)
    assert result

def test_headtop_floorname_03(browser):
    num = 3
    print('测试首页点击设计元素最新推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floorname(num)
    assert result

def test_headtop_floorname_04(browser):
    num = 4
    print('测试首页点击PPT模板最新推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floorname(num)
    assert result

def test_headtop_floorname_05(browser):
    num = 5
    print('测试首页点击插画绘画最新推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floorname(num)
    assert result

def test_headtop_floorname_06(browser):
    num = 6
    print('测试首页点击视频音频最新推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floorname(num)
    assert result

def test_headtop_floor_change_01(browser):
    num = 1
    print('测试楼层下千图精选-换一批')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_change(num)
    assert result

def test_headtop_floor_change_02(browser):
    num = 2
    print('测试楼层下千图精选-换一批')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_change(num)
    assert result

def test_headtop_floor_change_03(browser):
    num = 3
    print('测试楼层下千图精选-换一批')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_change(num)
    assert result

def test_headtop_floor_recommend_01(browser):
    above1 = 1
    above2 = 2
    print('测试平广告-促销海报-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_02(browser):
    above1 = 1
    above2 = 3
    print('测试平广告-商务名片-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_03(browser):
    above1 = 1
    above2 = 4
    print('测试平广告-企业画册-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_04(browser):
    above1 = 1
    above2 = 5
    print('测试平广告-化妆品包装-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_05(browser):
    above1 = 2
    above2 = 2
    print('测试电商淘宝-服装鞋业-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_06(browser):
    above1 = 2
    above2 = 3
    print('测试电商淘宝-美妆洗护-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_07(browser):
    above1 = 2
    above2 = 4
    print('测试电商淘宝-日用家居-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_08(browser):
    above1 = 2
    above2 = 5
    print('测试电商淘宝-数码电器-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_09(browser):
    above1 = 3
    above2 = 2
    print('测试设计元素-效果元素-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_10(browser):
    above1 = 3
    above2 = 3
    print('测试设计元素-装饰图案-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_12(browser):
    above1 = 3
    above2 = 4
    print('测试设计元素-节日元素-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_13(browser):
    above1 = 3
    above2 = 5
    print('测试设计元素-纹理边框-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_14(browser):
    above1 = 4
    above2 = 2
    print('测试PPT模板-工作汇报-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_15(browser):
    above1 = 4
    above2 = 3
    print('测试PPT模板-计划总结-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_16(browser):
    above1 = 4
    above2 = 4
    print('测试PPT模板-个人简历-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_17(browser):
    above1 = 4
    above2 = 5
    print('测试PPT模板-企业宣传-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_18(browser):
    above1 = 5
    above2 = 2
    print('测试插画绘画-情感表达-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_19(browser):
    above1 = 5
    above2 = 3
    print('测试插画绘画-节日节气-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_20(browser):
    above1 = 5
    above2 = 4
    print('测试插画绘画-教育文化-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_21(browser):
    above1 = 5
    above2 = 5
    print('测试插画绘画-风光建筑-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_22(browser):
    above1 = 6
    above2 = 2
    print('测试视频音频-婚恋家庭-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_23(browser):
    above1 = 6
    above2 = 3
    print('测试视频音频-背景-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_24(browser):
    above1 = 6
    above2 = 4
    print('测试视频音频-字幕条-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_floor_recommend_25(browser):
    above1 = 6
    above2 = 5
    print('测试视频音频-党政文化-查看全部推荐')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_recommend(above1,above2)
    assert result

def test_headtop_card_01(browser):
    above1 = 1
    above2 = 1
    num1 = 1
    print('测试平面广告-千图精选卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_02(browser):
    above1 = 1
    above2 = 2
    num1 = 1
    print('测试平面广告-促销海报卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_03(browser):
    above1 = 1
    above2 = 3
    num1 = 1
    print('测试平面广告-商务名片卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_04(browser):
    above1 = 1
    above2 = 4
    num1 = 1
    print('测试平面广告-企业画册卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_05(browser):
    above1 = 1
    above2 = 5
    num1 = 1
    print('测试平面广告-化妆品包装卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_06(browser):
    above1 = 2
    above2 = 1
    num1 = 1
    print('测试电商淘宝-千图精选卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_07(browser):
    above1 = 2
    above2 = 2
    num1 = 1
    print('测试电商淘宝-服装鞋业卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_08(browser):
    above1 = 2
    above2 = 3
    num1 = 1
    print('测试电商淘宝-美妆洗护卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_09(browser):
    above1 = 2
    above2 = 4
    num1 = 1
    print('测试电商淘宝-日用家居卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_10(browser):
    above1 = 2
    above2 = 5
    num1 = 1
    print('测试电商淘宝-数码电器卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_11(browser):
    above1 = 3
    above2 = 1
    num1 = 1
    print('测试设计元素-千图精选卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_12(browser):
    above1 = 3
    above2 = 2
    num1 = 1
    print('测试设计元素-效果元素卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_13(browser):
    above1 = 3
    above2 = 3
    num1 = 1
    print('测试设计元素-装饰图案卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_14(browser):
    above1 = 3
    above2 = 4
    num1 = 1
    print('测试设计元素-节日元素卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_15(browser):
    above1 = 3
    above2 = 5
    num1 = 1
    print('测试设计元素-纹理边框卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_16(browser):
    above1 = 4
    above2 = 1
    num1 = 1
    print('测试PPT模板-千图精选卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_17(browser):
    above1 = 4
    above2 = 2
    num1 = 1
    print('测试PPT模板-工作汇报卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_18(browser):
    above1 = 4
    above2 = 3
    num1 = 1
    print('测试PPT模板-计划总结卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_19(browser):
    above1 = 4
    above2 = 4
    num1 = 1
    print('测试PPT模板-个人简历卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_20(browser):
    above1 = 4
    above2 = 5
    num1 = 1
    print('测试PPT模板-企业宣传卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_21(browser):
    above1 = 5
    above2 = 1
    num1 = 1
    print('测试插画绘画-千图精选卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_22(browser):
    above1 = 5
    above2 = 2
    num1 = 1
    print('测试插画绘画-情感表达卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_23(browser):
    above1 = 5
    above2 = 3
    num1 = 1
    print('测试插画绘画-节日节气卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_24(browser):
    above1 = 5
    above2 = 4
    num1 = 1
    print('测试插画绘画-教育文化卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_25(browser):
    above1 = 5
    above2 = 5
    num1 = 1
    print('测试插画绘画-风光建筑卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_26(browser):
    above1 = 6
    above2 = 1
    num1 = 1
    print('测试视频音频-千图精选卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_27(browser):
    above1 = 6
    above2 = 2
    num1 = 1
    print('测试视频音频-婚恋家庭卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_28(browser):
    above1 = 6
    above2 = 3
    num1 = 1
    print('测试视频音频-背景卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_29(browser):
    above1 = 6
    above2 = 4
    num1 = 1
    print('测试视频音频-字幕条卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_headtop_card_30(browser):
    above1 = 6
    above2 = 5
    num1 = 1
    print('测试视频音频-党政文化卡片')
    dl_module = DLAutomatedTest(browser)
    result = dl_module.drop_home_floor_card(above1,above2,num1)
    assert result

def test_teardown(browser):
    assert True
    browser.quit()


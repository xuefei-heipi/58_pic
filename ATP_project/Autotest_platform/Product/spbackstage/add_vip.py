from pic_project.spbackstage.qt_backstage import QTBackstage


# :param uid:  需要添加的账号id   int
    # :param vip_type: 1 共享  2 原创  3 办公  int
    # :param limit: 0 海量  1 每日受限20次   2 每日受限10次（办公）  int
    # :param time_type: 1 输入天数， 2 到期时间， 3 终生  int
    # :param time_value: 5 ，    2018-12-1      无需传   int  string
    # :param reason: 添加原因   string
    # :return:
qt_bkstage = QTBackstage('gvph8jp4ha9hpt8v0n9stbnsti')

var = 0
uid = 49070243
if var == 0:

    datas_gx_vip_times = [uid, 1, 1, 2, '2018-12-09', "充值AB测试"]
    datas_yc_vip_times = [uid, 2, 1, 2, '2018-12-09', "充值AB测试"]
    datas_bg_vip_times = [uid, 3, 2, 2, '2018-12-09', "充值AB测试"]

    qt_bkstage.add_vip(datas_gx_vip_times[0], datas_gx_vip_times[1], datas_gx_vip_times[2], datas_gx_vip_times[3], datas_gx_vip_times[4]
                       , datas_gx_vip_times[5])
    qt_bkstage.add_vip(datas_yc_vip_times[0], datas_yc_vip_times[1], datas_yc_vip_times[2], datas_yc_vip_times[3], datas_yc_vip_times[4]
                       , datas_yc_vip_times[5])
    qt_bkstage.add_vip(datas_bg_vip_times[0], datas_bg_vip_times[1], datas_bg_vip_times[2], datas_bg_vip_times[3], datas_bg_vip_times[4]
                       , datas_bg_vip_times[5])
elif var == 1:
    datas_gx_vip_times = [uid, 1, 0, 1, '1', "充值AB测试"]
    datas_yc_vip_times = [uid, 2, 0, 1, '1', "充值AB测试"]
    datas_bg_vip_times = [uid, 3, 0, 1, '1', "充值AB测试"]
    qt_bkstage.add_vip(datas_gx_vip_times[0], datas_gx_vip_times[1], datas_gx_vip_times[2], datas_gx_vip_times[3],
                       datas_gx_vip_times[4]
                       , datas_gx_vip_times[5])
    qt_bkstage.add_vip(datas_yc_vip_times[0], datas_yc_vip_times[1], datas_yc_vip_times[2], datas_yc_vip_times[3],
                       datas_yc_vip_times[4]
                       , datas_yc_vip_times[5])
    qt_bkstage.add_vip(datas_bg_vip_times[0], datas_bg_vip_times[1], datas_bg_vip_times[2], datas_bg_vip_times[3],
                       datas_bg_vip_times[4]
                       , datas_bg_vip_times[5])
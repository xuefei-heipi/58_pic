from Product.spbackstage.qt_backstage import QTBackstage

if __name__ == '__main__':
    qtbkstage = QTBackstage()

    # 获取下载链接
    print('不是所有的链接都能下载，源文件可能已丢失，下载有效时间为10分钟。')
    designer_id = 12975016
    page_max_num = 20000
    file_name = 'C:\\Users\\Dell\\Desktop\\' + str(designer_id) + '.txt'
    file = open(file_name, 'w')
    file.write('不是所有的链接都能下载，源文件可能已丢失，下载有效时间为10分钟。\r\n')
    # 循环2000次如果第n页没有链接直接停止循环
    for page_num in range(1, page_max_num):
        print(page_num)
        if qtbkstage.get_user_pic_download_url(designer_id, page_num, file) == 0:
            break
    file.close()
    print('获取链接结束。。。')
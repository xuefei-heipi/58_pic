import requests
from lxml import etree
from envatoV2.common import *


class Envato():

    def get_page_source(self, page_url, cursor):
        """

        :param page_url:
        :return:
        """
        res = requests.get(url=page_url, timeout=10)

        # 获取页面元素
        html = etree.HTML(res.text)
        # 页面所有图片元素
        result = html.xpath('.//ul[@class="_2tY3C"]/li')
        if len(result) == 0:
            return False
        # print(len(result))
        #遍历当前页面所有素材
        for res in result:
            pic_info = {}
            # pic_id = pic_title_e = pic_detail_url = pic_img_url = ''   /bookmarks/widget?item_id=9959555
            # 获取pic_id
            pic_id = int(find_by_xpath(res, './/span[@class="_1CDxH"]/a[2]/@href', 0)\
                .replace('/bookmarks/widget?item_id=', '')\
                .replace('/favorites?item_id=', ''))
            # 获取素材名称  无法获取
            # pic_title = find_by_xpath(res, './/h3[@class="_2WWZB"]/a/descendant-or-self::text()', 0)
            # 获取素材 详情页链接
            pic_detail_url = find_by_xpath(res, './/h3[@class="_2WWZB"]/a/@href', 0)
            # 获取素材 价格 无法获取
            # pic_price = find_by_xpath(res, './/div[@class="-DeRq"]/text()', 0)
            # 获取素材 销售量
            # pic_pic_sales = find_by_xpath(res, './/div[@class="_3QV9M"]/descendant-or-self::text()', 0)
            try:
                pic_sales = find_by_xpath(res, './/div[@class="_3QV9M"]/text()', 0)\
                    .replace(' ', '')
                if 'K' in pic_sales:
                    coefficient = 1000  # 系数
                    pic_sales = pic_sales.replace('K', '')
                    if '.' in pic_sales:
                        pic_sales = pic_sales.replace('.', '')
                        coefficient = 100
                    pic_sales = int(pic_sales) * coefficient
                else:
                    pic_sales = int(pic_sales)
            except:
                pic_sales = 0

            # 获取素材 星级
            try:
                pic_stars = find_by_xpath(res, './/div[@class="_3yoIm"]/@aria-label', 0)\
                    .split(' ')[1]
            except:
                pic_stars = '0'

            # print(pic_id,  pic_detail_url)
            # print(pic_pic_sales, pic_stars)
            if not is_pic_exist(pic_id, cursor):
                print('开始插入: %d' % pic_id)
                insert_pic(pic_id, pic_detail_url, pic_sales, pic_stars, cursor)

        return True


    def get_info(self, url, pic_id , cursor):
        """

        :param url:
        :param pic_id:
        :param cursor:
        :return:
        """
        res = requests.get(url=url, timeout=10)

        # 获取页面元素
        html = etree.HTML(res.text.replace('\n', ''))
        # 获取 标题   处理：替换换行  替换 首尾空格
        pic_title = find_by_xpath(html, './/div[@class="item-header__title"]/h1/text()', 0)\
            .replace('\n', '')\
            .strip()
        # 获取 图片url
        pic_img_url = find_by_xpath(html, './/div[@class="video-preview-wrapper"]/a/img/@src', 0)
        # 获取 mp4 url
        pic_mp4_url = find_by_xpath(html, './/div[@class="video-preview-wrapper"]/a/@href', 0)

        try:
            # 获取 价格
            pic_price = int(find_by_xpath(html, './/span[@class="js-purchase-price"]/text()', 0)\
                .replace('$', ''))
        except:
            pic_price = 0

        # 获取分类
        categorys = html.xpath('.//nav[@class="breadcrumbs h-text-truncate "]/a')
        try:
            first_category = find_by_xpath(categorys[2], './/text()', 0)
        except:
            first_category = ''
        try:
            second_category = find_by_xpath(categorys[3], './/text()', 0)
        except:
            second_category = ''
        try:
            third_category = find_by_xpath(categorys[4], './/text()', 0)
        except:
            third_category = ''
        try:
            fourth_category = find_by_xpath(categorys[5], './/text()', 0)
        except:
            fourth_category = ''

        # 获取 评论 数
        comments = find_by_xpath(html, './/a[@class="t-link -decoration-none js-item-comments"]/descendant::text()', 2)\
            .strip()

        # with open('./1.txt', 'w+') as file:
        #     file.writelines(res.text)

        infos = html.xpath('.//table[@class="meta-attributes__table"]/tbody/tr')
        frame_rate = 0
        number_of_clips = 0
        last_update = created = alpha_channel = looped_video  = resolution = video_encoding = ''
        file_size = total_clip_length = individual_clip_lengths = tags = ''
        for info in infos:
            td_name = find_by_xpath(info, './/td[@class="meta-attributes__attr-name"]/text()', 0)
            td_atrr = find_by_xpath(info, './/td[@class="meta-attributes__attr-detail"]/descendant-or-self::text()', 1)\
                .strip()
            if 'Last' in td_name:
                last_update = td_atrr
            elif 'Created' in td_name:
                created= td_atrr
            elif 'Alpha' in td_name:
                alpha_channel = td_atrr
            elif 'Looped' in td_name:
                looped_video = td_atrr
            elif 'Frame' in td_name:
                try:
                    frame_rate = int(td_atrr)
                except:
                    frame_rate = 0
            elif 'Resolution' in td_name:
                resolution = td_atrr
            elif 'Video' in td_name:
                video_encoding = td_atrr
            elif 'File' in td_name:
                file_size = td_atrr
            elif 'Number' in td_name:
                try:
                    number_of_clips = int(td_atrr)
                except:
                    number_of_clips = 0
            elif 'Total' in td_name:
                total_clip_length = td_atrr
            elif 'Individual' in td_name:
                individual_clip_lengths = td_atrr
            elif 'Tags' in td_name:
                td_atrrs = info.xpath('.//span/a')
                for td_at in td_atrrs:
                    tags = tags + find_by_xpath(td_at, './/text()', 0) + ','
        pic_infos = {}
        pic_infos['pic_title'] = pic_title
        pic_infos['pic_img_url'] = pic_img_url
        pic_infos['pic_mp4_url'] = pic_mp4_url
        pic_infos['pic_price'] = pic_price
        pic_infos['first_category'] = first_category
        pic_infos['second_category'] = second_category
        pic_infos['third_category'] = third_category
        pic_infos['fourth_category'] = fourth_category
        pic_infos['comments'] = comments
        pic_infos['last_update'] = last_update
        pic_infos['created'] = created
        pic_infos['alpha_channel'] = alpha_channel
        pic_infos['looped_video'] = looped_video
        pic_infos['frame_rate'] = frame_rate
        pic_infos['resolution'] = resolution
        pic_infos['video_encoding'] = video_encoding
        pic_infos['file_size'] = file_size
        pic_infos['number_of_clips'] = number_of_clips
        pic_infos['total_clip_length'] = total_clip_length
        pic_infos['individual_clip_lengths'] = individual_clip_lengths
        pic_infos['tags'] = tags

        print(pic_infos)
        update_pic(pic_id, pic_infos, cursor)

        # print(pic_title)
        # print(pic_img_url)
        # print(pic_mp4_url)
        # print(pic_price)
        # print(first_category)
        # print(second_category)
        # print(third_category)
        # print(fourth_category)
        # print(comments)
        # print(last_update)
        # print(created)
        # print(alpha_channel)
        # print(looped_video)
        # print(frame_rate)
        # print(resolution)
        # print(video_encoding)
        # print(file_size)
        # print(number_of_clips)
        # print(total_clip_length)
        # print(individual_clip_lengths)
        # print(tags)

if __name__ == '__main__':

    import time
    ev = Envato()
    url = 'https://videohive.net/item/3d-video-mapping-vj-loop-pack-7in1/16429779'
    # driver = browser()
    # driver.maximize_window()
    # driver.get(url)
    # time.sleep(3)
    # page_source = driver.page_source
    ev.get_info(url)
    # driver.quit()

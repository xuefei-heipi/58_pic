
from urllib import request
import time
import os
#Django中导入models 必须要加入下面2个
from django.conf import settings
settings.configure()


def httpget_check(url_array, error_list):

    from Product.models import JSIgnore as jsignore
    js_ignore = jsignore.objects.filter()
    ignore_url = []
    for url in js_ignore:
        ignore_url.append(url.title)


    for url in url_array:
        # print(url)
        if url in ignore_url:
            pass
        else:
            try:

                request.urlopen(url).code

            except Exception as e:
                error_str = url + '     code:' + str(e.code)
                print(error_str)
                error_list.append(error_str)


def write_sourcemap(text):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    source_map_path = os.path.join(BASE_DIR, '..\\static\\check_report\\js_report\\sourcemap.html')

    with open(source_map_path, 'w') as file:
        file.write(text)


def get_BASE_DIR():

    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def report_path():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, '..\\static\\check_report\\test_report')

    return path


def print_time():
    print(time.time())

if __name__ == '__main__':

    write_sourcemap('1')

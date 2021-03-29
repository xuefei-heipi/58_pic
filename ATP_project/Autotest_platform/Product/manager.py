import os
import time


def do_test(cmd_command):
    mystr = os.popen(cmd_command)
    mystr.read()



if __name__ == '__main__':

    daytime = time.strftime("%Y%m%d%H%M%S")

    cmd_command = 'pytest D:\ATP_project\Autotest_platform\Product\pytest\\test_vip.py --html=D:\ATP_project\Autotest_platform\Product\..\static\check_report\\test_report\\report_vip%s.html --self-contained-html' % str(daytime)

    do_test(cmd_command)










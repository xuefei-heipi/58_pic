import os
from multiprocessing.pool import Pool
from time import sleep
import time


def do_test(cmd_command):
    mystr = os.popen(cmd_command)
    mystr.read()


if __name__ == '__main__':
    daytime = time.strftime("%Y%m%d%H%M%S")

    # cmd_command = ['pytest ' + os.getcwd() + '/test_firsttop.py --html=.\\..\\report\\report_firsttop.html --self-contained-html',
    #                ]
    cmd_command = ['pytest ' + os.getcwd() + '\\test_vip.py --html=.\\..\\report\\report_vip' + str(daytime) +'.html --self-contained-html',
                   ]
    # cmd_command = ['pytest ' + os.getcwd() + '/test_common_head.py --html=.\\..\\report\\report_common_head.html --self-contained-html',
    #                ]
    print(cmd_command[0])
    do_test(cmd_command[0])

    # pool_num = 1
    # pool = Pool(pool_num)
    # for x in range(0, 1):
    #     print(cmd_command[x])
    #     pool.apply_async(do_test, args=(cmd_command[x],))
    #     sleep(1)
    # pool.close()
    # pool.join()






# print('hello', mystr)



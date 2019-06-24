import os
from multiprocessing.pool import Pool
from time import sleep



def do_test(cmd_command):
    mystr = os.popen(cmd_command)
    mystr.read()

if __name__ == '__main__':

    cmd_command = ['pytest ' + os.getcwd() + '/test_vip.py --html=.\\..\\report\\report_vip.html --self-contained-html',
                   ]
    pool_num = 1
    pool = Pool(pool_num)
    for x in range(0,1):
        print(cmd_command[x])
        pool.apply_async(do_test, args=(cmd_command[x],))
        sleep(1)
    pool.close()
    pool.join()






# print('hello', mystr)



import unittest
from pic.common.driver import browser
import logging
from  time import sleep

class StartEnd(unittest.TestCase):


    logging.basicConfig(level=logging.INFO)
    def setUp(self):

        # logging.info('======setUp %d=========' %self.test_num)
        # logging.info('======setUp=========')
        self.driver=browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)




    def tearDown(self):
        # logging.info('======tearDown=====')
        sleep(2)
        self.driver.quit()
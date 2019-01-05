import unittest

from selenium import webdriver


class FunctionalTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()

    def setUp(self):
        # print('='*20, 'Start of a test', '='*20)
        pass

    def tearDown(self):
        # print('='*20, 'End of the test', '='*20)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

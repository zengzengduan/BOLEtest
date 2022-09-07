import unittest
from HTMLTestRunner import HTMLTestRunner
import os
# from fillback import *
from config import *
from fillback import *

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''初始化测试环境'''
        print("初始化")

    @classmethod
    def tearDownClass(cls):
        '''结束测试'''
        print("结束")

    def setUp(self):
        os.chdir(FillbackPath)

    def tearDown(self):
        print("结束测试")

    def func_DT_fillback_file_1(self):
        self.assertTrue(func_DT_fillback_file_1())

    def func_DT_fillback_file_2(self):
        self.assertTrue(func_DT_fillback_file_2())

    def func_DT_fillback_file_3(self):
        self.assertTrue(func_DT_fillback_file_3())

    def func_DT_fillback_file_4(self):
        self.assertTrue(func_DT_fillback_file_4())

    def func_DT_fillback_file_5(self):
        self.assertTrue(func_DT_fillback_file_5())

    def func_DT_fillback_file_6(self):
        self.assertTrue(func_DT_fillback_file_6())

    def func_DT_fillback_file_7(self):
        self.assertTrue(func_DT_fillback_file_7())

    def func_DT_fillback_file_8(self):
        self.assertTrue(func_DT_fillback_file_8())

    def func_DT_fillback_file_9(self):
        self.assertTrue(func_DT_fillback_file_9())

    def func_DT_fillback_file_10(self):
        self.assertTrue(func_DT_fillback_file_10())

    def func_DT_fillback_file_11(self):
        self.assertTrue(func_DT_fillback_file_11())

    def func_DT_fillback_file_12(self):
        self.assertTrue(func_DT_fillback_file_12())

    def func_DT_fillback_file_13(self):
        self.assertTrue(func_DT_fillback_file_13())

    def func_DT_fillback_file_14(self):
        self.assertTrue(func_DT_fillback_file_14())

    def func_DT_fillback_file_16(self):
        self.assertTrue(func_DT_fillback_file_16())

    @unittest.skip("do't run as not ready")
    def test_skip(self):
        """Test method"""
        print("do something before test : prepare environment.\n")


if __name__ == '__main__':
    report_title = "fillback test"
    filepath = os.path.join(os.getcwd(), 'Report', 'fillbacktest.html')  # os.getcwd()获取当前的路径
    fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    tests = [
                TestDemo("func_DT_fillback_file_1"),
                TestDemo("func_DT_fillback_file_2"),
                TestDemo("func_DT_fillback_file_3"),
                TestDemo("func_DT_fillback_file_4"),
                TestDemo("func_DT_fillback_file_5"),
                TestDemo("func_DT_fillback_file_6"),
                TestDemo("func_DT_fillback_file_7"),
                TestDemo("func_DT_fillback_file_8"),
                TestDemo("func_DT_fillback_file_9"),
                TestDemo("func_DT_fillback_file_10"),
                TestDemo("func_DT_fillback_file_11"),
                TestDemo("func_DT_fillback_file_12"),
                TestDemo("func_DT_fillback_file_13"),
                TestDemo("func_DT_fillback_file_14"),
                TestDemo("func_DT_fillback_file_16"),
                
            ]

    suite.addTests(tests)
    runner = HTMLTestRunner(stream=fp, title=report_title, description="V1.0")
    runner.run(suite)
    fp.close()


import unittest


class Test1(unittest.TestCase):

    def setUp(self):
        print('setUp...')


    def test_1(self):
        self.assertTrue(1==1)  # 判断d是否是dict类型

    def test_2(self):
        self.assertTrue(1==0)  # 判断d是否是dict类型


    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
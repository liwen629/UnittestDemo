import unittest


class Test3(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def test_5(self):
        self.assertTrue(1 == 1)  # 判断d是否是dict类型

    def test_6(self):
        self.assertTrue(1 == 0)  # 判断d是否是dict类型

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
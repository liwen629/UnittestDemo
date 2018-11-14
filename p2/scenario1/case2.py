import unittest


class Test2(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def test_3(self):
        self.assertTrue(1 == 1)  # 判断d是否是dict类型

    def test_4(self):
        self.assertTrue(1 == 0)  # 判断d是否是dict类型

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
import unittest
import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

'''
suite = unittest.TestSuite()
tests = [Test1("test.*"), Test2("test.*"), Test3("test.*")]
suite.addTests(tests)

'''

#test_dir=r'C:\UsersKevin\PycharmProjects\UnittestDemo\p1\scenario2'
test_dir=current_directory
discover=unittest.defaultTestLoader.discover(test_dir,pattern='case*.py')
runner = unittest.TextTestRunner()
runner.run(discover)


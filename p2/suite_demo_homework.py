import unittest
import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)


test_dir=current_directory
discover=unittest.defaultTestLoader.discover(test_dir,pattern='homework*.py')
runner = unittest.TextTestRunner()
runner.run(discover)


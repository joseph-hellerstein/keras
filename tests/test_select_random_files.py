import src.constants as cn
from select_random_files import main

import os
import shutil
import unittest


IGNORE_TEST = False
IS_PLOT = False
TO_DIR = os.path.join(cn.TEST_DIR, "test_todir")
FROM_DIR = os.path.join(cn.TEST_DIR, "test_fromdir")
DIRS = [TO_DIR, FROM_DIR]


#############################
# Tests
#############################
class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.remove()

    def remove(self):
        for dir_name in DIRS:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)

    def tearDown(self):
        self.remove()

    def makeFromDir(self, tot_file:int):
        if not os.path.exists(FROM_DIR):
            os.makedirs(FROM_DIR)
        for idx in range(tot_file):
            ffile = os.path.join(FROM_DIR, "file%d" % idx)
            with open(ffile, "w") as f:
                f.write("This is file %d" % idx)


    def test_main(self):
        if IGNORE_TEST:
            return
        NUM_FILE = 2
        TOT_FILE = 4
        self.makeFromDir(TOT_FILE)
        main(FROM_DIR, TO_DIR, NUM_FILE)
        ffiles = os.listdir(TO_DIR)
        self.assertTrue(len(ffiles) == NUM_FILE)
        
        
        

if __name__ == '__main__':
    unittest.main()

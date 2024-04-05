import src.constants as cn
import util  # type: ignore

import os
import shutil
import unittest
from typing import List


IGNORE_TEST = False
IS_PLOT = False
TEST_ROOT_DIR = os.path.join(cn.TEST_DIR, "select")
FROM_NAME = "from"
TO_NAME = "to"


#############################
# Tests
#############################
class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.remove()

    def remove(self, path=TEST_ROOT_DIR):
        if os.path.exists(path):
            shutil.rmtree(path)

    def tearDown(self):
        self.remove()

    def makePath(self, names:List[str], root_dir:str=TEST_ROOT_DIR):
        path = root_dir
        for name in names:
            path = os.path.join(path, name)
        return path

    def makeFromDir(self, from_names:List[str]=[FROM_NAME], sub_dirs:List[str]=["0"], num_file:int=10)->str:
        # Copies files to the desired directory structure
        # from_dir = paths within tmp
        from_path = self.makePath(from_names)
        self.remove(path=from_path)
        for sub_dir in sub_dirs:
            local_dir = os.path.join(from_path, sub_dir)
            os.makedirs(local_dir)
            for idx in range(num_file):
                ffile = os.path.join(local_dir, "file%d.txt" % idx)
                with open(ffile, "w") as f:
                    f.write("This is file %d" % idx)
        return from_path

    def testCopyFiles(self):
        if IGNORE_TEST:
            return
        NUM_FILE = 2
        TOT_FILE = 4
        SUB_DIR = "0"
        self.makeFromDir([FROM_NAME], sub_dirs=[SUB_DIR], num_file=TOT_FILE)
        from_dir = self.makePath([FROM_NAME, SUB_DIR])
        to_dir = self.makePath([TO_NAME, SUB_DIR])
        util.copyFiles(from_dir, to_dir, NUM_FILE)
        ffiles = os.listdir(to_dir)
        self.assertTrue(len(ffiles) == NUM_FILE)

    def testMakeDirs(self):
        if IGNORE_TEST:
            return
        TOT_FILE = 4
        SUB_DIR3 = "3"
        SUB_DIR7 = "7"
        TRAIN_COUNT = 5
        TEST_COUNT = 2
        def test(directory):
            dirs = os.listdir(directory)
            diff = set(dirs).symmetric_difference([SUB_DIR3, SUB_DIR7])
            self.assertEqual(len(diff), 0)
        #
        root_from_dir = os.path.join(TEST_ROOT_DIR, FROM_NAME)
        testing_dir = self.makeFromDir([FROM_NAME, cn.TESTING], sub_dirs=[SUB_DIR3, SUB_DIR7], num_file=TOT_FILE)
        training_dir = self.makeFromDir([FROM_NAME, cn.TRAINING], sub_dirs=[SUB_DIR3, SUB_DIR7], num_file=TOT_FILE)
        root_to_dir = os.path.join(TEST_ROOT_DIR, TO_NAME)
        util.makeDigitDirs(train_count=TRAIN_COUNT, test_count=TEST_COUNT, sub_dirs=[SUB_DIR3, SUB_DIR7], root_from_dir=root_from_dir,
                    root_to_dir=root_to_dir)
        test(testing_dir)
        test(training_dir)

    def testMakeDirs2(self):
        if IGNORE_TEST:
            return
        pass
        #util.makeDigitDirs(train_count=20, sub_dirs=["0", "1"])
        
        
if __name__ == '__main__':
    unittest.main()
import src.constants as cn
import src.populate_bird_plane as pbp

import os
import unittest


IGNORE_TEST = False
IS_PLOT = False
DIRECTORY = os.path.join(cn.TEST_DIR, "test_images")
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)


#############################
# Tests
#############################
class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_populate(self):
        if IGNORE_TEST:
            return
        key = "bird"
        # Test
        for ffile in os.listdir(DIRECTORY):
            path = os.path.join(DIRECTORY, ffile)
            os.remove(path)
        max_result = 2
        directory = os.path.join(cn.TEST_DIR, "test_images")
        count = pbp.populate(key, directory=directory, max_result=max_result, max_size=4000*4000)
        self.assertTrue(count == max_result)
        

if __name__ == '__main__':
    unittest.main()

'''Utilities used in support of learning'''

import constants as cn

import argparse
import os
import numpy as np
import shutil
from typing import List, Optional


TESTING = "testing"
TRAINING = "training"


def copyFiles(from_dir:str, to_dir:str, num_files:int):
    """
    Selects a random subset of models in a directory and copies them to another directory.

    Args:
        from_dir: The directory to select files from.
        to_dir: The directory to copy files to.
        num_files: The number of files to copy. if < 0, all files are copied.
    """
    if not os.path.exists(from_dir):
        raise ValueError("Directory %s does not exist." % from_dir)
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
    ffiles = os.listdir(from_dir)
    if num_files < 0:
        num_files = len(ffiles)
    if num_files >= len(ffiles):
        sel_ffiles = ffiles
    else:
        idxs = np.random.choice(len(ffiles), num_files, replace=False)
        sel_ffiles = [ffiles[idx] for idx in idxs]
    for ffile in sel_ffiles:
        file_path = os.path.join(from_dir, ffile)
        new_file_path = os.path.join(to_dir, ffile)
        shutil.copy(file_path, new_file_path)

def makeDigitDirs(train_count:Optional[int]=100, test_count:Optional[int]=None, root_from_dir:str=cn.DATA_MNIST_FULL, 
             root_to_dir:str=cn.DATA_MNIST_SMALL, sub_dirs:List[str]=["0"]):
    """
    Creates training and test directories of the specified sizes

    Args:
        train_count: The number of training files.
        test_count: The number of test files.
    """
    if test_count is None:
        test_count = int(0.2*train_count)
    if len(sub_dirs) == 0:
        sub_dirs = [str(n) for n in range(cn.NUM_DIGIT)]
    is_error = False
    try:
        trues = [int(d) in range(cn.NUM_DIGIT) for d in sub_dirs]
    except:
        is_error = True
    if is_error or not all(trues):
        raise ValueError("Directories must be integers between 0 and %d." % (cn.NUM_DIGIT - 1))
    #
    count_dct = {TRAINING: train_count, TESTING: test_count}
    for phase_name in [TESTING, TRAINING]:
        phase_dir = os.path.join(root_to_dir, phase_name)
        if os.path.exists(phase_dir):
            shutil.rmtree(phase_dir)
        for sub_dir in sub_dirs:
            from_dir = os.path.join(root_from_dir, phase_name, str(sub_dir))
            to_dir = os.path.join(root_to_dir, phase_name, str(sub_dir))
            if os.path.exists(to_dir):
                shutil.rmtree(to_dir)
            os.makedirs(to_dir)
            copyFiles(from_dir, to_dir, count_dct[phase_name])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description='Copy randomly selected files')
    parser.add_argument('train_count', type=int, default=-1,
                    help='number of files in training data (-1 is all)')
    parser.add_argument('test_count', type=int, default=-1,
                    help='number of files in test data (-1 is all)')
    parser.add_argument('directories', metavar='N', type=int, nargs='*',
                    help='directories to copy files to')
    args = parser.parse_args()
    makeDigitDirs(args.from_dir, args.to_dir, args.count)
'''Selects a random subset of files from a directoyr.'''

import os
import numpy as np
from PIL import Image # type: ignore
import argparse

import constants as cn


def main(from_dir:str, to_dir:str, num_files:int):
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
        os.system("cp %s %s" % (file_path, new_file_path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description='Copy randomly selected files')
    parser.add_argument('from_dir', type=str,
                    help='from directory that contains files to copy')
    parser.add_argument('to_dir', type=str,
                    help='directory where files are copied')
    parser.add_argument('count', type=int, default=-1,
                    help='number of files to copy (-1 is all)')
    args = parser.parse_args()
    main(args.from_dir, args.to_dir, args.count)
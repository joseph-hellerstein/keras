'''Populate data for bird and plane models'''

from duckduckgo_search import DDGS
from fastdownload import download_url  # type: ignore
import os
import numpy as np
from PIL import Image # type: ignore

import constants as cn


MAX_RESULT = 10000

def populate(key:str, directory=None, max_result=10, max_size=2000*2000):
    """
    Acquires images and places them in a directory
    """
    if directory is None:
        if " " in key:
            raise ValueError("Must specify valid directory path")
        else:
            directory = os.path.join(cn.DATA_DIR, key)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Do the search
    results = DDGS().images(key, max_results=1000000)
    # Download the files
    count = 0
    for _ in range(max_result):
        idx = np.random.randint(0, len(results))
        dct = results[idx]
        if "image" in dct:
            if ("width" in dct) and ("height" in dct):
                size = dct["width"]*dct["height"]
                if size > max_size:
                    continue
            url = dct["image"]
            file_path = os.path.join(directory, url.split("/")[-1])
            if os.path.isfile(file_path):
                continue              
            try:
                download_url(url, directory, show_progress=True)
                count += 1
            except:
                print("Download failed: %s" % url)
    return count

def convertFiles(directory, size=(256, 256)):
    """
    Convert all images in a directory to png format of the same size.
    """
    for ffile in os.listdir(directory):
        filename, file_extension = os.path.splitext(ffile)
        path = os.path.join(directory, ffile)
        if not file_extension in [".png", ".jpg"]:
            print("***Skipping %s. Unrecognized extension." % path)
            continue
        image = Image.open(path)
        if file_extension == ".png":
            save_path = filename + ".pngsave"
            image.save(save_path)
        image.to_thumb(256, 256)
        new_path = filename + ".png"
        image.save(new_path)

pilImage1 = pilImage.rotate(-90, expand=1)
pilImage1.to_thumb(256, 256)
#new_image = pilImage.resize((256, 256))
#new_image.save("image.png")

if __name__ == "__main__":
    num_bird = populate("bird", max_result=MAX_RESULT)
    print("Number of bird images: %d" % num_bird)
    num_plane = populate("plane", max_result=MAX_RESULT)
    print("Number of plane images: %d" % num_plane)
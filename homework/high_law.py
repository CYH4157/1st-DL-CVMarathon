
import matplotlib.pyplot as plt 
import os

import scipy.misc
import numpy as np
import PIL.Image as Image

def convert_3d(r):
    s = np.empty(r.shape, dtype=np.uint8)
    for j in range(r.shape[0]):
        for i in range(r.shape[1]):
            s[j][i] = (r[j][i] / 255) ** 0.67 * 255
    return s


im = plt.imread('D:/第一屆ai競賽/第一屆ai競賽/TRAIN/all_train/2001_4000/02003.tif')

im_mat = scipy.misc.fromimage(im)
im_converted_mat = convert_3d(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.show()
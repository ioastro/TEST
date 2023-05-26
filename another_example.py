import json as J
from PIL import Image
import numpy as np
import os
def padding(json,image):
    with open(json, 'r') as f:
        temp = J.loads(f.read())
    points = np.array(temp['shapes'][0]['points'])
    img_arr =np.array(Image.open(image))
    a = int(points[0,0])
    b = int(points[0,1])
    c = int(points[1,0])
    d = int(points[1,1])
    img_arr[0:a,:,:] = 0
    img_arr[:, 0:b, :] = 0
    img_arr[c:649, :, :] = 0
    img_arr[:, d:649, :] = 0
    new_img = Image.fromarray(img_arr)
    return new_img


    img_arr =np.array(Image.open(image))
    a = int(points[0,0])
    b = int(points[0,1])
    c = int(points[1,0])
    d = int(points[1,1])
    img_arr[0:a,:,:] = 0
    img_arr[:, 0:b, :] = 0
    img_arr[c:649, :, :] = 0
    img_arr[:, d:649, :] = 0
    new_img = Image.fromarray(img_arr)
    return new_img




import json as J
from PIL import Image
import numpy as np
import os

root_path = '' # Path where JPGs are
output_path = '' # Path where you want to save your padded images
for file_name in os.listdir(root_path):
    if os.path.splitext(file_name)[1]=='.jpg':
        j_name = os.path.splitext(file_name)[0]
        j_file = root_path + '\\'+ j_name +'.json'
        img_file = root_path + '\\'+ file_name
        padded_img = padding(j_file,img_file)
        padded_img.save(output_path+'\\'+file_name)
        




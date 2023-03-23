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

root_path = '' # Path where JPGs are
output_path = '' # Path where you want to save your padded images
for file_name in os.listdir(root_path):
    if os.path.splitext(file_name)[1]=='.jpg':
        j_name = os.path.splitext(file_name)[0]
        j_file = root_path + '\\'+ j_name +'.json'
        img_file = root_path + '\\'+ file_name
        padded_img = padding(j_file,img_file)
        padded_img.save(output_path+'\\'+file_name)




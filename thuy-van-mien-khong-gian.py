from PIL import Image
import numpy as np
import sys


cover_AT140101 = Image.open("cover_watermark.jpg")


watermark_AT140101 = Image.open("watermark.jpg")


cW,rW = watermark_AT140101.size


cover_sequence = cover_AT140101.convert("RGB")
cover_array = np.array(cover_sequence)


water_sequence = watermark_AT140101.convert("RGB")
w_arr = np.array(water_sequence)


HAdd = cover_array.copy()

#Vòng lặp 3 chiều
for channel in range(3):
    for i in range(rW):
        for j in range(cW):
            HAdd[i,j+470,channel] = w_arr[i,j,channel]

ketqua = Image.fromarray(HAdd,'RGB')


ketqua.save('ketqua_04_AT140101.png')



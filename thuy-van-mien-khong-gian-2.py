from PIL import Image
import numpy as np
import sys


cover = Image.open("cover_watermark.jpg")


watermark = Image.open("watermark.jpg")


cW,rW = watermark.size


cover_sequence = cover.convert("RGB")
cover_array = np.array(cover_sequence)


water_sequence = watermark.convert("RGB")
w_arr = np.array(water_sequence)


k = np.zeros((rW, cW),dtype = np.uint8)

s = int(input("Nhap he so: "))


a = s + k


HAdd = cover_array.copy()

#Vòng lặp 3 chiều
for channel in range(3):
    for i in range(rW):
        for j in range(cW):         
            HAdd[i,j+470,channel] = (int(HAdd[i,j+470,channel]) + int((a[i,j]*w_arr[i,j,channel])))/2

ketqua = Image.fromarray(HAdd,'RGB')


ketqua.save('ketqua_05_AT140101.png')



print(cover_array)
print("-----------------------------------")
print("-----------------------------------")
print(HAdd)

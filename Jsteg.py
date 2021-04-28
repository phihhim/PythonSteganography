import numpy as np
from PIL import Image
from scipy.fftpack import dct, idct

def dct2(a):
    return dct(dct(a.T, norm='ortho'), norm='ortho')


def idct2(a):
    return idct(idct(a.T, norm='ortho'), norm='ortho')

cover_AT140101 = Image.open("cover_AT140101.png")
height, width  = cover_AT140101.size
matrix_AT140101 = cover_AT140101.convert("RGB")
arr = np.array(matrix_AT140101, dtype=np.uint8)

msg_AT140101 = "kythuatgiautin"
msg_array_AT140101 = list(''.join(format(ord(x), 'b') for x in msg_AT140101))
len_array = len(msg_array_AT140101)
steg_arr = arr.copy()

for k in range(3):
    for i in range(0,height,8):
        for j in range(0,width,8):
            steg_arr[i:i+7,j:j+7,k] = dct2(steg_arr[i:i+7,j:j+7,k])

for k in range(3):
    for i in range(0,height):
        for j in range(0,width):
            if (i == 0) and j == (0):
                pass
            elif (i%8 == 0) and (j%8==0):
                pass
            elif msg_array_AT140101:
                if msg_array_AT140101[0] != (steg_arr[i,j,k]%2):
                    if (steg_arr[i,j,k]%2) == 1:
                        steg_arr[i, j, k] -=1
                    else:
                        steg_arr[i, j, k] += 1
                msg_array_AT140101.pop()
            else:
                break
        if not msg_array_AT140101:
            break
    if not msg_array_AT140101:
        break

for k in range(3):
    for i in range(0,height,8):
        for j in range(0,width,8):
            if msg_array_AT140101:
                steg_arr[i:i+7,j:j+7,k] = idct2(steg_arr[i:i+7,j:j+7,k])


ketqua = Image.fromarray(steg_arr,'RGB')
ketqua.save('ketqua_AT140101.png')



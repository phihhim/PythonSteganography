from PIL import Image
import numpy as np

#LSB tuan tu
cover_AT140101 = Image.open("cover_AT140101.png")
height, width  = cover_AT140101.size
matrix_AT140101 = cover_AT140101.convert("RGB")
arr = np.array(matrix_AT140101, dtype=np.uint8)

msg_AT140101 = "kythuatgiautin"
msg_array_AT140101 = list(''.join(format(ord(x), 'b') for x in msg_AT140101))

steg_arr = arr.copy()

for k in range(3):
    for i in range(height):
        for j in range(height):
            if msg_array_AT140101:
                LSB = int(msg_array_AT140101[0])
                if LSB != (steg_arr[i,j,k]%2):
                    if steg_arr[i,j,k]%2 == 1:
                        steg_arr[i,j,k] = steg_arr[i,j,k] - 1
                    else:
                        steg_arr[i, j, k] = steg_arr[i, j, k] + 1
                msg_array_AT140101.pop()
            else:
                break
        if not msg_array_AT140101:
            break
    if not msg_array_AT140101:
        break

ketqua = Image.fromarray(steg_arr,'RGB')
ketqua.save('ketqua_01_AT140101.png')
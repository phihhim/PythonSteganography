from PIL import Image
import numpy as np
import random

#LSB ngau nhien
cover_AT140101 = Image.open("cover_AT140101.png")
height, width  = cover_AT140101.size
matrix_AT140101 = cover_AT140101.convert("RGB")
arr = np.array(matrix_AT140101, dtype=np.uint8)

msg_AT140101 = "kythuatgiautin"
msg_array_AT140101 = list(''.join(format(ord(x), 'b') for x in msg_AT140101))
msg_len = len(msg_array_AT140101)
print(msg_len)
print(msg_array_AT140101)

random_row = random.sample(range(1, width), len(msg_array_AT140101))
random_column = random.sample(range(1, height), len(msg_array_AT140101))
random_channel = np.random.randint(3, size = len(msg_array_AT140101))

steg_arr = arr.copy()

for i in range(msg_len):
    row = random_row[0]
    column = random_column[0]
    channel = random_channel[0]
    random_pixel = steg_arr[column, row, channel]
    if int(msg_array_AT140101[0]) != (random_pixel%2):
        if random_pixel%2 == 1:
            steg_arr[column, row, channel] -= 1
        else:
            steg_arr[column, row, channel] += 1
    msg_array_AT140101.pop()

ketqua = Image.fromarray(steg_arr,'RGB')
ketqua.save('ketqua_02_AT140101.png')

khoaK = open("LBS_ngaunhien.txt", "w")
for i in range(msg_len):
    khoaK.write(str(random_row[i]) + " " + str(random_column[i]) + " " + str(random_channel[i]) + "\n")
khoaK.close()

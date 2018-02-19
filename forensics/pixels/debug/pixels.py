from PIL import Image
import random

im = Image.open("logo_ori.png")
pix = im.load()

flag = "treeCTF{hello_pixels_my_old_friend}"


# clean up non-flag ASCII values in transparency (basiaclly the gray pixels in the original image)
for i in range(im.size[0]):
  for j in range(im.size[1]):
    if pix[i, j][3] not in [255, 0]:
      pix[i, j] = (255, 255, 255, 255)


row_start = 137
for c in flag:
  val = ord(c)
  i = 0
  while pix[row_start,i] == (255, 255, 255, 0):
    i += 1
  pix[row_start, i+3] = (255, 255, 255, val)
  row_start += 1
  #print(row_start-1, i-1)

# put in some noise, so you can't just diff the images

for r in range(100):
    i = random.randint(0, 136)
    j = random.randint(0, im.size[1]-1)
    pix[i, j] = (255, 255, 255, random.randint(0, 255))



im.save("logo.png")
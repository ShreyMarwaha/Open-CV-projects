#from _future_ import print_function
from cv2 import cv2
import numpy as np
import imageio
# from skimage.transform import resize



inp = cv2.VideoCapture(0)

inpWid  = inp.get(cv2.CAP_PROP_FRAME_WIDTH)
inpHig = inp.get(cv2.CAP_PROP_FRAME_HEIGHT)


xface="./1Face.gif"
gif = imageio.mimread(xface)
nums = len(gif)
print("Total {} frames in the gif!".format(nums))
imgs = [cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA) for img in gif]
i = 0



while True:
    _, frame = inp.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
   
    i = (i + 1) % nums
    imgs[i] = cv2.resize(imgs[i] , (120,120))

    # Create a mask
mask = np.zeros_like (binary)
# Fill the outline (pixels not transparent) with 255.
for cnt in contours:
    cv2.drawContours (mask, contours, -1, color = 255, thickness = -1)
# Convert to RGBA
rgba = cv2.cvtColor (img, cv2.COLOR_RGB2RGBA)
# Set the mask to the alpha channel.
rgba [..., 3] = mask



    x_offset = int((inpWid-imgs[i].shape[0])/2)
    y_offset = int(inpHig-imgs[i].shape[1])
    frame[y_offset:y_offset+imgs[i].shape[0], x_offset:x_offset+imgs[i].shape[1]] = imgs[i]

    # alpha = 1
    # cv2.addWeighted(imgs[i].copy(), alpha, imgs[i].copy(), 1 - alpha, 0, imgs[i].copy())

    

    cv2.imshow('ComputerVision', frame)
    key = cv2.waitKey(1)

    if(key == 32):
        break

cv2.destroyAllWindows()
inp.release()


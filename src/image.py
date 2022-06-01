import numpy as np
import imageio.v3 as image
import matplotlib.pyplot as plot

picture_path = 'rose.jpg'
new_picture_path = 'newrose.jpg'

red_threshold = 230
signal_color = [255, 255, 0]

def change_color(color):
  crosses_threshold = color[0] >= red_threshold
  return signal_color if crosses_threshold else color

picture = image.imread(picture_path)
new_picture_data = [[change_color(picture[i,j]) for j in range(picture.shape[1])] for i in range(picture.shape[0])]
new_rose = np.array(new_picture_data, np.uint8)

image.imwrite(new_picture_path, new_rose)

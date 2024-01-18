import imageio
import numpy as np
from PIL import Image

xm = 108
xp = 48
ym = 62
yp = 62

im = imageio.imread('table_v2.png')/255.
#im[:, :] = [1.0, 0.8, 0.8][0.70980392, 0.80784314, 0.87843137]
im[235-xm: 235+xp, 235-ym: 235+yp] = [0.9, 0.9, 0.9]
pim = Image.fromarray((255*im).astype(np.uint8))
pim.save('table_test.png')

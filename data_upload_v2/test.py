import cv2
import os
import numpy as np
import pandas as pd

img_array = []
for img in os.listdir("train/covid")[:10]:
    img_arr = cv2.imread("train/covid/"+img, 0).flatten()
    img_array.append(img_arr)
df = pd.DataFrame(data = img_array)
print(df)

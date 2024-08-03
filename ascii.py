import cv2
import numpy as np


ascii_chars = ["$","@","B","%","8","&", "W", "M", "#","*", ";",":",",","^","."]

image = cv2.imread("C:/Users/jaedo/OneDrive/Desktop/Ascii/catf.png")

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height,width = img_gray.shape
new_height = height //12 
new_width = width // 12
resize_img = cv2.resize(img_gray,(new_width, new_height))
num_chars = len(ascii_chars)
ascii_str = ""

for i in range(new_height):
    for j in range(new_width):
        pixel = resize_img[i,j]
        ascii_str += ascii_chars[int(pixel / 255 * (num_chars-1))]

    ascii_str += "\n"

    
print(ascii_str)
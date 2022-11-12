import numpy as np
import cv2
import os

def show_image(imgFile):
# Shows image on GUI
    cv2.imshow("image", imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image_matrix(dirname):
# Reads all .jpg files in a directory and converts them into image vectors, stored in a matrix
    mtx = np.array([])
    first = True
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".jpg"):
                filename = os.path.join(root, file)
                img = cv2.imread(filename, 0)
                resized = cv2.resize(img, (256, 256))
                flat = resized.flatten()
                if first:
                    mtx = flat.reshape(len(flat), 1)
                    first = False
                else:
                    mtx = np.hstack((mtx, flat.reshape(len(flat), 1)))
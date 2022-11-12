import numpy as np
import ZipFile
import cv2
import os

def extract(filename):
    # Unzipping zip files menjadi folder
    with ZipFile(filename, 'r') as zip:
    zip.extractall()

    # Notifikasi extracting berhasil
    print('Done extracting!')

def norm(img):
    return (img - np.amin(img))*(255/(np.amax(img)-np.amin(img)))

def list_files(filepath, filetype):
    # Mengembalikan array berisi pathfiles
    # Kamus
    paths = []
    # Algoritma
    for root, dirs, files in os.walk(filepath):
def norm(img):
    return (img - np.amin(img))*(255/(np.amax(img)-np.amin(img)))

def image_matrix(dirname):
# Reads all .jpg files in a directory and converts them into image vectors, stored in a matrix
    mtx = np.array([])
    first = True
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return (paths)

def image_to_matrix(dirname):
    # Mengembalikan kumpulan matrix dari folder dataset yang tersedia
    # Kamus
    # P : Array of filepaths
    M = np.array([])
    first = True

    # Algoritma
    P = list_files(dirname, ".jpg")
    for data in P:
        # Konversi image ke matrix
        img = norm(cv2.imread(data, 0))
        resized = norm(cv2.resize(img, (256, 256)))
        flat = resized.flatten()  
        if first:
            M = flat.reshape(len(flat), 1)
            first = False
        else:
            M = np.hstack((M, flat.reshape(len(flat), 1)))
    
    return(M)

def average_matrix(M):
    # Mengembalikan rata-rata semua matrix
    # Kamus
    MOut = np.array([])

    # Algoritma
    for i in range(0, M.shape[0]):
        count = 0
        for j in range(0, M.shape[1]):
            count += M[i][j]
        avg = count / M.shape[1]
        MOut = np.append(MOut, avg)
    return MOut

def show_matrix_as_img(M):
    # Mengembalikan display image dari Matrix input
    # Kamus
    # Algoritma



    

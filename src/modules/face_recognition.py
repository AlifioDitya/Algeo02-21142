import numpy as np
import util as ut

def average_face(matrix):
    avgFace = np.mean(matrix, axis=1)
    vector = avgFace.reshape(len(avgFace), 1)
    return vector

def deviation(matrix):
    avg = average_face(matrix)
    diff = np.subtract(matrix, avg)
    return diff

def covariance(matrix):
    A = deviation(matrix)
    return np.transpose(A) @ A

# arr = np.array([[1, 3], [3, 1]])
# val, vec = np.linalg.eig(arr)
# print(vec)
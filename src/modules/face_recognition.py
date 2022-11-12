import numpy as np

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

def eigenface(matrix):
    A = deviation(matrix)
    val, vec = np.linalg.eig(covariance(matrix))
    arr = np.array([[]])
    first = True
    for i in range(len(vec[0])):
        if first:
            arr = np.array([A @ vec[:, i]]).transpose()
            first = False
        else:
            arr = np.hstack((arr, np.array([A @ vec[:, i]]).transpose()))
    return arr
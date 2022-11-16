import numpy as np
import modules.eigen as eg

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
    return (np.transpose(A) @ A)

def eigenface(matrix, rank):
    if rank > len(matrix[0]) or rank < 0:
        rank = len(matrix[0])
    
    A = deviation(matrix)  # training_set - avg_face
    val, vec = eg.eig(covariance(matrix))  # eigenvectors sorted and normalized

    arr = []
    for i in range(rank):
        arr.append((A @ vec[:, i])/np.linalg.norm(A @ vec[:, i]))
    
    return np.array(arr).T

def euc_distance(v1, v2):
    diff = v1 - v2
    product = np.dot(diff.T, diff)
    return np.sqrt(product)
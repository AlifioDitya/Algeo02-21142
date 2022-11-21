from modules.face_recognition import (eigenface, average_face, deviation, euc_distance)
from modules.util import (extract, image_to_matrix, image_matrix_file, show_image, fixBadZipfile)
from modules.config import ROOT_DIR
import matplotlib.pyplot as plt
import os
import numpy as np

def index(dataset, test, isDatasetZip=True):
# Face recognition algorithm
# Extracts dataset if dataset is a zip file
# Otherwise, dataset is a folder
    if isDatasetZip:
        fixBadZipfile(dataset)
        extract(dataset)

    training_set = image_to_matrix(dataset)
    eigen_face = eigenface(training_set, len(training_set[0]))
    training_weight = eigen_face.T @ deviation(training_set)

    test_img = image_matrix_file(test)
    diff = test_img - average_face(training_set)
    test_weight = eigen_face.T @ diff

    d = np.array([euc_distance(test_weight[:, 0], training_weight[:, i]) for i in range(len(training_weight[0]))])
    toll = 0.75*np.amax(d)
    if np.amin(d) < toll:
        idx = np.where(d == np.amin(d))
        identified = training_set[:, idx]
        output_dir = os.path.join(ROOT_DIR, "../output")
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        plt.imsave(os.path.join(output_dir, "output.jpg"), identified.reshape(256, 256), cmap="gray")
        return (True, os.path.join(output_dir, "output.jpg"))
    else:
        return(False, test)
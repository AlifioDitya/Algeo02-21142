from modules.face_recognition import (eigenface, average_face, deviation, covariance, recognize)
from modules.util import (extract, image_to_matrix, show_image)
from modules.config import ROOT_DIR
import os
import cv2

# Have:
# Path of dataset file in zip
# Path of test image
# Need:
# Path of file of closest result image
# Filename of result file

def index(dataset_file, test_file):
    extract(dataset_file)
    
    training_set = image_to_matrix(os.path.join(ROOT_DIR, "extracted"))
    test_img = image_to_matrix(test_file)

    eigen_face = eigenface(training_set, len(training_set[0]))
    training_weight = eigen_face.T @ deviation(training_set)
    test_weight = eigen_face.T @ (test_img - average_face(training_set))

    return recognize(training_set, test_weight, training_weight)
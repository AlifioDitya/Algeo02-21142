import cv2
from time import sleep

from PIL import Image
import numpy as np


def webcamFunc():
# inspo: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    webCam = cv2.VideoCapture(0)

    while True:
        if not webCam.isOpened():
            print('no camera input')
            sleep(5)
            pass

        # Frame by frame capture
        capt, frame = webCam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        cv2.putText(frame, "Please stay in the centre", (450, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

        # kotak ijo
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        # Display the resulting frame
        cv2.imshow('WebCam', frame)

        # click buat moto
        if cv2.waitKey(1) & 0xFF == ord('c'): 
            check, frame = webCam.read()
            cv2.imshow("Capturing...", frame)
            cv2.imwrite(filename='hasilWebcam.jpg', img=frame)
            webCam.release()
            img_new = cv2.imread('hasilWebcam.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            print("Image Saved")
            cv2.destroyAllWindows()
            break
    
        # click buat exit
        elif cv2.waitKey(1) & 0xFF == ord('e'):
            print("Turning off camera.")
            webCam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

        # Display
        cv2.imshow('WebCam', frame)

    # capture release
    webCam.release()
    cv2.destroyAllWindows()

    # ubah ke ratio 1:1
    #from PIL import Image
    #import numpy as np

    def cropImg(foto):
        l, p = foto.size    # p = panjang, l = lebar
        if l == p:
            return foto
        foto = np.array(foto)
        offset  = int(abs(p-l)/2)
        if l < p:
            foto = foto[offset:(p-offset),:,:]
        else:
            foto = foto[:,offset:(l-offset),:]
        return Image.fromarray(foto)

    foto = Image.open(r"hasilWebcam.jpg")
    cropped = cropImg(foto)
    cropped.save("hasilWebcam.jpg")   


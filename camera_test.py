import cv2
import time


# 　参考にしたコード
def check_camera_connection():
    """
    Check the connection between the camera numbers and the computer.

    """
    true_camera_is = []

    # check the camera number from 0 to 9
    for camera_number in range(0, 10):
        cap = cv2.VideoCapture(camera_number)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(camera_number)
            print("port number", camera_number, "Find!")

        else:
            print("port number", camera_number, "None")
    print("Connected camera", len(true_camera_is))


check_camera_connection()

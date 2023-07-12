import cv2
from datetime import datetime
import sys
import time
import os
import threading
import platform


class VideoCapture:
    PREFIX: str = ""
    PATH: str = ""
    DIR: str = ""
    FPS: int
    CAMERA_ID: int
    CAMERA_WIDTH: int
    CAMERA_HEIGHT: int
    RECORD_STATUS: bool = False
    OS: str = platform.system()

    camera: cv2.VideoCapture = None
    video: cv2.VideoWriter = None
    fourcc: cv2.VideoWriter_fourcc = None
    frame_count: int = 0
    thread: threading.Thread = None

    def __init__(self, prefix: str, dir: str, fps: int, camera_id: int):
        # init
        self.PREFIX = prefix
        self.PATH = ""
        self.DIR = dir
        self.CAMERA_ID = camera_id

        self.camera = cv2.VideoCapture(camera_id)
        self.frame_count = 0

        # set camera fps
        self.set_fps(fps)

        # get camera frame size
        self.CAMERA_WIDTH = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.CAMERA_HEIGHT = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # set video decode format
        self.fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

        if not os.path.exists(self.DIR):
            os.mkdir(self.DIR)

        print(
            "fps: ",
            self.camera.get(cv2.CAP_PROP_FPS),
            "width: ",
            self.CAMERA_WIDTH,
            "height: ",
            self.CAMERA_HEIGHT,
        )

    # def __del__(self):
    # self.camera.release()
    # cv2.destroyAllWindows()

    def get_camera(self):
        return self.camera

    def get_fps(self):
        return self.FPS

    def get_path(self):
        return self.PATH

    def get_camera_id(self):
        return self.CAMERA_ID

    def get_frame_count(self):
        return self.frame_count

    def set_fps(self, fps: int):
        self.FPS = fps
        self.camera.set(cv2.CAP_PROP_FPS, self.FPS)

    def isOpened(self):
        return self.camera.isOpened()

    def start(self):
        self.RECORD_STATUS = True

        self.PATH = f"{self.DIR}/{self.PREFIX}_camera{self.CAMERA_ID}_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S.%f')[:-3]}.mp4"
        self.video = cv2.VideoWriter(
            self.PATH,
            self.fourcc,
            self.FPS,
            (self.CAMERA_WIDTH, self.CAMERA_HEIGHT),
        )

        self.thread = threading.Thread(target=self.captureAndRecord)
        self.thread.start()

    def captureAndRecord(self):
        while True:
            self.frame_count += 1
            ret, frame = self.camera.read()
            self.video.write(frame)
            if self.OS == "Windows":
                cv2.imshow("camera", frame)
            key = cv2.waitKey(1)

            if key == 27 or not self.RECORD_STATUS:
                break
        self.camera.release()
        self.video.release()
        cv2.destroyAllWindows()
        print("Finish record")
        return

    def stop(self):
        self.RECORD_STATUS = False


# FPS = 60

# camera = cv2.VideoCapture(1)

# if not camera.isOpened():
#     print("Camera is not opened")
#     sys.exit()

# camera.set(cv2.CAP_PROP_FPS, FPS)

# w = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
# h = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print("fps: ", camera.get(cv2.CAP_PROP_FPS), "width: ", w, "height: ", h)

# fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

# date = datetime.now().strftime("%Y%m%d_%H%M%S.%f")[:-3]
# print(date)

# if not os.path.exists("./video"):
#     os.mkdir("./video")

# path = "./video/" + date + ".mp4"
# video = cv2.VideoWriter(path, fourcc, FPS, (int(w), int(h)))

# time_start = time.time()

# limit_frame = 60 * FPS

# frame_count = 0

# while True:
#     frame_count += 1
#     ret, frame = camera.read()
#     video.write(frame)

#     cv2.imshow("camera", frame)
#     key = cv2.waitKey(1)

#     if frame_count == limit_frame or key == 27:
#         break

# camera.release()
# video.release()
# cv2.destroyAllWindows()
# print("finish")

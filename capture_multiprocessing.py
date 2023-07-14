import cv2
from datetime import datetime
import os
import platform


def multi_video_capture(
    prefix: str, dir: str, fps: int, w: int, h: int, camera_id: int, recode_time: int
):
    # init
    PREFIX = prefix
    PATH = ""
    DIR = dir
    CAMERA_ID = camera_id
    OS = platform.system()

    camera = cv2.VideoCapture(camera_id)
    frame_count = 0

    cv2.setNumThreads(0)

    # set camera fps
    FPS = fps
    camera.set(cv2.CAP_PROP_FPS, FPS)

    # set camera frame size
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

    # get camera frame size
    CAMERA_WIDTH = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    CAMERA_HEIGHT = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # set video decode format
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

    if not os.path.exists(DIR):
        os.mkdir(DIR)

    print(
        "fps: ",
        camera.get(cv2.CAP_PROP_FPS),
        "width: ",
        CAMERA_WIDTH,
        "height: ",
        CAMERA_HEIGHT,
    )

    PATH = f"{DIR}/{PREFIX}_camera{CAMERA_ID}_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S.%f')[:-3]}.mp4"
    video = cv2.VideoWriter(
        PATH,
        fourcc,
        FPS,
        (CAMERA_WIDTH, CAMERA_HEIGHT),
    )

    while True:
        frame_count += 1
        ret, frame = camera.read()
        video.write(frame)
        # if OS == "Windows":
        #     cv2.imshow("camera", frame)
        # key = cv2.waitKey(1)

        # if frame_count % 100 == 0:
        #     print(f"camera {CAMERA_ID}: {frame_count}")

        if frame_count >= FPS * recode_time:
            break

    camera.release()
    video.release()
    cv2.destroyAllWindows()
    print("Finish record")
    return

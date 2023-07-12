from arg import getArgs
from capture import VideoCapture
import time

camera_ids = [0, 1]
cameras = []

if __name__ == "__main__":
    args = getArgs()

    for index, camera_id in enumerate(camera_ids):
        camera = VideoCapture(
            prefix="test", dir="video", fps=args.fps, camera_id=camera_id
        )
        print(f"camera {camera_id}: {camera.isOpened()}")

        if camera.isOpened():
            cameras.append(camera)

    for camera in cameras:
        camera.start()

    time.sleep(10)

    for camera in cameras:
        camera.stop()

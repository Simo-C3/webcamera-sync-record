from arg import getArgs
from capture import VideoCapture
import time

if __name__ == "__main__":
    args = getArgs()
    video_capture0 = VideoCapture(prefix="test", dir="video", fps=args.fps, camera_id=0)
    video_capture1 = VideoCapture(prefix="test", dir="video", fps=args.fps, camera_id=1)

    print("camera: ", video_capture0.isOpened())
    print("camera: ", video_capture1.isOpened())

    print("fps: ", video_capture0.get_fps())
    print("fps: ", video_capture1.get_fps())

    video_capture0.start()
    video_capture1.start()

    time.sleep(10)

    video_capture0.stop()
    video_capture1.stop()

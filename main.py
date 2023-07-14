from arg import getArgs
from capture import VideoCapture
from capture_multiprocessing import multi_video_capture
import time
from multiprocessing import Process

if __name__ == "__main__":
    args = getArgs()

    camera_ids = args.cid.split(",")
    cameras = []
    processes = []

    if args.m:
        for index, camera_id in enumerate(camera_ids):
            process = Process(
                target=multi_video_capture,
                args=(
                    "test",
                    "video",
                    args.fps,
                    args.fw,
                    args.fh,
                    int(camera_id),
                    args.recode_time,
                ),
            )

            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()
    else:
        for index, camera_id in enumerate(camera_ids):
            camera = VideoCapture(
                prefix="test", dir="video", fps=args.fps, camera_id=int(camera_id)
            )
            print(f"camera {camera_id}: {camera.isOpened()}")

            if camera.isOpened():
                cameras.append(camera)

        for camera in cameras:
            camera.start()

        time.sleep(10)

        for camera in cameras:
            camera.stop()

import argparse

parser = argparse.ArgumentParser(description="Process some integers.")

parser.add_argument("--fps", type=int, default=30, help="動画のfpsを指定. default: 30")
parser.add_argument("--fw", type=int, help="動画のwidthを指定. default: カメラのwidth")
parser.add_argument("--fh", type=int, help="動画のheightを指定. default: カメラのheight")
parser.add_argument(
    "--cid", type=str, default="0", help="カメラIDを指定. default: 0. 複数指定する場合はカンマ区切りで指定"
)
parser.add_argument("-m", action="store_true", help="動画のwidthを指定. default: カメラのwidth")
parser.add_argument("--recode_time", type=int, default=10, help="録画時間を指定. default: 10")
parser.add_argument(
    "--prefix", type=str, default="test", help="動画のprefixを指定. default: test"
)
parser.add_argument(
    "--dir", type=str, default="video", help="動画の保存先を指定. default: video"
)
parser.add_argument(
    "--fourcc", type=str, default="mp4v", help="動画の保存形式を指定. default: mp4v"
)


def getArgs():
    args = parser.parse_args()
    print(args)
    return args

import argparse

parser = argparse.ArgumentParser(description="Process some integers.")

parser.add_argument("--fps", type=int, default=30, help="動画のfpsを指定. default: 30")
parser.add_argument("--w", type=int, help="動画のwidthを指定. default: カメラのwidth")


def getArgs():
    args = parser.parse_args()
    print(args)
    return args

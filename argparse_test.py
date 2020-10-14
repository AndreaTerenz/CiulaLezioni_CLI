import argparse

parser = argparse.ArgumentParser(description='test', usage="%(prog)s [-h] [[-o DIR] cookies url [url ...]]")

parser.add_argument("cookies", nargs=1, type=str, help="Path to cookies txt file")
parser.add_argument("url", type=str, nargs="+", help="Url of each video to be downloaded")

parser.add_argument("-o", "--out-dir", nargs=1, default="", metavar="DIR",
                    type=str, help="directory to download the videos in")

args = parser.parse_args()

print(vars(args)["url"])

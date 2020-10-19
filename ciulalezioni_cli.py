import sys, os
import youtube_dl
import argparse
from urllib.parse import urlparse

def check_url(url:str, log=False):
    if (url.strip() != ""):
        res = urlparse(url)
        valid = (res.scheme != "" and res.netloc != "")

        if log and not valid:
            print("Invalid url:" + url)

        return valid

    return False

def check_cookies_file(f:str):
    if (f.strip() != ""):
        return f.endswith(".txt") and os.path.isfile(f)

    return False

def get_input_urls():
    output = []
    
    i = 0
    exit = False

    while not exit:
        u = ""

        while not(check_url(u)) and not exit:
            prompt = f"Input url {i}>>" if i == 0 else f"Input url {i} (ENTER to stop)>>"
            u = input(prompt)
            exit = (u == "")

            if not(check_url(u)) and not exit:
                print("\tInvalid url - please try again")
        
        if not exit:
            i += 1
            output.append(u)
        
    return output

def get_cookies_file():
    output = ""

    while not check_cookies_file(output):
        output = input("Path to cookies file >>")

        if not(check_cookies_file(output)):
            print("\tInvalid path - please try again")
    
    return output

def get_args_from_usr():
    return get_input_urls(), get_cookies_file(), input("Insert path to output directory (ENTER to use current directory) >>")

def download(url:str, cookies:str, out_dir:str):
    if not(out_dir.endswith(os.path.sep)) and (len(out_dir) > 0):
        out_dir += os.path.sep

    output = out_dir + "%(title)s.%(ext)s"

    ydl_opts = {
        'cookiefile': cookies,
        'outtmpl' : output
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def read_arg_from_cli(arg_pos:int, check_fun, err_msg:str):
    if check_fun(sys.argv[arg_pos]):
        return sys.argv[arg_pos]
    else:
        print(err_msg)
        sys.exit(-1)

if __name__ == "__main__":
    input_urls = []
    cookies_path = ""
    out_dir = ""

    if (len(sys.argv) - 1 == 0):
        input_urls, cookies_path, out_dir = get_args_from_usr()
    else:
        parser = argparse.ArgumentParser(description='wrapper for youtube dl to easily "steal" lectures from my teachers\' GDrive',
                                         epilog='note that without any arguments the program will ask for them via stdin')

        COOKIES_ARG = "cookies"
        URLS_ARG = "urls"
        OUT_DIR_ARG = "out_dir"

        parser.add_argument(COOKIES_ARG, nargs=1, type=str, help="Path to cookies txt file")
        parser.add_argument(URLS_ARG, type=str, nargs="+", help="Url of each video to be downloaded")

        parser.add_argument("-o", "--"+OUT_DIR_ARG, nargs=1, default="", metavar="DIR",
                            type=str, help="directory to download the videos in")

        args = parser.parse_args()

        if not(check_cookies_file(vars(args)[COOKIES_ARG][0])):
            print("Cookies file is non existent or not a .txt file")
            sys.exit(-1)
        
        cookies_path = vars(args)[COOKIES_ARG][0]
        out_dir = vars(args)[OUT_DIR_ARG][0]
        
        input_urls = list(filter(lambda u: check_url(u, log=True), vars(args)[URLS_ARG]))

        if len(input_urls) == 0:
            print("No valid urls were provided")
            sys.exit(-1)
        
    for i in range(0, len(input_urls)):
        u = input_urls[i]

        print(f"################ Downloading video {i+1} of {len(input_urls)}\n")
        download(u, cookies_path, out_dir)
        print("\n")


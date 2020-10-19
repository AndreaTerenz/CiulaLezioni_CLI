import sys, os
import youtube_dl
import argparse
from urllib.parse import urlparse

COOKIES_ARG = "cookies"
URLS_LIST_ARG = "urls"
URLS_FILE_ARG = "urls_file"
OUT_DIR_ARG = "out_dir"

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

def parse_args_from_cli():
    parser = argparse.ArgumentParser(description='wrapper for youtube dl to easily "steal" lectures from my teachers\' GDrive',
                                     epilog='note that without any arguments the program will ask for them via stdin')

    main_grp = parser.add_argument_group()

    main_grp.add_argument("-o", "--"+OUT_DIR_ARG, nargs=1, default="", metavar="DIR",
                        type=str, help="directory to download the videos in")
    main_grp.add_argument("-c", "--"+COOKIES_ARG, required=True, nargs=1, type=str, help="Path to cookies txt file")

    group = main_grp.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--"+URLS_LIST_ARG, type=str, nargs="+", help="Url of each video to be downloaded")
    group.add_argument("-f", "--"+URLS_FILE_ARG, type=str, nargs=1, help="Path to txt file containing the urls of the video to download")

    args = vars(parser.parse_args())

    urls = None

    if (args[URLS_LIST_ARG] != None):    
        urls = list(args[URLS_LIST_ARG])
    elif (args[URLS_FILE_ARG] != None):
        try:
            with open(args[URLS_FILE_ARG][0], mode="r") as f:
                urls = f.readlines()
        except EnvironmentError:
            print("Failed to read urls from file")
            sys.exit(-1)
            
    return check_input_args(urls, args[COOKIES_ARG][0], args[OUT_DIR_ARG][0])

def check_input_args(urls:list, cookies:str, out_dir:str):
    if not(check_cookies_file(cookies)):
        print("Cookies file is non existent or not a .txt file")
        sys.exit(-1)

    urls = list(filter(lambda u: check_url(u, log=True), urls))

    if len(urls) == 0:
        print("No valid urls were provided")
        sys.exit(-1)

    if not(out_dir.endswith(os.path.sep)) and (len(out_dir) > 0):
        out_dir += os.path.sep

    return urls, cookies, out_dir

def download(url:str, cookies:str, out_dir:str):
    output = out_dir + "%(title)s.%(ext)s"

    ydl_opts = {
        'cookiefile': cookies,
        'outtmpl' : output
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    input_urls = []
    cookies_path = ""
    out_dir = ""

    input_urls, cookies_path, out_dir = parse_args_from_cli() if (len(sys.argv)-1 != 0) else get_args_from_usr()

    for i in range(0, len(input_urls)):
        u = input_urls[i]

        print(f"################ Downloading video {i+1} of {len(input_urls)}\n")
        download(u, cookies_path, out_dir)
        print("\n")


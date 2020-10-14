import sys, os
import youtube_dl
from urllib.parse import urlparse

def check_url(url:str):
    if (url.strip() != ""):
        res = urlparse(url)
        return (res.scheme != "" and res.netloc != "")

    return False

def check_cookies_file(f:str):
    if (f.strip() != ""):
        return f.endswith(".txt") and os.path.isfile(f)

    return False

def get_input_url():
    output = ""

    while not check_url(output):
        output = input("Input url >>")

        if not(check_url(output)):
            print("\tInvalid url - please try again")
    
    return output

def get_cookies_file():
    output = ""

    while not check_cookies_file(output):
        output = input("Path to cookies file >>")

        if not(check_cookies_file(output)):
            print("\tInvalid path - please try again")
    
    return output

def get_args_from_usr():
    return get_input_url(), get_cookies_file(), input("Insert path to output directory (ENTER to use current directory) >>")

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

def read_arg_from_cli(arg_pos:int, check_fun:function, err_msg:str):
    if check_fun(sys.argv[arg_pos]):
        return sys.argv[arg_pos]
    else:
        print(err_msg)
        sys.exit(-1)

if __name__ == "__main__":
    argc = len(sys.argv)-1

    if not(argc in (0, 2, 3)):
        print("Incorrect number of arguments - usage: ciulalezioni_cli.py [INPUT_URL PATH_TO_COOKIES [OUTPUT_DIRECTORY]]")
    else:
        input_url = ""
        cookies_path = ""
        out_dir = ""

        if (argc == 0):
            input_url, cookies_path, out_dir = get_args_from_usr()
        else:
            input_url = read_arg_from_cli(1, check_url, "Invalid input url")
            cookies_path = read_arg_from_cli(2, check_cookies_file, "Cookies file is non existent or not a .txt file")

            if argc == 3:
                out_dir = sys.argv[3]

        download(input_url, cookies_path, out_dir)


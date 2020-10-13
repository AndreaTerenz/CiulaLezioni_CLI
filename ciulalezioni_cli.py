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

if __name__ == "__main__":
    argc = len(sys.argv)-1

    if not(argc in (0, 2, 3)):
        print("Incorrect number of arguments - usage: ciulalezioni_cli.py [INPUT_URL PATH_TO_COOKIES [OUTPUT_DIRECTORY]]")
    else:
        input_url = ""
        cookies_path = ""
        out_dir = ""

        if (argc == 0):
            input_url = get_input_url()
            cookies_path = get_cookies_file()
            out_dir = input("Insert path to output directory (ENTER to use current directory) >>")
        else:
            if check_url(sys.argv[1]):
                input_url = sys.argv[1]
            else:
                print("Invalid input url")
                sys.exit(-1)

            if check_cookies_file(sys.argv[2]):
                cookies_path = sys.argv[2]
            else:
                print("Cookies file is non existent or not a .txt file")
                sys.exit(-1)

            if argc == 3:
                out_dir = sys.argv[3]

        if not(out_dir.endswith(os.path.sep)) and (len(out_dir) > 0):
            out_dir += os.path.sep

        output = out_dir + "%(title)s.%(ext)s"

        ydl_opts = {
            'cookiefile': cookies_path,
            'outtmpl' : output
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([input_url])



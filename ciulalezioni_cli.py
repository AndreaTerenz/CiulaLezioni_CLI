import sys, os
import youtube_dl

if __name__ == "__main__":
    argc = len(sys.argv)-1

    if not(argc in (0, 2, 3)):
        print("Incorrect number of arguments - usage: ciulalezioni_cli.py [INPUT_URL PATH_TO_COOKIES [OUTPUT_DIRECTORY]]")
    else:
        input_url = (sys.argv[1] if (argc != 0) else input("Input url >>"))
        cookies_path = (sys.argv[2] if (argc != 0) else input("Path to cookies file >>"))

        out_dir = ""

        if (argc == 0):
            out_dir = input("Insert path to output directory (ENTER to use current directory) >>")
        elif argc == 3:
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


        

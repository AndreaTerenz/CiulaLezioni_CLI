# CiulaLezioni_CLI

Like [CiulaLezioni](https://github.com/AndreaTerenz/CiulaLezioni), but it's from the command line

## Usage

From `ciulalezioni_cli.py -h`:

```
usage: ciulalezioni_cli.py [-h] [-o DIR] -c COOKIES (-l URL [URL ...] | -f URLS_FILE)

wrapper for youtube dl to easily "steal" lectures from my teachers' GDrive

optional arguments:
  -h, --help            show this help message and exit

  -o DIR, --out_dir DIR
                        directory to download the videos in
  -c COOKIES, --cookies COOKIES
                        Path to cookies txt file
  -l URL [URL ...], --urls_list URL [URL ...]
                        Url of each video to be downloaded
  -f URLS_FILE, --urls_file URLS_FILE
                        Path to txt file containing the videos' urls

note that without any arguments the program will ask for them via stdin
```

## Intalling required modules

`pip install youtube_dl`

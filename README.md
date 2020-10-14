# CiulaLezioni_CLI

Like [CiulaLezioni](https://github.com/AndreaTerenz/CiulaLezioni), but it's from the command line

## Usage

From `ciulalezioni_cli.py -h`:

```
usage: ciulalezioni_cli.py [-h] [-o DIR] cookies urls [urls ...]

wrapper for youtube dl to easily "steal" lectures from
my teachers' GDrive

positional arguments:
  cookies               Path to cookies txt file
  urls                  Url of each video to be
                        downloaded

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --out_dir DIR
                        directory to download the videos in

note that without any arguments the program will ask for
them via prompt
```

## Intalling required modules

`pip install youtube_dl`

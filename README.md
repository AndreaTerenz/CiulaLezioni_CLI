# CiulaLezioni_CLI

Like CiulaLezioni, but it's from the command line

## Usage

`ciulalezioni_cli.py [INPUT_URL PATH_TO_COOKIES [OUTPUT_DIRECTORY]]`

If no argument is specified, the program will prompt you to input the needed information

1. `python ciulalezioni_cli.py` to be prompted by the program to input the needed information
2. `python ciulalezioni_cli.py INPUT_URL PATH_TO_COOKIES`, where `INPUT_URL` is the URL of the video to download and `PATH_TO_COOKIES` is the path to a txt file containing the cookies (in Netscape format) of the webpage the video belongs to
3. `python ciulalezioni_cli.py INPUT_URL PATH_TO_COOKIES OUTPUT_DIRECTORY`, where `OUTPUT_DIRECTORY` specifies the directory in which to download the video

## Intalling required modules

`pip install youtube_dl`

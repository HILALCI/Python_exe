import sys
import re

"""
Not: URL eger uzun isie "url" tiknak veya cift tirnak icine alinmalidir. 

Ornek:

>>> python youtube.py https://www.youtube.com/watch?v=Ag1AKIl_2GM 9:40
>>> python youtube.py "https://www.youtube.com/watch?v=hy3sd9MOAcc&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=9" 1:41:27
"""


def kontrol(s):
    if re.search(r"^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$", s):
        if re.search(
            r"^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/.+$", sys.argv[1]
        ):
            convert(s)
        else:
            sys.exit("URL hatali girildi.")
    else:
        sys.exit("Sure degeri hatali girildi.")


def convert(sure):
    if sure.count(":") == 2:
        h, m, s = sure.split(":")
        sec = int(h) * 3600 + int(m) * 60 + int(s)

    elif sure.count(":") == 1:
        m, s = sure.split(":")
        sec = int(m) * 60 + int(s)

    elif sure.count(":") == 0:
        sec = int(sure)

    print("URL :", sys.argv[1] + "&t=" + str(sec))


if len(sys.argv) == 2:
    sys.exit("Sure degeri eksik girildi.")

elif len(sys.argv) == 3:
    kontrol(sys.argv[2])

else:
    sys.exit("Argumanlar eksik girildi.")

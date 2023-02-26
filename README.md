# telegram-sticker-downloader
Python scrypt that downloads all the stickers from a pack

Dependencies:
  python-telegram-bot (you can install it with 'pip install python-telegram-bot')

Help:
usage: main.py [-h] [-png] Packname

Download all the images from a Telegram sticker pack

positional arguments:
  Packname           Name of the Telegram pack to download. Provide the name as input (you can get it by clicking 'share stickers' on the pack in
                     Telegram). Example: if the link you get is https://t.me/addstickers/mypack, use just 'mypack' as input

options:
  -h, --help         show this help message and exit
  -png, --pngformat  Download the images as png instead of webp

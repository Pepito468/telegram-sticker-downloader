# telegram-sticker-downloader
Python scrypt that downloads all the stickers from a pack

Dependencies:
  python-telegram-bot (you can install it with 'pip install python-telegram-bot')

Before runnig the main.py you have to open 'TeleKey.py' and put there a bot API key (you can get one by messaging @botfather on telegram). This is because the scrypt needs an API key to request the images from Telegram.

Run:
python3 main.py [-h] [-png] Packname

Download all the images from a Telegram sticker pack

positional arguments:
  Packname           Name of the Telegram pack to download. Provide the name as input (you can get it by clicking 'share stickers' on the pack in
                     Telegram). Example: if the link you get is https://t.me/addstickers/mypack, use just 'mypack' as input

options:
  -h, --help         show this help message and exit
  -png, --pngformat  Download the images as png instead of webp

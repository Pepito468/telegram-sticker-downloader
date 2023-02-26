#libs
import os
import urllib.request
import argparse
import telegram
import asyncio
from TeleKey import key

#function
async def download_stickers(telepack, pngflag):
    bot = telegram.Bot(token=key)
    try:
        stickers = await bot.get_sticker_set(telepack)
    except telegram.error.BadRequest:
        print("The pack does not exist")
        return

    if not os.path.exists("Images"):
        os.makedirs("Images")

    # Download sticker images
    for sticker in stickers.stickers:
        file_id = sticker.file_id
        file = await bot.get_file(file_id)
        file_url = file.file_path
        file_extension = file_url.split(".")[-1]

        if not pngflag:
            urllib.request.urlretrieve(
                file_url, f"Images/{sticker.file_id}.{file_extension}"
            )
        else:
            urllib.request.urlretrieve(
                file_url, f"Images/{sticker.file_id}.png"
            )

    print("Done")
    
#Terminal arguments
command = argparse.ArgumentParser(description="Download all the images from a Telegram sticker pack")
command.add_argument("Packname", type=str ,help="Name of the Telegram pack to download.\nProvide the name as input (you can get it by clicking 'share stickers' on the pack in Telegram).\n Example: if the link you get is https://t.me/addstickers/mypack, use just 'mypack' as input") #must be provided
command.add_argument("-png", "--pngformat", action="store_true", help="Download the images as png instead of webp")

args = command.parse_args()

#run
asyncio.run(download_stickers(args.Packname, args.pngformat))

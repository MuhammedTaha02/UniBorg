"""
Usage: .sa
Author on Muhammed Taha
https://t.me/BU9TR4CK3R
"""

from telethon import events, functions, types

from time import sleep
from os import remove
from PIL import Image
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker
import asyncio
import io
import math
import urllib.request
from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time
from collections import deque
import requests
import os
import sys
import random
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="^.sa$", outgoing=True))

async def merkurkedissa(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 8)

    await event.edit("Selamün Aleyküm..")

    animation_chars = [
        
            "S",
            "SA",
            "S ve A",
            "Sa",
            "Selammm",
            "💥Naber?",
            "**🔥Selamün Aleyküm**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 8])

"""
Author on Muhammed Taha
https://t.me/BU9TR4CK3R
"""

from telethon import events

import asyncio



@borg.on(events.NewMessage(pattern=r"\.hack", outgoing=True))

async def port_hack(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 24)

    #input_str = event.pattern_match.group(1)

    await event.edit("`Hazırlık sürüyor...`")

    animation_chars = [
        
            "`Programlar hazır !`",
            "`İşlem başlatılıyor \n(0%) ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Sistem özellikleri alınıyor. \n(5%) █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Sistem özellikleri alınıyor.. \n(10%) ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Sistem özellikleri alınıyor... \n(15%) ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor. \n(20%) ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor.. \n(25%) █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor... \n(30%) ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor. \n(35%) ███████▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor.. \n(40%) ████████▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor... \n(45%) █████████▒▒▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor. \n(50%) ██████████▒▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor.. \n(55%) ███████████▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor... \n(60%) ████████████▒▒▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor. \n(65%) █████████████▒▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor.. \n(70%) ██████████████▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor... \n(75%) ███████████████▒▒▒▒▒`",
            "`Dosyalar yükleniyor. \n(80%) ████████████████▒▒▒▒`",
            "`Dosyalar yükleniyor.. \n(85%) █████████████████▒▒▒`",
            "`Dosyalar yükleniyor... \n(90%) ██████████████████▒▒`",
            "`Dosyalar yükleniyor. \n(95%) ███████████████████▒`",
            "`Temizleniyor.. \n(100%) ███████████████████`",
            "`İşlem Tamam... \n(100%) ███████████████████ `",
            "`Bilgisayar tarafımızca hacklendi.\nHack'i kaldırmak için 100$ ödeyin`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 24])

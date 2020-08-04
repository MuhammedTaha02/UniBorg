"""Purge your messages without the admins seeing it in Recent Actions"""
from telethon import events
import asyncio
from uniborg.util import admin_cmd
from asyncio import sleep
from telethon.errors import rpcbaseerrors


###@borg.on(admin_cmd(pattern="purge ?(.*)"))
###async def _(event):
###    if event.fwd_from:
###        return
###    if event.reply_to_msg_id:
###        i = 1
###        msgs = []
###        from_user = None
###        input_str = event.pattern_match.group(1)
###        if input_str:
###            from_user = await borg.get_entity(input_str)
###            logger.info(from_user)
###        async for message in borg.iter_messages(
###            event.chat_id,
###            min_id=event.reply_to_msg_id,
###            from_user=from_user
###        ):
###            i = i + 1
###            msgs.append(message)
###            if len(msgs) == 100:
###                await borg.delete_messages(event.chat_id, msgs, revoke=True)
###                msgs = []
###        if len(msgs) <= 100:
###            await borg.delete_messages(event.chat_id, msgs, revoke=True)
###            msgs = []
###            await event.delete()
###        else:
###            await event.edit("**PURGE** Failed!")


@borg.on(admin_cmd(pattern="^.purge$"))
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count = count + 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        await purg.edit("`Temizlemeye başlamak için bir mesaja ihtiyacım var.`")
        return

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, f"`Hızlı temizlik tamamlandı!`\
        \n{str(count)} tane mesaj silindi.")
    await sleep(2)
    await done.delete()

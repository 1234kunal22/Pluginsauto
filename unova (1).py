import sys
import os
import asyncio
from telethon import events

@hell_cmd(pattern="unova(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = int(event.pattern_match.group(1)) or 15
    await eod(event,"`Ok! Finding.....`")
    while True:
        await event.client.send_message(572621020,"/hunt")
        await asyncio.sleep(input_str)
      

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    if 'A wild Cobalion' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Virizion' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Victini' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Reshiram' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Kyurem' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Zekrom' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'Shiny pokemon found!' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
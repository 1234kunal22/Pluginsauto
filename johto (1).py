import sys
import os
import asyncio
from telethon import events

@hell_cmd(pattern="johto(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = int(event.pattern_match.group(1)) or 15
    await eod(event,"`Ok! Finding.....`")
    while True:
        await event.client.send_message(572621020,"/hunt")
        await asyncio.sleep(input_str)
      

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    if 'A wild Lugia' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Ho-Oh' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Suicune' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Raikou' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild entei' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'Shiny pokemon found!' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
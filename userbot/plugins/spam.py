# For UniBorg
# Thanks To Priyam Kalra
# Syntax (.spam <number of msgs> <text>)
#Ported To Xtra Bot MOD v2.0 By MrMobTech
from asyncio import wait
import asyncio
from telethon.tl import functions, types
from time import sleep


@client.on(events(pattern="spam ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = str(event.pattern_match.group(1))
    input_split = input.split()
    chat = event.chat_id
    try:
        count = str(input_split[0])
    except ValueError:
        await event.edit("Invalid Syntax!")
        return
    if input.startswith(count):
        strip = len(count)
        text = input[strip:]
    else:
        await event.edit("Fatal Error!")
        return
    if text and count != None:
        await event.delete()
        for spam in range(int(count)):
            await event.reply(text)
        msg = await event.reply(f"Task complete, spammed input text {count} times!")
        sleep(2)
        await msg.delete()
        status = f"SPAMMED\n```{text}```\n in ```{chat}``` ```{count}``` times."
        await log(status)
    else:
        await event.edit("Unexpected Error! Aborting..")
        return

async def log(text):
    LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
    await client.send_message(LOGGER, text)


HELPER.update({"spam": "\
**Available commands in spam module:**\
\n`.spam <text>`\
")}

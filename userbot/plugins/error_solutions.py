# Exclusive module for PhoeniX
#Ported To DeOXy
# By @Techy05
# You should use this module without proper credits
# Syntax (.solution <error_name>)
import asyncio
from telethon.tl import functions, types, ERROR, ERROR_LIST



@client.on(events(pattern="solution ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        err = event.pattern_match.group(1)
        if err:
            if err in ERROR:
                await event.edit(ERROR[err])
            else:
                await event.edit("No information for this error yet!\n**Tip: Get a list of all errors using .errors**")
        else:
            await event.edit("Please specify an error.\n**Tip: Get a list of all errors using .errors**")

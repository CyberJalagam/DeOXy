"""Emoji

Available Commands:

.wtf"""


import asyncio


@client.on(events(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        await event.edit(input_str)
        animation_chars = [
            "**Bruh**",
            "**Bruh __What__",
            "**Bruh** __What The__",
            "**Bruh** __What The F__",
            "**Bruh** __What The F ?!__"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])


HELPER.update({"wtf": "\
**Available commands in wtf module:**\
\n`.<text>`\
")}

#By X-tra-Telegram Modz Geng
#Developed By @TechyNewbie
#Module made for mocking Priyam.
#Sorry Priyam, Don't take it seriously XD
#Syntax .gei"""


import asyncio


@client.on(events(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 4)
    input_str = event.pattern_match.group(1)
    if input_str == "gei":
        await event.edit(input_str)
        animation_chars = [
            "**“It**",
            "**“It Is**",
            "**“It Is Gei”**",
            "**“It Is Gei”** __- Priyam Kalra__"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


HELPER.update({"gei": "\
**Available commands in gei module:**\
\n`.<text>`\
")}

# plugin by lejend @r4r4n4
"""Emoji

Available Commands:

.lucky"""


import asyncio





@client.on(events(pattern="lucky (.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 17)
    animation_chars = [
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",    
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/Dark-Princ3/X-tra-Telegram/)⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
            "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
            "⬜⬜\n⬜⬜",
            "[🎁](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy/)"
 ]
        for i in animation_ttl:
            await asyncio.sleep(0.5)
            await event.edit(animation_chars[i % 17])

HELPER.update({
    "lucky": f"\
**Requested Module --> Lucky**\
\n\nDetailed usage of fuction(s):\
\n\n```.lucky```\
\nUsage: Gifts DeOXy Repo :-0 .\
"
})            

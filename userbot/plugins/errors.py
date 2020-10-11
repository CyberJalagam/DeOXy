# Exclusive for PhoeniX
#Ported To DeOXy
# By @Techy05
# Credits --> @authoritydmc and Priyam Kalra
# You should not use this module without proper credits
# A dictionary of errors. With solutions ofc.
# Syntax (.errors)

import asyncio
from telethon.tl import functions, types
from global_variables_sql import ERROR_LIST


@client.on(events(pattern="errors ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    erros = "💫  **List of known errors in 𝔡𝓔𝐎𝕩𝕐 USERBOT **\n"
    ERROR_LIST.sort()
    prev = "1"
    num = 0
    for err in ERROR_LIST:
        num += 1
        if prev[0] != err[0]:
            erros += f"\n\t{err[0].upper()}\n"
        erros += f"-  ```{err}```\n"
        prev = err
    erros += f"\n\n__Number of solutions loaded:__ {num}\n**Tip:** Use .solution <error_name> for more info."
    await event.edit(erros)


HELPER.update({"errors": "\
**Available commands in errors module:**\
\n`.errors <text>`\
")}

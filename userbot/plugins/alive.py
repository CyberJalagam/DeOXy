"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname


DEFAULTUSER = Var.ALIVE_NAME if Var.ALIVE_NAME else f"[{(await client.get_me()).first_name}](tg://user?id={(await client.get_me()).id})"

@client.on(events(pattern="alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("•´¯``•.¸¸.•` 𝔡𝓔𝐎𝕩𝕐 `•.¸¸.•´´¯`•\n\n"
                     "👍🏻  `-̷-̷ Currently Alive! 🍻 -̷-̷` \n\n"
                     "__Telethon version: 6.9.0 // Python: 3.7.3\n\n__"
                     "**◆ ---------------- ✪ ----------------◆**\n"
                     "𝓑𝓸𝓽 𝓜𝓪𝓭𝓮 𝓑𝔂: [ᴊᴀɪꜱʜɴᴀᴠᴘʀᴀꜱᴀᴅ | #𝓣𝓱𝓮𝓣𝓮𝓬𝓱𝓖𝓪𝓷𝓰](t.me/CyberJalagam)\n"
                     f"ℱÃ𝐈𝕥н𝒻𝕦l𝕝𝔂 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑓𝑜𝑟: {DEFAULTUSER}\n"
                     "**◆ ---------------- ✪ ----------------◆**\n\n"
                     "                  ★彡 [GitHub](https://github.com/CyberJalagam/DeOXy) 彡★"
                     "                                                ")
HELPER.update({
    "alive": "\
**Requested Module --> alive**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.alive```\
\nUsage: Checks If Userbot Is Alive.\
"
})

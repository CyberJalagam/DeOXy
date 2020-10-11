from telethon import __version__

me = await client.get_me()
DEFAULTUSER = Var.ALIVE_NAME if Var.ALIVE_NAME else f"[{me.first_name}](tg://user?id={me.id})"

@client.on(events(pattern="alive"))
async def amireallyalive(alive):
    await alive.edit("•´¯``•.¸¸.•` 𝔡𝓔𝐎𝕩𝕐 `•.¸¸.•´´¯`•\n\n"
                     "👍🏻  `-̷-̷ Currently Alive! 🍻 -̷-̷` \n\n"
                     f"__Telethon version: {__version__} // Python: 3.7.3\n\n__"
                     "**◆ ---------------- ✪ ----------------◆**\n"
                     "𝓑𝓸𝓽 𝓜𝓪𝓭𝓮 𝓑𝔂: [ᴊᴀɪꜱʜɴᴀᴠᴘʀᴀꜱᴀᴅ | #𝓣𝓱𝓮𝓣𝓮𝓬𝓱𝓖𝓪𝓷𝓰](t.me/CyberJalagam)\n"
                     f"ℱÃ𝐈𝕥н𝒻𝕦l𝕝𝔂 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑓𝑜𝑟: {DEFAULTUSER}\n"
                     "**◆ ---------------- ✪ ----------------◆**\n\n"
                     "                  ★彡 [GitHub](https://github.com/CyberJalagam/DeOXy) 彡★")


HELPER.update({"alive": "\
**Requested Module --> alive**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.alive```\
\nUsage: Checks If Userbot Is Alive.\
"})

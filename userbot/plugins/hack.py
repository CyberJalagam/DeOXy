#Emoji

#Available Commands:

#.hackallph

#ANIMATION WRITTED BY @CyberJalagam
#OpenSource

from telethon import events
import asyncio

from uniborg.util import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST
from telethon.tl.functions.users import GetFullUserRequest

MODULE_LIST.append("hack")

SYNTAX.update({
    "hack": "\
**Requested Module --> Hack meme Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.hack```\
\nUsage: Memes a hack.\
\n\n```.gmailhack```\
\nUsage: hacks a person's mail.\
"
})        



@borg.on(admin_cmd(pattern=r"(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 26)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)
        
        animation_chars = [
            "`Connecting To DarkWeb.ONION...`",
            "`Successful!`",
            "`Connected 69.669.699.96`",
            "`Targetting Selected Message.`",
            "`Successfully Founded The Hash Of The Account`"
            "`Targeting PH: HackAll.onion`"
            "`Attempting method I... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method I FAILED!`",
            "`Attempting method II... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method II Does Not Exist!`",
            "`Attempting method III... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Disabling Account Security... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting Password... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Pulling Information... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 69%\n█████████████████▒▒▒▒▒▒▒▒ `",
            "`Hacking... 74%\n███████████████████▒▒▒▒▒▒▒ `",
            "`Hacking.... 80%\n█████████████████████▒▒▒▒ `",
            "`Adding Modules... 84%\n█████████████████████▒▒▒▒ `",
            "`Adding Finishing Touches... 96%\n████████████████████████▒`",
            "`HACKED 100%\n█████████████████████████ `",
            "`Targeted PH: All Accounts Hacked. ×_× Hacked Successfully...`\n__Targeted account is under Boss' control now__\n\n**Pay 50$ To** @CyberJalagam **Or Get Ready To See Your E-Mail and YouTube Channel Spamming Everywhere.**" 
       
        
        
        
        ]
             
         

        
        
        
        
        
        
        
     

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 26])
            
            
@borg.on(events.NewMessage(pattern=r"(.gmailhack)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "gmailhack":
        
        await event.edit(input_str)
        
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 767014786:
            await reply_message.reply("`Wait a second, This is my boss!`\n**How dare you threaten to hack my boss' google account stupid!**\n\n__Your account will be hacked in a few minutes! Pay 50$ to my Boss__ @CyberJalagam __OR delete your telegram account to prevent the virus getting into your Gmail account __😏")
        else:
            animation_chars = [
        
            "`Connecting To DarkWEB.ONION`",
            "`Connection Successful!`",
            "`Targetting` [{}](tg://user?id={})'s `Google Account.`".format(firstname, idd),
            "`Attempting method I... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method I FAILED!`",
            "`Attempting method II... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method II Out Of Order!`",
            "`Attempting method III... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Disabling Account Security... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting Password... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Pulling Information... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 69%\n█████████████████▒▒▒▒▒▒▒▒ `",
            "`Hacking... 74%\n███████████████████▒▒▒▒▒▒ `",
            "`Hacking.... 80%\n█████████████████████▒▒▒▒ `",
            "`Adding Modules... 86%\n██████████████████████▒▒▒ `",
            "`Adding Finishing Touches... 98%\n████████████████████████▒`",
            "`HACKED 100%\n█████████████████████████ `",
            "`Targeted Google Account Hacked Successfully...`\n[{}](tg://user?id={})'s __account is under Boss' control now__\n\n**Pay 50$ To** @CyberJalagam **Or Get Ready To See Your E-Mail and YouTube Channel Spamming Everywhere.**".format(firstname, idd)
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])            

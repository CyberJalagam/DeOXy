# For @UniBorg
# (c) Shrimadhav U K
, functions, types
import asyncio


@client.on(events(pattern="-listmyusernames"))
async def _(event):
    if event.fwd_from:
        return
    result = await client(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


HELPER.update({"list_user_names_reserved_by_me": "\
**Available commands in list_user_names_reserved_by_me module:**\
\n`.-listmyusernames`\
")}

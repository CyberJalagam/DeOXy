# For Uniclient
# (c) @INF1N17Y



@client.on(events(pattern="mention (.*)"))
async def _(event):
	if event.fwd_from:
		return	
	input_str = event.pattern_match.group(1)
	if event.reply_to_msg_id:
		previous_message = await event.get_reply_message()
		if previous_message.forward:
			replied_user = previous_message.forward.from_id
		else:
			replied_user = previous_message.from_id
	else:
		await event.edit("reply To Message")
	user_id = replied_user
	caption = """<a href='tg://user?id={}'>{}</a>""".format(user_id, input_str)
	await event.edit(caption, parse_mode="HTML")


HELPER.update({"mention": "\
**Available commands in mention module:**\
\n`.mention <text>`\
"})

"""CoronaVirus LookUp
Syntax: .covid <country>"""
from covid import Covid

@client.on(events(pattern="covid (.*)"))
async def _(event):
    covid = Covid()
    data = covid.get_data()
    country = event.pattern_match.group(1)
    country_data = get_country_data(country, data)
    output_text = "" 
    for name, value in country_data.items():
        output_text += "`{}`: `{}`\n".format(str(name), str(value))
    await event.edit("**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text))

def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return {"Status": "Use the first letter CAPITAL. Diden't Work?, No information yet about this country!"}


HELPER.update({"corona_virus": "\
**Available commands in corona_virus module:**\
\n`.covid <text>`\
"})

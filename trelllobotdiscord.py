import requests
import json
import discord
from discord.ext import commands
import time, threading


main_trello_endpoint = "https://api.trello.com/1/"
trello_key ="Ключ_Trello"
trello_token = "Токен_Trello"
application_list_id = "Айди_категории_Trello"
discordchannel = Айди_канала
discordtokenbot = 'Токен_DiscordBot'

new_card = ""
name = ""
shortlink = ""
fullName = ""
desccardtrello = ""


def create_trello_card(card_name, card_description):
	
	global name,shortlink,fullName,desccardtrello

	zaproscard = main_trello_endpoint+"lists/"+application_list_id+"/actions"
	jsonObj = {"key":trello_key,"token":trello_token,"name":card_name,"desc":card_description}
	new_card = requests.get(zaproscard, json=jsonObj)
	json_data = json.loads(new_card.text)
	
	name = json_data[0]["data"]["card"]["name"]
	shortlink = json_data[0]["data"]["card"]["shortLink"]
	fullName = json_data[0]["memberCreator"]["fullName"]
	idcardtrello = json_data[0]["data"]["card"]["id"]	
	
	zaproscard = main_trello_endpoint+"cards/"+idcardtrello
	jsonObj = {"key":trello_key,"token":trello_token,"name":card_name,"desc":card_description}
	new_card = requests.get(zaproscard, json=jsonObj)
	json_data = json.loads(new_card.text)
	
	desccardtrello = json_data["desc"]

bot = commands.Bot(command_prefix='?')

async def test():
    await bot.wait_until_ready()
    channel = bot.get_channel(discordchannel)
    await channel.send(f"🔥**Название:** {name}\n"
     			f"📄**Описание:** {desccardtrello}\n\n"
    			f"📧**Ссылка:** https://trello.com/c/{shortlink}\n"
     			f"🐗**Автор**: {fullName}\n"
				f":wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash:")

def foo():
	last_shortLink = shortlink
	create_trello_card("card_nametrst", "card_descriptiontest")
	threading.Timer(600, foo).start()
	if last_shortLink != shortlink:
		bot.loop.create_task(test())
foo()

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="github.com/BazZziliuS")
    await bot.change_presence(status=discord.Status.idle, activity=activity)


bot.run(discordtokenbot)


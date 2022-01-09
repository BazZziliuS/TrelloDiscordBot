import requests
import json
import discord
from discord.ext import commands
import time, threading


main_trello_endpoint = "https://api.trello.com/1/"
trello_key ="Ключ_Trello"
trello_token = "Токен_Trello"
boardnumber = "Айди_Борда_Trello"
application_list_id = "Айди_категории_Trello"
discordchannel = Айди_канала_для_категории
discordchannel2 = Айди_канала_для_борда
discordtokenbot = 'Токен_DiscordBot'

new_card = ""
name = ""
shortlink = ""
fullName = ""
desccardtrello = ""
nameq = ""
descq = ""
shortlinkq = ""
namelistq = ""
fullnameq = ""
desccardtrelloq = ""
idcardtrelloq = ""

def trellonewcard():
	
	global name,shortlink,fullName,desccardtrello

	zaproscard = main_trello_endpoint+"lists/"+application_list_id+"/actions"
	jsonObj = {"key":trello_key,"token":trello_token}
	new_card = requests.get(zaproscard, json=jsonObj)
	json_data = json.loads(new_card.text)
	
	name = json_data[0]["data"]["card"]["name"]
	shortlink = json_data[0]["data"]["card"]["shortLink"]
	fullName = json_data[0]["memberCreator"]["fullName"]
	idcardtrello = json_data[0]["data"]["card"]["id"]	
	
	zaproscard = main_trello_endpoint+"cards/"+idcardtrello
	jsonObj = {"key":trello_key,"token":trello_token}
	new_card = requests.get(zaproscard, json=jsonObj)
	json_data = json.loads(new_card.text)
	
	desccardtrello = json_data["desc"]

def trelloallcard():

	global nameq,descq,shortlinkq,namelistq,fullnameq,idcardtrelloq,desccardtrelloq

	zaproscardd = main_trello_endpoint+"boards/"+boardnumber+"/actions"
	jsonObj = {"key":trello_key,"token":trello_token}
	new_cardd = requests.get(zaproscardd, json=jsonObj)
	json_data = json.loads(new_cardd.text)

	nameq = json_data[0]["data"]["card"]["name"]
	shortlinkq = json_data[0]["data"]["card"]["shortLink"]
	namelistq = json_data[0]["data"]["list"]["name"]
	fullnameq = json_data[0]["memberCreator"]["fullName"]
	idcardtrelloq = json_data[0]["data"]["card"]["id"]	
	
	zaproscard = main_trello_endpoint+"card/"+idcardtrelloq
	jsonObj = {"key":trello_key,"token":trello_token}
	new_cardd = requests.get(zaproscard, json=jsonObj)
	json_dataq = json.loads(new_cardd.text)
	
	desccardtrelloq = json_dataq["desc"]



bot = commands.Bot(command_prefix='?')

async def test():
    await bot.wait_until_ready()
    channel = bot.get_channel(discordchannel)
    await channel.send(f"🔥**Название:** {name}\n"
     			f"📄**Описание:** {desccardtrello}\n\n"
    			f"📧**Ссылка:** https://trello.com/c/{shortlink}\n"
     			f"🐗**Автор**: {fullName}\n"
				f":wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash:")
    

async def tests():
    await bot.wait_until_ready()
    channelq = bot.get_channel(discordchannel2)
    await channelq.send(f"📊**Доска**: {namelistq}\n"
    			f"🔥**Название:** {nameq}\n"
     			f"📄**Описание:** {desccardtrelloq}\n"
    			f"📧**Ссылка:** https://trello.com/c/{shortlinkq}\n"
     			f"🐗**Автор**: {fullnameq}\n"
				f":wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash:")



def foo():
	last_shortLink = shortlink
	trellonewcard()
	threading.Timer(600, foo).start()
	if last_shortLink != shortlink:
		bot.loop.create_task(test())
foo()



def food():
	last_shortLinkq = shortlinkq
	trelloallcard()
	threading.Timer(150, food).start()
	if last_shortLinkq != shortlinkq:
		bot.loop.create_task(tests())
food()



bot.run(discordtokenbot)


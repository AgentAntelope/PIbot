import time
import random
from pibot_constants import *

name="greeting"
description="Greets users who arrive in chat."
version="1.0.0.2"

oldfag=[]
newfag=[]

#initialize oldfag and newfag
def init(bot):
	global oldfag,newfag
	file=open(www+"data/oldgreet.txt","r")
	oldfag=file.read().split('\n')
	file.close()
	file=open(www+"data/newgreet.txt","r")
	newfag=file.read().split('\n')
	file.close()
	file=open(www+"data/greetings.txt","r")
	string=file.read()
	file.close()
	greetings=string.replace('\r','').split('\n')
	random.seed()
	out=random.choice(greetings)
	bot.chat.send(out)

def format_greet(text,username):
	text=text.replace("<user>",username).replace("<USER>",username.upper())
	if "<time>" in text:
		t=time.localtime()
		if t.tm_hour>=5 and t.tm_hour<10:
			text.replace("<time>","morning")
		elif t.tm_hour>=10 and t.tm_hour<=12:
			text.replace("<time>","day")
		elif t.tm_hour>12 and t.tm_hour<=5:
			text.replace("<time>","afternoon")
		elif t.tm_hour>5 and t.tm_hour<8:
			text.replace("<time>","evening")
		elif t.tm_hour>=8 or t.tm_hour<5:
			text.replace("<time>","night")
	return text

def infunc(bot,text):
	global oldfag,newfag
	if text["Type"]=="Announcement":
		#check if this is the string
		if text["Msg"]=="has joined the channel":
			return format_greet(random.choice(oldfag),text["User"])
		elif text["Msg"]=="just joined the site":
			return format_greet(random.choice(newfag),text["User"])
		elif text["Msg"]=="has left the channel":
			return ""
		else:
			return 'Error: Unexpected announcement "'+text["Msg"]+'" received.'
	else:
		return ""

def outfunc(bot,ostream):
	return None

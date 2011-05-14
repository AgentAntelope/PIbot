import time

name="greeting"
description="Greets users who arrive in chat."
version="1.1.0"

oldfag=[]
newfag=[]

#initialize oldfag and newfag
file=open("/data/oldgreet.txt","r")
string=file.read()
oldfag=string.split('\n')
file.close()
file=open("/data/newgreet.txt","r")
string=file.read()
newfag=string.split('\n')
file.close()
del file
del string

file=open("../data/oldgreet.txt","r")
string=file.read()
oldfag=string.split('\n')
file.close()
file.open("../data/newgreet.txt","r")
string=file.read()
newfag=string.split('\n')
file.close()

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

def func(bot,text):
	if text["Type"]=="Announcement":
		#check if this is the string
		if text["Msg"]=="has joined chat":
			return format_greet(oldfag[randint(0,len(oldfag))])
		elif text["Msg"]=="has joined the site":
			return format_greet(newfag[randint(0,len(newfag))])
		else:
			return 'Error: Unexpected announcement "'+text["Msg"]+'" received.'
	else:
		return ""
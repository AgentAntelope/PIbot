from pibot_constants import *

name="services"
parameters="[service]"
description="Gives a list of all services and their status."
version="1.0.0"
level=user.basic

def format_status(cmd):
	string=cmd.name
	if cmd.disabled:
		string+=": disabled."
	return string+'\n'

def func(bot,text,args):
	if len(args)==0:
		string=""
		for s in bot.services:
			string+=format_status(s)
		return string[:-1]
	elif len(args)==1:
		service=0
		for s in bot.services:
			if s.name.lower()==args[0].lower():
				service=s
		if type(service)==type(bot.services[0]):
			return format_status(service)[:-1]
		else:
			return '"'+args[0]+'" is not a PIbot command.'
	else:
		return "Proper usage: "+CK+name+' '+parameters+' - '+description
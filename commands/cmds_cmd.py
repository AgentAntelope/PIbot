from pibot_constants import *

name="commands"
parameters="[command]"
description="Gives a list of all commands and their status."
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
		for c in bot.commands:
			string+=format_status(c)
		return string[:-1]
	elif len(args)==1:
		cmd=0
		for c in bot.commands:
			if c.name.lower()==args[0].lower():
				cmd=c
		if type(cmd)==type(bot.commands[0]):
			return format_status(cmd)[:-1]
		else:
			return '"'+args[0]+'" is not a PIbot command.'
	else:
		return "Proper usage: "+CK+name+' '+parameters+' - '+description
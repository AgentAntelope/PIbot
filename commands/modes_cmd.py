from pibot_constants import *

name="modes"
parameters="[mode]"
description="Gives a list of all modes and their status."
version="1.0.0"
level=user.basic

def format_status(m:
	string=m.name+':'
	if m.disabled:
		string+=" disabled and"
	if m.status:
		string+=" on."
	else:
		string+=" off."
	return string+'\n'

def func(bot,text,args):
	if len(args)==0:
		string=""
		for m in bot.modes:
			string+=format_status(m)
		return string[:-1]
	elif len(args)==1:
		mode=0
		for m in bot.modes:
			if m.name.lower()==args[0].lower():
				mode=m
		if type(mode)==type(bot.modes[0]):
			return format_status(m)[:-1]
		else:
			return '"'+args[0]+'" is not a PIbot mode.'
	else:
		return "Proper usage: "+CK+name+' '+parameters+' - '+description
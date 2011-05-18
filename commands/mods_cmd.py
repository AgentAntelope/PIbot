from pibot_constants import *

name="mods"
parameters=""
description="Returns a list of PIbot mods."
version="1.0.1.0"
level=user.basic

def func(bot,text,args):
	if len(args)>0:
		return "Proper usage: "+CK+name
	string="Mods:\n"
	print bot.mods
	for mod in bot.mods:
		string+=mod+'\n'
	print string
	return string[:-1]

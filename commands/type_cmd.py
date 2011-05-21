from pibot_constants import *

name="type"
parameters="<module>"
description="Returns the type of module of module."
version="1.0.0.0"
level=user.basic

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	for c in bot.commands:
		if args[0].lower()==c.name:
			return '"'+args[0]+'" is a command.'
	for m in bot.modes:
		if args[0].lower()==m.name:
			return '"'+args[0]+'" is a mode.'
	for s in bot.services:
		if args[0].lower()==s.name:
			return '"'+args[0]+'" is a service.'
	#doesn't exist
	return '"'+args[0]+'" is not a PIbot module.'

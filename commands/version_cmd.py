from pibot_constants import *

name="version"
parameters="[module]"
description="Returns the version of module or of PIbot."
level=user.basic
version="1.0.0.1"

def func(bot,text,args):
	if len(args)==0:
		return 'PIbot v'+str(bot.version)
	if len(args)==1:
		for c in bot.commands:
			if c.name==args[0]:
				return 'v'+str(c.version)
		for m in bot.modes:
			if m.name==args[0]:
				return 'v'+str(m.version)
		for s in bot.modes:
			if s.name==args[0]:
				return 'v'+str(s.version)
		return '"'+args[0]+'" is not a PIbot module.'
	return "Proper usage: "+CK+name+' '+parameters

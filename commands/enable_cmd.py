from pibot_constants import *

name="enable"
parameters="<module>"
description="Enables a PIbot module."
version="1.0.1.2"
level=user.mod

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	for c in bot.commands:
		if c.name==args[0].lower():
			if bot.userlvl(text["User"])>c.level:
				if not c.disabled:
					return '"'+CK+c.name+'" is not disabled.'
				c.disabled=False
				return '"'+CK+c.name+'" has been disabled.'
			else:
				return '"'+CK+c.name+'" is a '+userlvlname(c.level)+"-only command."
	for m in bot.modes:
		if m.name==args[0].lower():
			if bot.userlvl(text["User"])>m.level:
				if not m.disabled:
					return '"'+m.name+'" mode is not disabled.'
				m.disabled=False
				return '"'+m.name+'" mode has been disabled.'
			else:
				return '"'+m.name+'" is a '+userlvlname(m.level)+"-only mode."
	for s in bot.services:
		if s.name==args[0].lower():
			if not s.disabled:
				return '"'+s.name+'" service is not disabled.'
			s.disabled=False
			return '"'+s.name+'" service has been disabled.'
	return '"'+args[0]+'" is not a PIbot module.'

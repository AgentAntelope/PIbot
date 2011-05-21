from pibot_constants import *

name="disable"
parameters="<module>"
description="Disables a PIbot module."
version="1.0.1.2"
level=user.mod

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	for c in bot.commands:
		if c.name==args[0].lower():
			if bot.userlvl(text["User"])>c.level:
				if c.disabled:
					return '"'+CK+c.name+'" is already disabled.'
				c.disabled=True
				return '"'+CK+c.name+'" has been disabled.'
			else:
				return '"'+CK+c.name+'" is a '+userlvlname(c.level)+"-only command."
	for m in bot.modes:
		if m.name==args[0].lower():
			if bot.userlvl(text["User"])>m.level:
				if m.disabled:
					return '"'+m.name+'" mode is already disabled.'
				m.disabled=True
				return '"'+m.name+'" mode has been disabled.'
			else:
				return '"'+m.name+'" is a '+userlvlname(m.level)+"-only mode."
	for s in bot.services:
		if s.name==args[0].lower():
			if s.disabled:
				return '"'+s.name+'" service is already disabled.'
			s.disabled=True
			return '"'+s.name+'" service has been disabled.'
	return '"'+args[0]+'" is not a PIbot module.'

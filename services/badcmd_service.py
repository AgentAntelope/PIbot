from pibot_constants import *

name="badcommand"
description="Alerts users if a command is invalid."
version="1.0.0"

def infunc(bot,text):
	args=text["Msg"].split(' ')
	if args[0][0]=='!' and len(args[0])>1:
		for c in bot.commands:
			if CK+c.name.lower()==args[0].lower():
				return ""
		return '"'+args[0]+'" is not a PIbot command.'
	return ""

def outfunc(ostream):
	return None

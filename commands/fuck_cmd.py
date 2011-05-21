from pibot_constants import *

name="fuck"
parameters="<\"off\">"
description="Makes PIbot fuck off."
version="1.0.1.0"
level=user.basic

def func(bot,text,args):
	if len(args)==1:
		if args[0].lower()=="off":
			return "/me fucks off"
	return ""

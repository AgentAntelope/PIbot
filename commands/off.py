from pibot_constants import *

name="off"
parameters="<mode>"
description="Turn off a PIbot mode."
level=user.basic
version="1.0.0.0"

def func(bot,text,args):
	if len(args)==0 or len(args)>1:
		return "Proper usage: "+CK+name+' '+parameters
	elif len(args)==1:
		for m in bot.modes:
			if m.name==args[0]:
				return m.off()
		return '"'+args[0]+'" is not a PIbot command.'

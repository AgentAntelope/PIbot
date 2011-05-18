from pibot_constants import *

name="toggle"
parameters="<mode>"
description="Toggle a PIbot mode."
level=user.basic
version="1.0.1.1"

def func(bot,text,args):
	if len(args)==0 or len(args)>1:
		return "Proper usage: "+CK+name+' '+parameters
	elif len(args)==1:
		found=False
		for m in bot.modes:
			if m.name==args[0]:
				found=True
				break
		if found:
			if bot.userlvl(text["User"])>=m.level:
				return m.toggle()
			else:
				return '"'+args[0]+'" is a '+userlvlname(m.level)+'-only mode.'
		else:
			return '"'+args[0]+'" is not a PIbot mode.'

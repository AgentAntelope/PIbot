import codecs
from pibot_constants import *

name="dltmod"
parameters="<user>"
description="Delete a PIbot mod."
version="1.0.0.0"
level=user.admin

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	if args[0].lower() in bot.mods:
		bot.mods.remove(args[0].lower())
		mods=codecs.open(www+"data/mods.txt","w","utf-8")
		for m in bot.mods:
			mods.write(m+'\n')
		mods.close()
		return '"'+args[0]+'" has been removed as a PIbot mod.'
	else:
		return '"'+args[0]+'" is not a PIbot mod.'

import codecs
from pibot_constants import *

name="addmod"
parameters="<user>"
description="Add a PIbot moderator."
version="1.0.0.0"
level=user.mod

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	bot.mods.append(args[0].lower())
	mods=codecs.open(www+"data/mods.txt","a","utf-8")
	mods.write(args[0].lower()+'\n')
	mods.close()
	return '"'+args[0]+'" has been added as a PIbot mod.'

import codecs
from pibot_constants import *

name="ban"
parameters="<user>"
description="Ban a user from all PIbot use."
version="1.0.1.2"
level=user.mod

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	if bot.userlvl(text["User"])>bot.userlvl(args[0]):
		if args[0] not in bot.banned:
			bot.banned.append(args[0].lower())
			banned=codecs.open(www+"data/banned.txt","a","utf-8")
			banned.write(args[0].lower()+'\n')
			banned.close()
			return '"'+args[0]+'" has been banned from PIbot use.'
		else:
			return '"'+args[0]+'" is already banned.'

import codecs
from pibot_constants import *

name="unban"
parameters="<user>"
description="Unban user from PIbot use."
version="1.0.1.1"
level=user.mod

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	if args[0].lower() in bot.banned:
		bot.banned.remove(args[0].lower())
		banned=codecs.open(www+"data/ban.txt","w","utf-8")
		for b in bot.banned:
			banned.write(b+'\n')
		banned.close()
		return '"'+args[0]+'" is no longer banned from PIbot use.'
	else:
		return '"'+args[0]+'" is not banned.'

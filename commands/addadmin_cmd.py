import codecs
from pibot_constants import *

name="addadmin"
parameters="<user>"
description="Add a PIbot admin."
version="1.0.0.0"
level=user.admin

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	if args[0].lower() not in bot.admins:
		bot.admins.append(args[0].lower())
		admins=codecs.open(www+"data/admins.txt","a","utf-8")
		admins.write(args[0].lower()+'\n')
		admins.close()
		return '"'+args[0]+'" has been added as a PIbot admin.'
	return '"'+args[0]+'" is already a PIbot admin.'

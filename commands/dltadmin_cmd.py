import codecs
from pibot_constants import *

name="dltadmin"
parameters="<user>"
description="Delete a PIbot admin."
version="1.0.0.0"
level=user.host

def func(bot,text,args):
	if len(args)!=1:
		return "Proper usage: "+CK+name+' '+parameters
	if args[0].lower() in bot.admins:
		bot.admins.remove(args[0].lower())
		admins=codecs.open(www+"data/admins.txt","w","utf-8")
		for a in bot.admins:
			admins.write(a+'\n')
		admins.close()
		return '"'+args[0]+'" has been removed as a PIbot admin.'
	else:
		return '"'+args[0]+'" is not a PIbot admin.'

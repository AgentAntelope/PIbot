from pibot_constants import *

name="logout"
parameters=""
description="Make PIbot log out."
version="1.1.0"
level=user.admin

def func(bot,text,args):
	if len(args)>0:
		return "Proper usage: "+CK+name+' '+parameters
	bot.dologout=True
	return "Goodbye"

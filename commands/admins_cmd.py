from pibot_constants import *

name="admins"
parameters=""
description="Returns a list of PIbot admins."
version="1.0.1.0"
level=user.basic

def func(bot,text,args):
	if len(args)>0:
		return "Proper usage: "+CK+name
	string="Admins:\n"
	for admin in bot.admins:
		string+=admin+'\n'
	return string[:-1]

from pibot_constants import *

name="say"
parameters="<text>"
description="Make PIbot say text"
level=user.basic
version="1.0.0"

def combine(list):
	string=""
	for s in list:
		string+=s+' '
	return s[:-1]

def func(bot,text,args):
	if len(args)==0:
		return "Proper usage: "+CK+name+' '+parameters
	if args[0][0]=='/'
		if args[0].lower()!="/me":
			if text["User"].lower()!=bot.host.lower():
				return "I will not say that, "+text["User"]+'.'
	return combine(args)
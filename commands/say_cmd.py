from pibot_constants import *

name="say"
parameters="<text>"
description="Make PIbot say text"
level=user.basic
version="1.0.1.1"

def combine(params):
	string=""
	for s in params:
		string+=s+' '
	return string[:-1]

def func(bot,text,args):
	if len(args)==0:
		return "Proper usage: "+CK+name+' '+parameters
	if args[0][0]=='/':
		if args[0].lower()!="/me":
			if text["User"].lower()!=host.lower():
				return "I will not say that, "+text["User"]+'.'
	return combine(args).replace('\\n','\n').split('||')

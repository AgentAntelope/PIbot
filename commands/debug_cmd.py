from pibot_constants import *

name="debug"
parameters="<expression>"
description="Execute Python code while PIbot is running."
version="1.0.1.1"
level=user.host

def func(bot,text,args):
	if len(args)==0:
		return "Proper usage: "+CK+name+' '+parameters
	#recombine args
	expr=""
	for a in args:
		expr+=a+' '
	try:
		return eval(expr)
	except Exception as detail:
		print detail
		return "An error has occurred. Please view the console for more info."
	#should be handled by now, but just in case
	return ""

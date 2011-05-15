from pibot_constants import *

name="shout"
parameters="[on/off]"
description="All output is capitalized"
version="1.1.0"
level=user.basic

def func(bot,text):
	return text.upper()

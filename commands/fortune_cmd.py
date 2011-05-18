import random
import codecs
from pibot_constants import *

name="fortune"
parameters="[fortune]"
description="Either adds or returns a fortune."
version="1.0.2.0"
level=user.basic

fortunes=[]

def init(bot):
	global fortunes
	ffile=open(www+"data/fortunes.txt","r")
	string=ffile.read()
	string.replace('\r','')
	fortunes=string.split('\n')

def func(bot,text,args):
	global fortunes
	if len(args)==0:
		return random.choice(fortunes)
	string=""
	for a in args:
		string+=a+' '
	string=string[:-1]
	ffile=codecs.open(www+"data/fortunes.txt","a","utf-8")
	ffile.write('\n"'+string+'" ~ '+text["User"])
	ffile.close()
	fortunes.append('"'+string+'" ~ '+text["User"])
	return "Fortune has been added."

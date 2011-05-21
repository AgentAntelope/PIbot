import random
import codecs
from pibot_constants import *

name="fiskie"
description="Makes PIbot say random vulgar phrases."
version="1.0.1.2"
level=user.basic

phrases=[]

def init(bot):
	global phrases
	ffile=codecs.open(www+"data/fiskie.txt","r","utf-8")
	string=ffile.read()
	ffile.close()
	string.replace('\r','')
	phrases=string.split('\n')

def func(bot,text):
	global phrases
	words=text.split(' ')
	if len(words)>1:
		words.insert(random.randrange(1,len(words)),random.choice(phrases))
		string=""
		for w in words:
			string+=w+' '
		return string[:-1]
	return text

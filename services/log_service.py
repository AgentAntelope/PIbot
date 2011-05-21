import time
import codecs
from pibot_constants import *

name="log"
description="Records all conversation that goes on in chat."
version="1.0.1.5"

#init logging
def init(bot):
	file=codecs.open(www+"data/log.txt","a","utf-8")
	file.write('i\t\t\t'+time.strftime("%I:%M")+'\n')
	file.close()

def isemote(text):
	args=text.split(' ')
	if len(args)==0:
		if args[0][0]=='/':
			if args[0].lower()=="/me":
				return True
	return False

def func(bot,text):
	file=codecs.open(www+"data/log.txt","a","utf-8")
	if text["Type"]=="Message":
		file.write('m')
	elif text["Type"]=="Emote":
		file.write('e')
	elif text["Type"]=="Announcement":
		file.write('a')
	else:
		file.write('x')
	file.write('\t')
	file.write(unicode(text["User"]+u'\t'))
	file.write(unicode(text["Msg"]+u'\t'))
	#guaranteed to always be ascii-compatible
	file.write(text["Timestamp"]+'\n')
	return ""

def infunc(bot,text):
	if text["Type"]=="Message":
		print "<"+text["User"]+"> "+text["Msg"]+' '+text["Timestamp"]
	elif text["Type"]=="Announcement":
		print "-="+text["User"]+' '+text["Msg"]+"=-"+text["Timestamp"]
	else:
		print "***"+text["User"]+' '+text["Msg"]+' '+text["Timestamp"]
	return func(bot,text)

def outfunc(bot,ostream):
	text={"User":bot.username,"Msg":ostream,"Timestamp":time.strftime("%I:%M"),"Type":"Message"}
	if isemote(ostream):
		text["Type"]="Emote"
	else:
		text["Type"]="Message"
	func(bot,text)
	return None

import time

name="log"
description="Records all conversation that goes on in chat."
version="1.1.0"

#init logging
file=open("../data/log.txt","a")
file.write('i\t\t\t'+time.strftime("%I:%M"))
file.close()

def func(bot,text):
	file=open("../data/log.txt","a")
	if text["Type"]=="Msg":
		file.write('m')
	elif text["Type"]=="Emote":
		file.write('e')
	elif text["Type"]=="Announcement":
		file.write('a')
	else:
		file.write('x')
	file.write('\t')
	file.write(text["User"]+'\t')
	file.write(text["Msg"]+'\t')
	file.write(text["Timestamp"])
	return ""
import sys
import os
import time
from pibot_classes import bot,command,mode,service
from pibot_constants import *

def main():
	trigger=open(www+"data/trigger.tmp","w")
	trigger.close()
	sys.path.append(workingdir+"commands/")
	sys.path.append(workingdir+"modes/")
	sys.path.append(workingdir+"services/")
	password=open("/home/pimaster/password.txt","r")
	pibot=bot("PIbot",password.read().replace('\n',''),"2.0.1.0","")
	pibot.loadmodules(workingdir+"commands/",workingdir+"modes/",workingdir+"services/")
	pibot.initmodules()
	#run the bot
	while not pibot.dologout:
		pibot.run()
		time.sleep(delay)
	pibot.logout()
	os.remove(www+"data/trigger.tmp")
	return 0

if __name__=="__main__":
	main()

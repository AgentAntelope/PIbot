import sys
import os
import time
from pibot_classes import bot,command,mode,service
from pibot_constants import *

def main():
	sys.path.append(workingdir+"commands/")
	sys.path.append(workingdir+"modes/")
	sys.path.append(workingdir+"services/")
	password=open("/home/pimaster/password.txt","r")
	pibot=bot("PIbot",password.read().replace('\n',''),"2.2.1.5","")
	pibot.loadmodules(workingdir+"commands/",workingdir+"modes/",workingdir+"services/")
	pibot.initmodules()
	#run the bot
	while not pibot.dologout:
		pibot.run()
		time.sleep(delay)
	pibot.logout()
	return 0

if __name__=="__main__":
	main()

import sys
import time
import os
from pibot_classes import bot,command,mode,service
from pibot_constants import *

def loadmodules(bot,cmddir,modedir,servdir):
	#load commands
	listing=os.listdir(cmddir)
	for f in listing:
		path=os.path.splitext(f)
		if path[1]==".py":
			bot.addcmd(command(os.path.basename(path[0]),bot))
	#load modes
	listing=os.listdir(modedir)
	for f in listing:
		path=os.path.splitext(f)
		if path[1]==".py":
			bot.addmode(mode(os.path.basename(path[0]),bot))
	#load services
	listing=os.listdir(servdir)
	for f in listing:
		path=os.path.splitext(f)
		if path[1]==".py":
			bot.addservice(service(os.path.basename(path[0]),bot))

def main():
	sys.path.append(workingdir+"commands/")
	sys.path.append(workingdir+"modes/")
	sys.path.append(workingdir+"services/")
	password=open("/home/pimaster/password.txt","r")
	pibot=bot("PIbot",password.read().replace('\n',''),"2.0.0.1","")
	loadmodules(pibot,workingdir+"commands/",workingdir+"modes/",workingdir+"services/")
	#run the bot
	while not pibot.dologout:
		pibot.run()
		time.sleep(delay)
	pibot.logout()

if __name__=="__main__":
	main()

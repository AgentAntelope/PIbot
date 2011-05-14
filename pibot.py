from pibot_classes import bot

def main():
	file=open("..\password.txt","r")
	pibot=bot("PIbot",password.read(),"2.0.0","")
	#commands
	pibot.addcmd(command("/commands/cmds_cmd.py"))
	pibot.addcmd(command("/commands/modes_cmd.py"))
	pibot.addcmd(command("/commands/services_cmd.py"))
	pibot.addcmd(command("/commands/say_cmd.py"))
	#modes
	pibot.addmode(mode("/modes/quiet_mode.py"))
	#services
	pibot.addservice(service("/services/greet_service.py"))
	pibot.addservice(service("/services/log_service.py"))
	#run the bot
	while not pibot.logout:
		pibot.run()

if __name__=="__main__":
	main()
import u413lib
from pibot_constants import *

class module:
	#default values
		name=""
		type=""
		description=""
		version=""
		func=0
		disabled=False
	def __init__(self,name,description,version,func,disable=False):
		self.name=name
		self.description=description
		self.version=version
		self.func=func
		self.disable=disable
	def enable(self):
		if not self.disabled:
			return self.name+" "+self.type+" is not disabled."
		self.disabled=False
		return self.name+" "+self.type+" is now enabled."
	def disable(self):
		if self.disabled:
			return self.name+" "+self.type+" is already disabled."
		self.disabled=True
		return self.name+" "+self.type+" is now disabled."

class command(module):
	#default values
		parameters=""
		level=user.basic
		type="command"
	def __init__(self,filename):
		mod=__import__(filename)
		self.name=mod.name
		self.parameters=mod.parameters
		self.description=mod.description
		self.level=mod.level
		self.version=mod.version
		self.func=mod.func
	def __init__(self,name,parameters,description,version,func,level,disable=False):
		self.parameters=parameters
		self.level=level
		super(command,self).__init___(name,description,version,func,disable)
	def run(self,bot,text,args):
		if self.disable:
			return self.name+' '+self.type+" is disabled."
		return self.func(bot,text,args)

class service(module):
	#default values
		type="service"
	def __init__(self,filename):
		mod=__import__(filename)
		name=mod.name
		description=mod.description
		version=mod.version
		func=mod.func
	def __init__(self,name,description,version,func)
		super(command,self).__init___(name,description,version,func,disable)
	def run(self,bot,text):
		if self.disable:
			return self.name+' '+self.type+" is disabled."
		return self.func(bot,text)

class mode(module):
	#default values
		level=user.basic
		state=False
	def on(self):
		if self.state:
			return self.name+" mode is already on."
		self.state=True
		return self.name+" mode is now on."
	def off(self):
		if not self.state:
			return self.name+" mode is already off."
		self.state=False
		return self.name+" mode is now off."
	def toggle(self):
		if self.state:
			self.state=False
			return self.name+" mode is now off."
		self.state=True
		return self.name+" mode is now on."
	def __init__(self,filename):
		mod=__import__(filename)
		name=mod.name
		description=mod.description
		version=mod.version
		func=mod.func
		level=mod.level
	def __init__(self,name,parameters,description,version,func,level,state=False,disable=False):
		self.parameters=parameters
		self.level=level
		self.state=state
		super(command,self).__init___(name,description,version,func,disable)
	def run(self,bot,text):
		if self.disable:
			return self.name+' '+self.type+" is disabled."
		return self.func(bot,text)

class bot:
	logout=False
	username=""
	password=""
	version=""
	description=""
	host=""
	#modules
	modes=[]
	services=[]
	commands=[]
	#user data
	admins=[]
	mods=[]
	def __init__(self,username,password,version,description,channel="general"):
		self.username=username
		self.password=password
		self.version=version
		self.description=description
		self.chat=u413lib.createclient()
		if not self.chat.login(username,password)
			print "Error: Login failed."
			exit()
		self.chat.joinchat(channel)
	def addmode(self,botmode):
		self.modes.append(botmode)
	def addcmd(self,botcmd):
		self.commands.append(botcmd)
	def addservice(self,botservice):
		self.services.append(botservice)
	def run(self):
		chatget=self.chat.get()
		if chatget:
			for text in chatget:
				output=[]
				#services
				for s in self.services:
					output.extend(s.run(self,text).split("||"))
				#commands
				if text["Type"]=="Message":
					args=text["Msg"].split(' ')
					for c in self.commands:
						if CK+c.name==args[0]:
							output.extend(c.run(self,text,args[1:]).split("||"))
							break
					#turning modes on/off
					for m in self.modes:
						if CK+m.name==args[0]:
							if len(args)==1:
								return self.modes[self.modes.index(m)].toggle()
							elif len(args)==2:
								if args[1]=="on":
									return self.modes[self.modes.index(m)].on()
								elif args[1]=="off":
									return self.modes[self.modes.index(m)].off()
								else:
									return "Proper usage: "+CK+m.name+' '+m.parameters+" - "+m.description
							else:
								return "Proper usage: "+CK+m.name+' '+m.parameters+" - "+m.description
				#modes
				out=[]
				for m in self.modes:
					for o in output:
						out.append(m.run(self,o))
				for o in out:
					self.chat.send(o)

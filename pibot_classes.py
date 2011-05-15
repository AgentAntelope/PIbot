import sys
sys.path.append("/home/pimaster/www/pibot/")
import u413lib
from pibot_constants import *

class module:
	#default values
	name=""
	modtype=""
	description=""
	version=""
	func=0
	disabled=False
	def enable(self):
		if not self.disabled:
			return self.name+" "+self.modtype+" is not disabled."
		self.disabled=False
		return self.name+" "+self.modtype+" is now enabled."
	def disable(self):
		if self.disabled:
			return self.name+" "+self.modtype+" is already disabled."
		self.disabled=True
		return self.name+" "+self.modtype+" is now disabled."

class command(module):
	#default values
	parameters=""
	level=user.basic
	modtype="command"
	def __init__(self,filename,bot):
		mod=__import__(filename)
		self.name=mod.name
		self.parameters=mod.parameters
		self.description=mod.description
		self.level=mod.level
		self.version=mod.version
		self.func=mod.func
		try:
			init=getattr(mod,"init")
			init(bot)
		except:
			pass
	def run(self,bot,text,args):
		if self.disabled:
			return CK+self.name+' '+self.modtype+" is disabled."
		return self.func(bot,text,args)

class service(module):
	#default values
	modtype="service"
	def __init__(self,filename,bot):
		mod=__import__(filename)
		self.name=mod.name
		self.description=mod.description
		self.version=mod.version
		self.infunc=mod.infunc
		self.outfunc=mod.outfunc
		try:
			init=getattr(mod,"init")
			init(bot)
		except:
			pass
	def run(self,bot,text,isout):
		if self.disable:
			return ""
		return self.func(bot,text)

class mode(module):
	#default values
	level=user.basic
	state=False
	modtype="mode"
	def on(self):
		if self.disabled:
			return self.name+" mode is disabled."
		if self.state:
			return self.name+" mode is already on."
		self.state=True
		return self.name+" mode is now on."
	def off(self):
		if self.disabled:
			return self.name+" mode is disabled."
		if not self.state:
			return self.name+" mode is already off."
		self.state=False
		return self.name+" mode is now off."
	def toggle(self):
		if self.disabled:
			return self.name+" mode is disabled."
		if self.state:
			self.state=False
			return self.name+" mode is now off."
		self.state=True
		return self.name+" mode is now on."
	def __init__(self,filename,bot):
		mod=__import__(filename)
		self.name=mod.name
		self.description=mod.description
		self.version=mod.version
		self.func=mod.func
		self.level=mod.level
		try:
			init=getattr(mod,"init")
			init(bot)
		except:
			pass
	def run(self,bot,text):
		return self.func(bot,text)

class bot:
	dologout=False
	username=""
	password=""
	version=""
	description=""
	#modules
	modes=[]
	services=[]
	commands=[]
	#user data
	admins=[]
	banned=[]
	bots=[]
	mods=[]
	def __init__(self,username,password,version,description,channel="general"):
		self.username=username
		self.password=password
		self.version=version
		self.description=description
		self.client=u413lib.createclient()
		if not self.client.login(username,password):
			print username,password
			exit()
		self.chat=self.client.joinchat(channel)
		self.client.sendRawCommand("channel "+channel)
		#load user data
		txtfile=open(www+"data/admins.txt","r")
		string=txtfile.read()
		admins=string.split('\n')
		txtfile.close()
		txtfile=open(www+"data/mods.txt","r")
		string=txtfile.read()
		admins=string.split('\n')
		txtfile.close()
		txtfile=open(www+"data/bots.txt","r")
		string=txtfile.read()
		bots=string.split('\n')
		txtfile.close()
		txtfile=open(www+"data/banned.txt","r")
		string=txtfile.read()
		banned=string.split('\n')
		txtfile.close()
	def addmode(self,botmode):
		self.modes.append(botmode)
	def addcmd(self,botcmd):
		self.commands.append(botcmd)
	def addservice(self,botservice):
		self.services.append(botservice)
	def logout(self):
		self.client.sendRawCommand("logout")
	def userlvl(self,username):
		if username==host:
			return user.host
		elif username in self.admins:
			return user.admin
		elif username in self.mods:
			return user.mod
		elif username in self.bots:
			return user.bot
		elif username in self.banned:
			return user.ban
		else:
			return user.basic
	def run(self):
		chatget=self.chat.get()
		if chatget:
			for text in chatget:
				output=[]
				#services
				for s in self.services:
					output.extend(s.infunc(self,text).split("||"))
				#commands
				if text["Type"]=="Message":
					args=text["Msg"].split(' ')
					for c in self.commands:
						if CK+c.name==args[0]:
							if self.userlvl(text["User"])>=c.level:
								output.extend(c.run(self,text,args[1:]).split("||"))
								break
				#modes
				for o in output:
					if o=="":
						continue
					out=o
					for m in self.modes:
						if not m.disabled and m.state:
							out=m.run(self,out)
					#run output services on output
					for s in self.services:
						if not s.disabled:
							s.outfunc(self,out)
					print out
					self.chat.send(out)

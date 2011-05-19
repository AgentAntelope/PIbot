import sys
import os
from pibot_constants import *
sys.path.append("/home/pimaster/www/pibot/")
import u413lib

def isvowel(letter):
	if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
		return True
	return False

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
	initexist=False
	def __init__(self,filename):
		mod=__import__(filename)
		self.name=mod.name
		self.parameters=mod.parameters
		self.description=mod.description
		self.level=mod.level
		self.version=mod.version
		self.func=mod.func
		try:
			self.init=getattr(mod,"init")
			self.initexist=True
		except:
			pass
	def run(self,bot,text,args):
		if self.disabled:
			return CK+self.name+' '+self.modtype+" is disabled."
		return self.func(bot,text,args)

class service(module):
	#default values
	modtype="service"
	initexist=False
	def __init__(self,filename):
		mod=__import__(filename)
		self.name=mod.name
		self.description=mod.description
		self.version=mod.version
		self.infunc=mod.infunc
		self.outfunc=mod.outfunc
		try:
			self.init=getattr(mod,"init")
			self.initexist=True
		except:
			pass

class mode(module):
	#default values
	level=user.basic
	state=False
	modtype="mode"
	initexist=False
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
	def __init__(self,filename):
		mod=__import__(filename)
		self.name=mod.name
		self.description=mod.description
		self.version=mod.version
		self.func=mod.func
		self.level=mod.level
		try:
			self.init=getattr(mod,"init")
			self.initexist=True
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
	channels=[]#list of (chat,chatname)
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
			exit()
		self.chat=self.client.joinchat(channel)
		self.client.sendRawCommand("channel "+channel)
		#admins
		txtfile=open(www+"data/admins.txt","r")
		string=txtfile.read().replace('\r','')
		txtfile.close()
		self.admins=string.split('\n')
		while '' in self.admins:
			self.admins.remove('')
		#mods
		txtfile=open(www+"data/mods.txt","r")
		string=txtfile.read().replace('\r','')
		txtfile.close()
		self.mods=string.split('\n')
		while '' in self.mods:
			self.mods.remove('')
		#bots
		txtfile=open(www+"data/bots.txt","r")
		string=txtfile.read().replace('\r','')
		txtfile.close()
		self.bots=string.split('\n')
		while '' in self.bots:
			self.bots.remove('')
		#banned
		txtfile=open(www+"data/banned.txt","r")
		string=txtfile.read().replace('\r','')
		txtfile.close()
		self.banned=string.split('\n')
		while '' in self.banned:
			self.banned.remove('')
	def addmode(self,botmode):
		self.modes.append(botmode)
	def addcmd(self,botcmd):
		self.commands.append(botcmd)
	def addservice(self,botservice):
		self.services.append(botservice)
	def initmodules(self):
		for c in self.commands:
			if c.initexist:
				c.init(self)
		for m in self.modes:
			if m.initexist:
				m.init(self)
		for s in self.services:
			if s.initexist:
				s.init(self)
	def loadmodules(self,cmddir,modedir,servdir):
		#load commands
		listing=os.listdir(cmddir)
		for f in listing:
			path=os.path.splitext(f)
			if path[1]==".py":
				self.addcmd(command(os.path.basename(path[0])))
		#load modes
		listing=os.listdir(modedir)
		for f in listing:
			path=os.path.splitext(f)
			if path[1]==".py":
				self.addmode(mode(os.path.basename(path[0])))
		#load services
		listing=os.listdir(servdir)
		for f in listing:
			path=os.path.splitext(f)
			if path[1]==".py":
				self.addservice(service(os.path.basename(path[0])))
	def logout(self):
		self.client.sendRawCommand("logout")
	def userlvl(self,username):
		username=username.lower()
		if username in self.banned:
			return user.ban
		elif username==host.lower():
			return user.host
		elif username in self.admins:
			return user.admin
		elif username in self.mods:
			return user.mod
		elif username in self.bots:
			return user.bot
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
							elif self.userlvl(text["User"])==0:
								output.append("You are banned from PIbot use.")
							else:
								article=""
								if isvowel(userlvlname(c.level)[0]):
									article="an"
								else:
									article="a"
								output.append("Error: "+CK+c.name+" is "+article+' '+userlvlname(c.level)+" command.")
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

from pibot_constants import *

name="help"
parameters="[module]"
description="Display the help information."
level=user.basic
version="1.0.1.3"

def init(bot):
	#dynamically create the help information
	helphtml="""<html>
	<head>
		<title>-=Using PIbot=-</title>
		<link href="../style.css" rel="stylesheet" type="text/css">
	</head>
	<body>
		<a href="http://jq.dyndns-free.com:3145/index.php">Homepage</a><br/>
		<p>[] denotes an optional field<p>
		<p>&lt;&gt; denotes an required field<p>
		<p>All PIbot commands begin with """+CK+"""<p><br/>
		<h2>Commands</h2>\n"""
	for c in bot.commands:
		helphtml+="<p> &gt; "+CK+c.name+' v'+c.version+' '+c.parameters.replace('<',"&lt;").replace('>',"&gt;")+" - "+c.description+" ("+userlvlname(c.level)+")</p>\n\t\t"
	helphtml+="<h2>Modes</h2>\n\t\t"
	for m in bot.modes:
		helphtml+="<p> &gt; "+m.name+" mode v"+m.version+" - "+c.description+" ("+userlvlname(m.level)+")</p>\n\t\t"
	helphtml+="<h2>Services</h2>\n\t\t"
	for s in bot.services:
		helphtml+="<p> &gt; "+s.name+" service v"+s.version+" - "+s.description+"</p>\n\t\t"
	helphtml=helphtml[:-1]
	helphtml+="</body>\n</html>"
	html=open(www+"data/help.html","w")
	html.write(helphtml)
	html.close()

def func(bot,text,args):
	if len(args)==0:
		bot.chat.send("Go to http://jq.dyndns-free.com:3145/data/help.html for help with PIbot.")
		return ""
	if len(args)==1:
		#check if it's a command
		for c in bot.commands:
			if c.name==args[0]:
				return CK+c.name+' '+c.parameters+" - "+c.description
		#check if it's a mode
		for m in bot.modes:
			if m.name==args[0]:
				return m.name+" mode - "+m.description
		#check if it's a service
		for s in bot.services:
			if s.name==args[0]:
				return s.name+" service - "+s.description
		return '"'+args[0]+'" is not a PIbot module.'
	return "Proper usage: "+CK+name+' '+parameters

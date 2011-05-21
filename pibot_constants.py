class user:
	ban=0
	basic=10
	bot=20
	trusted=30
	mod=40
	admin=50
	host=60

def userlvlname(userlvl):
	if userlvl==user.host:
		return "host"
	elif userlvl==user.admin:
		return "admin"
	elif userlvl==user.mod:
		return "mod"
	elif userlvl==user.trusted:
		return "trusted"
	elif userlvl==user.bot:
		return "bot"
	elif userlvl==user.basic:
		return "basic"
	elif userlvl==user.ban:
		return "banned"
	else:
		return "unknown"

CK="!"
delay=7
maxlen=512
host="PiMaster"
workingdir="/home/pimaster/www/pibot/2.0.0/"
www="/home/pimaster/www/"
delay=7

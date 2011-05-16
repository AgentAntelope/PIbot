import random
from pibot_constants import *

name="laioni"
description="Makes PIbot misspell things."
version="1.0.1.0"
level=user.basic

#letters that are cloes together on the keyboard
close={'q':['w'],'w':['q','2'],'e':['3'],'r':'r','t':['r','5'],'y':['y'],'u':['y'],'i':['8','k'],'o':['p','0'],'p':['o','['],'a':['s','d','q'],'s':['a','d'],'d':['s','e'],'f':['g'],'g':['f','h','t'],'h':['h'],'j':['k','h'],'k':['i'],'l':[';','o'],'z':['z'],'x':['x'],'c':['c'],'v':['b'],'n':['b'],'m':['n'],"'":[';'],'(':['9'],')':['0']}

mixrate=40
addrate=80

def mixletter(text):
	if len(text)>1:
		letters=list(text)
		while True:
			place=random.randrange(0,len(letters))
			if place>len(letters)/2:
				letters[place],letters[place-1]=letters[place-1],letters[place]
			else:
				letters[place],letters[place+1]=letters[place+1],letters[place]
			if not random.randrange(0,100)<=mixrate:
				break
		text=""
		for l in letters:
			text+=l
	return text

def badtype(text):
	letters=list(text)
	while True:
		place=random.randrange(0,len(letters))
		if letters[place] in close:
			if random.randrange(0,100)<=addrate:
				letters.insert(place,random.choice(close[letters[place]]))
			else:
				letters[place]=random.choice(close[letters[place]])
		if not random.randrange(0,100)<=mixrate:
			break
	text=""
	for l in letters:
		text+=l
	return text

def func(bot,text):
	text=mixletter(text)
	text=badtype(text)
	return text

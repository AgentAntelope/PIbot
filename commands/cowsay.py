from pibot_constants import *

name="cowsay"
parameters="<text>"
description="Make a cow say something."
version="1.0.0.1"
level=user.basic

def combine(params):
    string=""
    for s in params:
        string+=s+' '
    return string[:-1]
    


def func(bot,text,args):
    if len(args)==0:
        return "Proper usage: "+CK+name+' '+parameters
    argscomb=combine(args)
    cowpic = """\n ._______(o o) - """ + argscomb + """\n (_u413_\\/.(__) \n .||....|| """
    return(cowpic)

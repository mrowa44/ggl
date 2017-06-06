#!python 2
'''
https://github.com/Vinay26k/
'''
import os
import sys
import subprocess

def command(st):
    if st!=None:
        com = r'cmd /c start'
        com = 'start '+ com +' '+st
        os.system(com)
def y():
    com = 'https://www.youtube.com/results?search_query='+str('%20'.join(st[1:]))
    return com
def i():
    com = 'http://www.google.com/images?q='+str('%20'.join(st[1:]))
    return com
def g():
    com = 'https://www.google.com/search?q='+str('%20'.join(st[1:]))
    return com
def d():
    com = 'https://duckduckgo.com/?q='+str('%20'.join(st[1:]))
    return com
def s():
    com = 'http://stackoverflow.com/search?q='+str('%20'.join(st[1:]))
    return com
def w():
    com = 'http://www.wikipedia.org/w/index.php?search='+str('%20'.join(st[1:]))
    return com
def insta():
    com = 'https://www.instagram.com/'+str('%20'.join(st[1:]))
    return com
def fb():
    com = 'https://www.facebook.com/'+str('%20'.join(st[1:]))
    return com
def tw():
    com = 'https://twitter.com/'+str('%20'.join(st[1:]))
    return com
def cr():
    print('''
            https://github.com/vinay26k
''')
    com = 'start https://github.com/vinay26k'
    #os.system(com)
    return com
def e():
    sys.exit(0)
def usage():
    print('''
Search through following web engines as follows :
Command as:
    y|i|g|d|s|w|in|fb|tw|cr|u [search_terms]
     y - youtube search
     i - image search
     g - google search
     d - duckduckgo search
     s - stack overflow
     w - wiki
    in - instagram search
    fb - facebook search
    tw - twitter search
    cr - coded by details
     u - for usage
    type e to exit the program !
    
''')
    return None
usage()
while(1):
    st = raw_input().split()
    options= { 'y' : y,\
               'i' : i,\
               'g' : g,\
               'd' : d,\
               's' : s,\
               'w' : w,\
               'e' : e,\
               'in': insta,\
               'fb': fb,\
               'tw': tw,\
               'cr': cr,\
               'u' : usage\
           }
    command(options[st[0]]())

#! /usr/bin/env python
# Twitmote
# A remote control server for Twitter Direct Messages
# File created: 2009-05-09
# Author: Kyle Krafka

import getpass
import base64
import string # TODO: from string import strip
import httplib
from xml.dom import minidom
from os import system
import time

print "Greetings!  Please log your Twitter Bot in."

while True:
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")

    auth = 'Basic ' + \
    string.strip(base64.encodestring(username + ":" + password))
    conn = httplib.HTTPConnection('twitter.com')
    conn.putrequest('GET', '/direct_messages.xml?count=1')
    conn.putheader('Authorization', auth)
    conn.endheaders()
    resp = conn.getresponse()
    if resp.status == 200:
        print "You're good.\n"
        break
    else:
        print 'Your credentials could not be verified ("'+\
        `resp.status`+' '+\
        resp.reason+'").  Please try again.\n'

# Read the data into a string
data = resp.read()
dom = minidom.parseString(data)
since_id = dom.getElementsByTagName('direct_message')[0]\
.getElementsByTagName('id')[0].firstChild.nodeValue
loop_count = 0

# The initial since_id has been set, begin the regular message checking.
while True:
    conn.putrequest('GET', '/direct_messages.xml?since_id='+since_id)
    conn.putheader('Authorization', auth)
    conn.endheaders()
    resp = conn.getresponse()
    if resp.status == 200:
	data = resp.read()
	dom = minidom.parseString(data)
	# TODO: do this list in reverse
	textNodesReversed = dom.getElementsByTagName('text')
	textNodesReversed.reverse()
	for command in textNodesReversed:
	    command = command.firstChild.nodeValue
	    print "Command received:", command
        # Put logic for processing the command here, or directly interpret it
        system(command)
	# if last time, set new since_id
	if len(textNodesReversed) > 0: # if there were any new commands
	    since_id = dom.getElementsByTagName('direct_message')[0]\
	    .getElementsByTagName('id')[0].firstChild.nodeValue
	loop_count = loop_count + 1
	print "Just checked: ", loop_count
    # Don't exceed API rate limit
	time.sleep(36)
    else:
        print 'There was a problem connecting ("'+\
        `resp.status`+' '+\
        resp.reason+'").  Will continue to try.\n'

#!/usr/bin/env python3

print('Content-type: text/html\n')

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

arguments = cgi.FieldStorage()
for i in arguments.keys():
#  print(i)
 print('<title>'+arguments[i].value+'</title>')
 print(arguments[i].value)

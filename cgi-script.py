#!/usr/bin/env python

import os, json, cgi

print("Content-Type: text/html")
#print("Location: http://google.com/")
print
print("<HTML><BODY><H1>Hello, World!</H1>")
print("<FORM method = 'POST'><INPUT name = 'x'></FORM>")

form = cgi.FieldStorage()
 
print("<P>X was: " + cgi.escape(str(form.getvalue('x'))) + "</P>")

print("</BODY></HTML>")


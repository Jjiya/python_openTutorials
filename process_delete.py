#!python

import cgi, os
form = cgi.FieldStorage()

title = form["title"].value
os.remove("data/"+title)

print("Location: index.py")
print()
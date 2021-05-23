#!python

import cgi
form = cgi.FieldStorage()

title = form["title"].value
desc = form["desc"].value


createFile = open('data/'+title, 'w')
createFile.write(desc)

createFile.close()

print("Location: index.py?id="+title)
print()
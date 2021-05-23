#!python

import cgi, os
form = cgi.FieldStorage()

old_title = form["old_title"].value
new_title = form["new_title"].value
desc = form["new_desc"].value

modifyFile = open('data/'+old_title, 'w+')
modifyFile.write(desc)
modifyFile.close()

os.rename('data/'+old_title, 'data/'+new_title)


print("Location: index.py?id="+new_title)
print()
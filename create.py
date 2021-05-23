#!python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type: text/html; charset=utf-8\n")
import cgi,os

#os 모듈 이용해서 data폴더에 있는 파일 명들을 가져온 후 files에 저장
files = os.listdir('data')
listStr = ''
for item in files:  # files에 있는 리스트들을 반복문을 통해 <li>로 만들어준다.
    listStr += '<li><a href="index.py?id={id}">{id}</a></li>'.format(id=item)

form = cgi.FieldStorage() # cgi에서 제공하는 함수를 통해 페이지에 있는 정보들을 가져옴
if 'id' in form:
    pageId = form["id"].value
    f = open('data/'+pageId,'r', encoding='UTF-8')
    desc = f.read()
    f.close()
else:
    pageId = "Welcome"
    desc = "Hello, Web"

print('''
    <!doctype html>
    <html lang="ko">
    <head>
    <meta charset="utf-8">
    <title>web python </title>
    </head>
    <body>
    <h1><a href="index.py">Web</a></h1>
    <ol>
        {list}
    </ol>
    <a href="cerate.py">글쓰기</a>
    <form action="process_create.py" method="POST">
        <p>
            <input type="text" name="title" placeholder="제목"/>
        </p>    
        <p>
            <textarea rows="4" name="desc" placeholder="본문"></textarea>
        </p>    
        <p><input type="submit"></p>  
    </form>  
    </body>
    </html>
'''.format(list=listStr,title=pageId, description=desc))


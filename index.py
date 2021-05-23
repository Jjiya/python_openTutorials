#!python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type: text/html; charset=utf-8\n")
import cgi,os
# from tkinter import messagebox
# 삭제 여부 묻는 confirm 띄우고 싶었는데 이건 alret이고 몰라... 활용 못해봤음 onClick으로 안되나....
# https://doch12.tistory.com/32

# def checkDelete() :
    # messagebox.showinfo("삭제 여부", "정말 삭제하시겠습니까?")

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
    modify = '<a href="modify.py?id={}">수정하기</a>'.format(pageId)
    delete_action = '''
        <form action = "process_delete.py" method="POST">
            <input type="hidden" name="title" value="{}"/>
            <input type="submit" value="삭제">
        </form>
    '''.format(pageId)
else:
    pageId = "Welcome"
    desc = "Hello, Web"
    modify = ''
    delete_action = ''

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
    <a href="create.py">글쓰기</a>
    {update_link} {delete_action}
    <h2>{title}</h2>
    <p>{description}</p>
    </body>
    </html>
'''.format(list=listStr,title=pageId, description=desc, update_link=modify, delete_action=delete_action))
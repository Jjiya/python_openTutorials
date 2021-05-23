person = {"name":"Jjiya","age":0}

print(person["name"])
# print(person.name)    -> 파이썬은 객체에 접근할 때, person.key가 아니라 배열 가져오듯이 해야되네... 이렇게하면 AttributeError: 'dict' object has no attribute 'name' 에러남

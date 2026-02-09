x = input()
y = x.split("'")
y = x.split('"')
y = list(filter(lambda i:i !=" " and i!="",y))
if len(y) >= 2:
    for i in reversed(y):
        print(i)
else:
    print("none")

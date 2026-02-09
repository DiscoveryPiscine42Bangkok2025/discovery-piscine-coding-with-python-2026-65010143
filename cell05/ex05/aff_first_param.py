x = input()
y = x.split('"')
y = list(filter(lambda i:i !=" " and i!="",y))

if y == []:
    print("none")
else:
    print(y[0])

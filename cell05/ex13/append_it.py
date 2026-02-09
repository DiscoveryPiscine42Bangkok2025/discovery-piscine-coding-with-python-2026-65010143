x = input()
y = x.split("'")
y = x.split('"')
y = list(filter(lambda i:i !=" " and i!="",y))
if len(y) == 0:
    print('none')
else:
    for i in y:
        if i[-3:] != "ism":
            i = i + "ism"
            print(i)     

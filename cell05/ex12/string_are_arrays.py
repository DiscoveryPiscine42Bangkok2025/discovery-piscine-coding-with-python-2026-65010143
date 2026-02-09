x = input()
y = x.split("'")
y = x.split('"')
y = list(filter(lambda i:i !=" " and i!="",y))
if len(y) != 1:
    print('none')
else:
    n=0
    for i in y[0]:
        if i =="z":
            n+=1
        else:
            n+=0
    if n != 0:
        print("z"*n)
    else:
        print("none")
        

x = input()
x = x.split(" ")
y = list(filter(lambda i:i !=" ",x))
if len(y) != 2:
    print("none")
else:
    l,u =int(y[0]),int(y[1])
    a = []
    for i in range(l,u+1):
        a.append(i)
    print(a)

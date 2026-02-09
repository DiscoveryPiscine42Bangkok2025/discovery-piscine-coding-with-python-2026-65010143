def methods_everywhere(x=""):
    y = x.split("'")
    y = list(filter(lambda i:i !=" " and i!="",y))
    a =[]
    def enlarge(x):
        n = 8 - len(x)
        x = x + "Z"*n
        return x
    def shrink(x):
        x = x[0:8]
        return x
    
    if len(y) < 1:
        print("none")
    else:
        for i in y:
            if len(i) < 8 :
                w = enlarge(i)   
                a.append(w)
            elif len(i) > 8:
                w = shrink(i)
                a.append(w)
            else:
                a.append(i)
        for i in a:
            print(i)
x = input()
methods_everywhere(x)

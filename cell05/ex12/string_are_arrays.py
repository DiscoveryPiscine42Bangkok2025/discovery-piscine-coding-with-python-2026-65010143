import sys

y = sys.argv[1:]

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
        

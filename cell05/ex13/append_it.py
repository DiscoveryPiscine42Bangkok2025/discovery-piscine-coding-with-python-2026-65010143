import sys

y = sys.argv[1:]
if len(y) == 0:
    print('none')
else:
    for i in y:
        if i[-3:] != "ism":
            i = i + "ism"
            print(i)     

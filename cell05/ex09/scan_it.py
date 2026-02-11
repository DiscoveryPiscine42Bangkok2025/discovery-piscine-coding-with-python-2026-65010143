import sys

y = sys.argv[1:]


n = 0
if len(y) != 2:
    print("none")
else:
    key = y[0]
    scan = y[1]
    scan_list = list(scan.split(" "))
    for i in scan_list:
        if i == key:
            n+=1
        else:
            n+=0
    if n == 0:
        print("none")
    else:
        print(n)

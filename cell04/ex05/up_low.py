import sys
x = sys.argv[1]

for i in x:
    if i ==  i.lower():
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")
